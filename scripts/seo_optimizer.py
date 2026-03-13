#!/usr/bin/env python3
"""
SEO Optimizer — Generates complete SEO packages for video content:
titles, descriptions, tags, hashtags, and metadata for all platforms.

Usage:
    python scripts/seo_optimizer.py --niche "AI tools" \
        --titles "How AI Replaces Marketing Teams|7 AI Tools You Need in 2026"
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


TITLE_FORMULAS = [
    {"name": "number_outcome", "template": "{number} {things} That {outcome}", "psychology": "Specificity + benefit"},
    {"name": "why_authority", "template": "Why {authority} {surprising_action}", "psychology": "Credibility + curiosity"},
    {"name": "experiment", "template": "I {did_x} for {time} — Here's What Happened", "psychology": "Personal experiment + open loop"},
    {"name": "lie_truth", "template": "{topic} Is a Lie (Here's the Truth)", "psychology": "Contrarian + revelation"},
    {"name": "how_group", "template": "How {group} {achieves_outcome}", "psychology": "Blueprint + aspiration"},
    {"name": "explained", "template": "{topic} Explained in {time}", "psychology": "Value + time commitment"},
    {"name": "complete_guide", "template": "The {adjective} Guide to {topic}", "psychology": "Comprehensiveness"},
    {"name": "year_change", "template": "{year} {topic}: Everything Changed", "psychology": "Timeliness + stakes"},
    {"name": "urgency", "template": "{do_this} Before {deadline}", "psychology": "Urgency + fear"},
    {"name": "data_reveals", "template": "What {data_point} Reveals About {topic}", "psychology": "Data-driven + insight"},
    {"name": "stop_start", "template": "Stop {mistake} — Do {better_action} Instead", "psychology": "Correction + solution"},
    {"name": "targeted", "template": "{topic} for {audience} ({promise})", "psychology": "Targeted + concrete"},
]

POWER_WORDS = [
    "Ultimate", "Complete", "Secret", "Revealed", "Proven", "Shocking",
    "Essential", "Critical", "Insane", "Brutal", "Game-Changing",
    "Revolutionary", "Hidden", "Deadly", "Massive", "Explosive",
]

TAG_TIERS = {
    "tier1": "Exact-match primary and secondary keywords (3-5 tags)",
    "tier2": "Long-tail keyword variations (5-7 tags)",
    "tier3": "Broad niche terms (3-5 tags)",
    "tier4": "Channel name and series name for branding (2-3 tags)",
}


def generate_title_variants(base_title: str, niche: str) -> list[dict]:
    """Generate title variants using proven formulas."""
    variants = []
    
    # Original title analysis
    variants.append({
        "title": base_title,
        "type": "original",
        "char_count": len(base_title),
        "has_number": any(c.isdigit() for c in base_title),
        "under_60_chars": len(base_title) <= 60,
        "notes": [],
    })
    
    # Add notes
    if len(base_title) > 60:
        variants[0]["notes"].append("WARNING: Over 60 chars — will truncate on mobile")
    if not any(c.isdigit() for c in base_title):
        variants[0]["notes"].append("Consider adding a number — titles with numbers get ~36% higher CTR")
    
    # Generate formula-based variants
    for formula in TITLE_FORMULAS[:6]:  # Top 6 most versatile formulas
        variants.append({
            "title": f"[Apply '{formula['name']}' formula: {formula['template']}]",
            "type": "formula_variant",
            "formula": formula["name"],
            "psychology": formula["psychology"],
            "template": formula["template"],
        })
    
    return variants


def generate_description(title: str, niche: str, keywords: list[str]) -> str:
    """Generate an SEO-optimized video description."""
    primary_kw = keywords[0] if keywords else f"[PRIMARY KEYWORD for {niche}]"
    secondary_kws = keywords[1:4] if len(keywords) > 1 else [f"[SECONDARY KW {i}]" for i in range(1, 4)]
    
    return f"""[HOOK: 1-2 compelling sentences expanding on the title's promise. Include {primary_kw} naturally in the first sentence. This appears in search results — make every word count.]

In this video, [2-sentence summary of what viewers will learn]. Whether you're [audience segment 1] or [audience segment 2], this breakdown gives you [specific actionable value].

🔑 Key Takeaways:
00:00 — Introduction
[MM:SS] — [Chapter 2: First Major Point]
[MM:SS] — [Chapter 3: Second Major Point]
[MM:SS] — [Chapter 4: Third Major Point]
[MM:SS] — [Chapter 5: The Key Insight]
[MM:SS] — [Chapter 6: Action Steps]

📌 Resources Mentioned:
- [Resource 1 — with URL]
- [Resource 2 — with URL]
- [Resource 3 — with URL]

🔗 Related Videos:
- [INTERNAL LINK: Related video title 1] — [URL]
- [INTERNAL LINK: Related video title 2] — [URL]
- [INTERNAL LINK: Related video title 3] — [URL]

📢 Connect:
- [Platform 1 with link]
- [Platform 2 with link]

#{primary_kw.replace(' ', '')} #{secondary_kws[0].replace(' ', '').replace('[', '').replace(']', '')} #{secondary_kws[1].replace(' ', '').replace('[', '').replace(']', '')}

---
{primary_kw.title()} is one of the most important topics in {niche} right now. Understanding {secondary_kws[0] if not secondary_kws[0].startswith('[') else 'the core concepts'} can help you make better decisions and stay ahead. This video breaks down everything you need to know about {primary_kw} in a clear, actionable format.
"""


def generate_tag_strategy(niche: str, keywords: list[str], channel_name: str = "[CHANNEL NAME]") -> dict:
    """Generate a complete tag strategy."""
    primary = keywords[0] if keywords else f"{niche} guide"
    
    return {
        "tag_architecture": TAG_TIERS,
        "suggested_tags": {
            "tier1_exact_match": [
                primary,
                f"{primary} explained",
                f"{primary} tutorial",
            ],
            "tier2_long_tail": [
                f"{primary} for beginners",
                f"how to {primary}",
                f"best {primary}",
                f"{primary} tips",
                f"{primary} mistakes",
            ],
            "tier3_broad": [
                niche,
                f"{niche} tips",
                f"{niche} guide",
            ],
            "tier4_branding": [
                channel_name,
                f"{channel_name} {niche}",
            ],
        },
        "total_estimated_chars": "[Calculate — must be under 500 total]",
        "rules": [
            "First tag = exact primary keyword",
            "Mix broad and specific",
            "Never use irrelevant tags (YouTube penalizes this)",
            "Include common misspellings if search volume exists",
            "Update tags based on YouTube Studio search term data after 2 weeks",
        ],
    }


def generate_seo_package(
    niche: str,
    titles: list[str],
    keywords: list[str] | None = None,
    channel_name: str = "[CHANNEL NAME]",
) -> str:
    """Generate a complete SEO package in markdown format."""
    if keywords is None:
        keywords = [f"{niche} guide", f"best {niche}", f"{niche} explained"]
    
    lines = [
        f"# SEO Package — {niche.title()}",
        "",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Niche**: {niche}",
        f"**Videos**: {len(titles)}",
        "",
        "---",
        "",
        "## Title Formulas Reference",
        "",
        "| # | Formula | Psychology |",
        "|---|---------|-----------|",
    ]
    
    for i, f in enumerate(TITLE_FORMULAS, 1):
        lines.append(f"| {i} | `{f['template']}` | {f['psychology']} |")
    
    lines.extend([
        "",
        f"**Power Words to Inject**: {', '.join(POWER_WORDS[:10])}",
        "",
        "---",
    ])
    
    # Per-video SEO packages
    for idx, title in enumerate(titles, 1):
        variants = generate_title_variants(title, niche)
        description = generate_description(title, niche, keywords)
        tags = generate_tag_strategy(niche, keywords, channel_name)
        
        lines.extend([
            "",
            f"## Video {idx}: {title}",
            "",
            "### Title Variants",
            "",
        ])
        
        for v in variants:
            if v.get("type") == "original":
                notes = " | ".join(v["notes"]) if v["notes"] else "OK"
                lines.append(f"- **Original**: `{v['title']}` ({v['char_count']} chars) — {notes}")
            else:
                lines.append(f"- **{v.get('formula', 'variant')}** ({v.get('psychology', '')}): {v['title']}")
        
        lines.extend([
            "",
            "### Description",
            "",
            "```",
            description,
            "```",
            "",
            "### Tags",
            "",
        ])
        
        for tier, tag_list in tags["suggested_tags"].items():
            lines.append(f"**{tier.replace('_', ' ').title()}**: {', '.join(tag_list)}")
        
        lines.extend([
            "",
            "### Shorts Funnel",
            f"- **Short Hook**: [Extract the most surprising 30 seconds from this video]",
            f"- **Short CTA**: 'Full breakdown in the video above ☝️'",
            f"- **Pinned Comment**: Link to this video with context",
            "",
            "---",
        ])
    
    # Keyword database
    lines.extend([
        "",
        "## Keyword Database",
        "",
        "| Keyword | Est. Volume | Competition | Intent | New Channel Rank? | Priority |",
        "|---------|-----------|-------------|--------|-------------------|----------|",
    ])
    
    for kw in keywords:
        lines.append(f"| {kw} | [RESEARCH] | [Low/Med/High] | [Info/Nav/Trans] | [Yes/Maybe/No] | [P1/P2/P3] |")
    
    lines.extend([
        "",
        "*Use web search to fill in actual search volume and competition data for each keyword.*",
        "",
        "---",
        "",
        "## Hashtag Strategy",
        "",
        "| Platform | Hashtag Count | Strategy |",
        "|----------|-------------|----------|",
        "| YouTube | 3-5 | First 3 appear above title in some views |",
        "| Instagram | 5-10 | Mix niche-specific + trending |",
        "| TikTok | 3-5 | At least one trending hashtag |",
        "| X/Twitter | 1-2 | Conversation hashtags only |",
        "| LinkedIn | 3-5 | Professional/industry hashtags |",
    ])
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="SEO Optimizer")
    parser.add_argument("--niche", required=True, help="Content niche")
    parser.add_argument("--titles", required=True, help="Video titles (pipe-separated)")
    parser.add_argument("--keywords", default=None, help="Target keywords (comma-separated)")
    parser.add_argument("--channel-name", default="[CHANNEL NAME]", help="Channel name for branding tags")
    parser.add_argument("--output", default=None, help="Output file path")
    
    args = parser.parse_args()
    titles = [t.strip() for t in args.titles.split("|")]
    keywords = [k.strip() for k in args.keywords.split(",")] if args.keywords else None
    
    output = generate_seo_package(args.niche, titles, keywords, args.channel_name)
    
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"SEO package written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
