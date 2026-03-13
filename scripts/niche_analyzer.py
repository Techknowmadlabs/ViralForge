#!/usr/bin/env python3
"""
Niche Analyzer — Competitive intelligence and niche scoring engine.

Generates a comprehensive niche scorecard with competitive analysis,
sub-niche identification, and positioning recommendations.

Usage:
    python scripts/niche_analyzer.py --interests "ai,finance,health" --platforms youtube,instagram
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


# === CPM Reference Database ===
# Approximate CPM ranges by niche category (USD, YouTube)
CPM_DATABASE: dict[str, dict[str, Any]] = {
    "finance": {"low": 12, "high": 45, "avg": 25, "trend": "stable"},
    "technology": {"low": 8, "high": 30, "avg": 18, "trend": "growing"},
    "business": {"low": 10, "high": 35, "avg": 20, "trend": "growing"},
    "health": {"low": 6, "high": 22, "avg": 14, "trend": "stable"},
    "education": {"low": 5, "high": 18, "avg": 10, "trend": "growing"},
    "science": {"low": 4, "high": 15, "avg": 9, "trend": "growing"},
    "self_improvement": {"low": 5, "high": 20, "avg": 12, "trend": "growing"},
    "real_estate": {"low": 10, "high": 40, "avg": 22, "trend": "stable"},
    "cryptocurrency": {"low": 8, "high": 35, "avg": 18, "trend": "volatile"},
    "programming": {"low": 6, "high": 25, "avg": 15, "trend": "growing"},
    "ai_ml": {"low": 10, "high": 35, "avg": 20, "trend": "growing"},
    "marketing": {"low": 8, "high": 28, "avg": 16, "trend": "stable"},
    "gaming": {"low": 2, "high": 8, "avg": 4, "trend": "stable"},
    "entertainment": {"low": 2, "high": 6, "avg": 3, "trend": "declining"},
    "travel": {"low": 4, "high": 15, "avg": 8, "trend": "recovering"},
    "food_cooking": {"low": 3, "high": 12, "avg": 6, "trend": "stable"},
    "fitness": {"low": 4, "high": 15, "avg": 8, "trend": "stable"},
    "psychology": {"low": 5, "high": 18, "avg": 10, "trend": "growing"},
    "history": {"low": 3, "high": 10, "avg": 6, "trend": "stable"},
    "true_crime": {"low": 3, "high": 12, "avg": 7, "trend": "stable"},
    "law": {"low": 8, "high": 30, "avg": 18, "trend": "stable"},
    "automotive": {"low": 5, "high": 20, "avg": 12, "trend": "stable"},
    "insurance": {"low": 15, "high": 50, "avg": 30, "trend": "stable"},
    "saas": {"low": 12, "high": 40, "avg": 25, "trend": "growing"},
}

# === Visual Style Recommendations ===
VISUAL_STYLE_MAP: dict[str, list[str]] = {
    "finance": ["Cinematic Realism", "Flat Design / Infographic", "Dramatic Dark Mode"],
    "technology": ["Isometric Illustration", "3D Rendered", "Cinematic Realism"],
    "business": ["Flat Design / Infographic", "Cinematic Realism", "2D Animation"],
    "health": ["Watercolor / Soft Illustration", "2D Animation", "Flat Design"],
    "education": ["2D Animation", "Isometric Illustration", "Flat Design"],
    "science": ["Cinematic Realism", "3D Rendered", "Isometric Illustration"],
    "self_improvement": ["Watercolor / Soft Illustration", "Cinematic Realism", "2D Animation"],
    "ai_ml": ["Isometric Illustration", "3D Rendered", "Dramatic Dark Mode"],
    "gaming": ["Pixel Art / 8-bit", "Anime / Manga", "3D Rendered"],
    "true_crime": ["Dramatic Dark Mode", "Photojournalistic", "Collage / Mixed Media"],
    "history": ["Retro / Vintage", "Cinematic Realism", "Photojournalistic"],
    "programming": ["Isometric Illustration", "Flat Design", "Dramatic Dark Mode"],
}

# === Production Ease Scores ===
PRODUCTION_EASE: dict[str, int] = {
    "finance": 9,       # Mostly graphs, charts, text — very AI-friendly
    "technology": 8,     # Illustrations, diagrams — AI handles well
    "business": 8,       # Similar to finance
    "health": 7,         # Some medical accuracy needed
    "education": 9,      # Diagrams, explanations — perfect for AI
    "science": 7,        # Complex visuals, accuracy critical
    "self_improvement": 8, # Abstract concepts, mood imagery
    "ai_ml": 8,          # Tech diagrams, code visuals
    "gaming": 6,         # May need game footage
    "entertainment": 5,  # Often needs real footage
    "true_crime": 7,     # Can use stock + AI dramatization
    "history": 7,        # AI-generated period scenes + stock
    "programming": 9,    # Code, diagrams, terminal recordings
}


def generate_niche_crossovers(interests: list[str]) -> list[dict[str, Any]]:
    """Generate niche candidates by crossing user interests with high-value categories."""
    candidates = []
    
    # Direct matches
    for interest in interests:
        interest_lower = interest.lower().strip().replace(" ", "_")
        if interest_lower in CPM_DATABASE:
            candidates.append({
                "name": interest.strip().title(),
                "category": interest_lower,
                "type": "direct",
                "description": f"Direct coverage of {interest.strip()}"
            })
    
    # Cross-pollination: interest × high-CPM category
    high_cpm = [k for k, v in CPM_DATABASE.items() if v["avg"] >= 15]
    for interest in interests:
        interest_clean = interest.strip().lower()
        for hc in high_cpm:
            hc_clean = hc.replace("_", " ")
            if interest_clean != hc_clean:
                candidates.append({
                    "name": f"{interest.strip().title()} × {hc_clean.title()}",
                    "category": hc,
                    "type": "crossover",
                    "description": f"{interest.strip().title()} topics through the lens of {hc_clean}"
                })
    
    # Sub-niche variants
    sub_niche_patterns = [
        "{interest} for beginners",
        "{interest} explained simply",
        "{interest} case studies",
        "{interest} vs alternatives",
        "dark side of {interest}",
        "{interest} myths debunked",
        "{interest} for professionals",
        "future of {interest}",
    ]
    for interest in interests:
        for pattern in sub_niche_patterns:
            name = pattern.format(interest=interest.strip().title())
            interest_lower = interest.lower().strip().replace(" ", "_")
            cat = interest_lower if interest_lower in CPM_DATABASE else "education"
            candidates.append({
                "name": name,
                "category": cat,
                "type": "sub_niche",
                "description": f"Focused sub-niche: {name}"
            })
    
    return candidates


def score_niche(niche: dict[str, Any]) -> dict[str, Any]:
    """Score a niche candidate across the 6-dimension framework."""
    cat = niche["category"]
    cpm_data = CPM_DATABASE.get(cat, {"low": 3, "high": 10, "avg": 5, "trend": "unknown"})
    prod_ease = PRODUCTION_EASE.get(cat, 6)
    
    # CPM Score (1-10, based on average CPM)
    cpm_score = min(10, max(1, round(cpm_data["avg"] / 5)))
    
    # Production Ease Score
    ease_score = prod_ease
    
    # Competition Density (estimate — crossovers and sub-niches have less competition)
    base_competition = 5  # default medium
    if niche["type"] == "crossover":
        base_competition = 7  # less saturated
    elif niche["type"] == "sub_niche":
        base_competition = 8  # even less saturated
    elif niche["type"] == "direct":
        base_competition = 4  # more saturated
    
    # Monetization Paths (finance, tech, SaaS have more)
    monetization_map = {
        "finance": 9, "insurance": 9, "saas": 9, "real_estate": 8,
        "technology": 8, "business": 8, "ai_ml": 8, "marketing": 8,
        "cryptocurrency": 7, "programming": 7, "law": 7,
        "health": 6, "education": 6, "self_improvement": 6,
        "fitness": 5, "science": 5, "automotive": 5,
        "travel": 4, "food_cooking": 4, "psychology": 5,
        "history": 3, "true_crime": 3, "gaming": 4, "entertainment": 3,
    }
    monetization_score = monetization_map.get(cat, 5)
    
    # Trend Trajectory
    trend_map = {"growing": 8, "stable": 6, "recovering": 5, "volatile": 4, "declining": 3, "unknown": 5}
    trend_score = trend_map.get(cpm_data["trend"], 5)
    
    # Audience Size (rough estimate based on category breadth)
    audience_map = {
        "finance": 8, "technology": 9, "health": 9, "education": 9,
        "gaming": 10, "entertainment": 10, "business": 7, "science": 7,
        "self_improvement": 8, "ai_ml": 7, "programming": 6,
        "fitness": 8, "food_cooking": 8, "travel": 7, "true_crime": 7,
        "history": 6, "psychology": 7, "marketing": 5, "law": 4,
        "real_estate": 6, "cryptocurrency": 6, "saas": 4, "insurance": 3,
        "automotive": 6,
    }
    audience_score = audience_map.get(cat, 5)
    if niche["type"] == "sub_niche":
        audience_score = max(1, audience_score - 2)
    elif niche["type"] == "crossover":
        audience_score = max(1, audience_score - 1)
    
    # Weighted Score
    weighted = (
        cpm_score * 0.25 +
        audience_score * 0.20 +
        ease_score * 0.20 +
        base_competition * 0.15 +
        monetization_score * 0.10 +
        trend_score * 0.10
    )
    
    # Visual style recommendations
    styles = VISUAL_STYLE_MAP.get(cat, ["2D Animation", "Flat Design", "Cinematic Realism"])
    
    return {
        **niche,
        "scores": {
            "cpm": {"score": cpm_score, "data": cpm_data},
            "audience_size": {"score": audience_score},
            "production_ease": {"score": ease_score},
            "competition_density": {"score": base_competition},
            "monetization_paths": {"score": monetization_score},
            "trend_trajectory": {"score": trend_score, "direction": cpm_data["trend"]},
        },
        "weighted_score": round(weighted, 2),
        "recommended_visual_styles": styles,
    }


def generate_scorecard_markdown(scored_niches: list[dict[str, Any]], top_n: int = 10) -> str:
    """Generate a markdown scorecard from scored niches."""
    sorted_niches = sorted(scored_niches, key=lambda x: x["weighted_score"], reverse=True)[:top_n]
    
    lines = [
        f"# Niche Scorecard — Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Top Niches by Weighted Score",
        "",
        "| Rank | Niche | Weighted Score | CPM | Audience | Ease | Competition | Monetization | Trend | Visual Style |",
        "|------|-------|---------------|-----|----------|------|-------------|-------------|-------|-------------|",
    ]
    
    for i, niche in enumerate(sorted_niches, 1):
        s = niche["scores"]
        styles = ", ".join(niche["recommended_visual_styles"][:2])
        lines.append(
            f"| {i} | **{niche['name']}** | **{niche['weighted_score']}** | "
            f"{s['cpm']['score']}/10 | {s['audience_size']['score']}/10 | "
            f"{s['production_ease']['score']}/10 | {s['competition_density']['score']}/10 | "
            f"{s['monetization_paths']['score']}/10 | {s['trend_trajectory']['score']}/10 ({s['trend_trajectory']['direction']}) | "
            f"{styles} |"
        )
    
    # Top pick deep dive
    top = sorted_niches[0]
    lines.extend([
        "",
        "---",
        "",
        f"## #1 Pick: {top['name']}",
        "",
        f"**Type**: {top['type'].replace('_', ' ').title()}",
        f"**Description**: {top['description']}",
        f"**Weighted Score**: {top['weighted_score']} / 10",
        "",
        f"### CPM Potential",
        f"- Average CPM: ${top['scores']['cpm']['data']['avg']}",
        f"- Range: ${top['scores']['cpm']['data']['low']} - ${top['scores']['cpm']['data']['high']}",
        f"- Trend: {top['scores']['cpm']['data']['trend']}",
        "",
        f"### Recommended Visual Styles",
    ])
    for style in top["recommended_visual_styles"]:
        lines.append(f"- {style}")
    
    lines.extend([
        "",
        "### Next Steps",
        "1. Run competitor analysis on this niche (search for top channels)",
        "2. Validate sub-niche with keyword research (Phase 4)",
        "3. Create visual style guide (Phase 2)",
        "4. Build 90-day content calendar (Phase 3)",
    ])
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Niche Analyzer — Score and rank content niches")
    parser.add_argument("--interests", required=True, help="Comma-separated list of interests/topics")
    parser.add_argument("--platforms", default="youtube,instagram", help="Target platforms (comma-separated)")
    parser.add_argument("--top-n", type=int, default=10, help="Number of top niches to display")
    parser.add_argument("--output", default=None, help="Output file path (default: stdout)")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Output format")
    
    args = parser.parse_args()
    interests = [i.strip() for i in args.interests.split(",")]
    
    # Generate candidates
    candidates = generate_niche_crossovers(interests)
    
    # Score all candidates
    scored = [score_niche(c) for c in candidates]
    
    # Sort and output
    if args.format == "markdown":
        output = generate_scorecard_markdown(scored, args.top_n)
    else:
        sorted_niches = sorted(scored, key=lambda x: x["weighted_score"], reverse=True)[:args.top_n]
        output = json.dumps(sorted_niches, indent=2)
    
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
