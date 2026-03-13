#!/usr/bin/env python3
"""
Master Pipeline Orchestrator — Runs the full end-to-end video content
engine from niche selection to production-ready outputs.

This is the single-command entry point for generating a complete
content operation from initial parameters.

Usage:
    python scripts/pipeline.py \
        --interests "AI,finance,health" \
        --platforms youtube,instagram,x,tiktok \
        --budget 50 \
        --cadence 3 \
        --content-type faceless \
        --output-dir ./content-engine-output
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPTS_DIR = Path(__file__).parent


def run_script(script_name: str, args: list[str], capture: bool = True) -> str:
    """Run a pipeline script and return its output."""
    cmd = [sys.executable, str(SCRIPTS_DIR / script_name)] + args
    print(f"  ▸ Running: {' '.join(cmd[:4])}...", file=sys.stderr)
    
    result = subprocess.run(
        cmd,
        capture_output=capture,
        text=True,
        cwd=str(SCRIPTS_DIR.parent),
    )
    
    if result.returncode != 0:
        print(f"  ✗ Error in {script_name}: {result.stderr}", file=sys.stderr)
        return ""
    
    return result.stdout


def create_directory_structure(output_dir: Path) -> dict[str, Path]:
    """Create the full output directory structure."""
    dirs = {
        "intelligence": output_dir / "01-intelligence",
        "brand": output_dir / "02-brand",
        "strategy": output_dir / "03-strategy",
        "seo": output_dir / "04-seo",
        "scripts": output_dir / "05-scripts",
        "production": output_dir / "06-production",
        "platform_ops": output_dir / "07-platform-ops",
        "analytics": output_dir / "08-analytics",
    }
    
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)
    
    return dirs


def generate_master_playbook(
    config: dict[str, Any],
    dirs: dict[str, Path],
    output_dir: Path,
) -> str:
    """Generate the master playbook that links all deliverables."""
    return f"""# MASTER PLAYBOOK — Video Content Engine

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Niche Interests**: {', '.join(config['interests'])}
**Platforms**: {', '.join(config['platforms'])}
**Budget**: ${config['budget']}/month
**Upload Cadence**: {config['cadence']} videos/week
**Content Type**: {config['content_type']}

---

## Quick Start Checklist

- [ ] Review niche scorecard → `01-intelligence/niche-scorecard.md`
- [ ] Select top niche and confirm positioning
- [ ] Review visual style guide → `02-brand/visual-style-guide.json`
- [ ] Review 90-day calendar → `03-strategy/content-calendar-90day.md`
- [ ] Review SEO package → `04-seo/seo-package.md`
- [ ] Review first batch of scripts → `05-scripts/`
- [ ] Set up production tools per → `06-production/tool-chain.md`
- [ ] Configure platform accounts per → `07-platform-ops/platform-configs.md`
- [ ] Set up analytics tracking per → `08-analytics/kpi-framework.md`

---

## Phase Deliverables

### Phase 1: Intelligence
- [Niche Scorecard](01-intelligence/niche-scorecard.md) — Top niches ranked by weighted score
- [Competitor Analysis](01-intelligence/competitor-analysis.md) — Gap analysis for top niches
- [Positioning](01-intelligence/positioning.md) — Channel positioning statement

### Phase 2: Brand System
- [Visual Style Guide](02-brand/visual-style-guide.json) — Machine-readable style guide for AI tools
- [Thumbnail System](02-brand/thumbnail-system.md) — 3-variant thumbnail design system
- [Brand Kit](02-brand/brand-kit.md) — Colors, fonts, and visual identity rules

### Phase 3: Content Strategy
- [90-Day Calendar](03-strategy/content-calendar-90day.md) — Full upload calendar with entries
- [Series Concepts](03-strategy/series-concepts.md) — 2-3 recurring series with episode lists
- [Milestones](03-strategy/milestones.md) — Growth targets by month

### Phase 4: SEO & Discovery
- [SEO Package](04-seo/seo-package.md) — Keywords, titles, descriptions, tags
- [Keyword Database](04-seo/keyword-database.md) — Ranked keywords with volume and competition
- [Description Templates](04-seo/description-templates.md) — Copy-paste description templates

### Phase 5: Scripts
- Scripts for first {min(4, config['cadence'] * 2)} videos
- Companion Short scripts
- Platform-specific adaptations

### Phase 6: Production Pipeline
- [Tool Chain](06-production/tool-chain.md) — Recommended tools for ${config['budget']}/mo budget
- [Workflow SOP](06-production/workflow-sop.md) — Step-by-step production process
- [Cost Breakdown](06-production/cost-breakdown.md) — Monthly cost analysis

### Phase 7: Platform Operations
- [Platform Configs](07-platform-ops/platform-configs.md) — Per-platform technical specs
- [Scheduling Plan](07-platform-ops/scheduling-plan.md) — Weekly posting cadence

### Phase 8: Analytics
- [KPI Framework](08-analytics/kpi-framework.md) — Metrics to track with targets
- [A/B Testing SOP](08-analytics/ab-testing-sop.md) — Testing framework and log template

---

## Weekly Operating Rhythm

### Production Day (Batch Session — 5-7 hours)
1. Review upcoming calendar entries
2. Generate all scripts for the week
3. Batch-generate visual assets
4. Batch-generate voiceovers
5. Assemble all videos
6. Create thumbnails
7. Schedule uploads

### Upload Days ({config['cadence']}x/week)
1. Verify scheduled upload went live
2. Add end screens and cards
3. Cross-post adaptations to secondary platforms
4. Reply to comments for first 30 minutes
5. Share to relevant communities

### Weekly Review (30 minutes)
1. Review top and bottom performers
2. Note CTR and AVD trends
3. Update next week's calendar if needed
4. Log A/B test results

### Monthly Audit (60 minutes)
1. Full content performance audit
2. Update content calendar for next month
3. Review competitor landscape
4. Adjust strategy based on data

---

## Emergency Playbook

**If CTR drops below 3%**: Redesign thumbnails using Variant B or C approaches
**If AVD drops below 35%**: Rewrite hooks using a different hook type, add more pattern interrupts
**If subscriber growth stalls**: Launch a new series, increase Shorts output, experiment with collaborations
**If video gets flagged/restricted**: Review content against platform guidelines, appeal if appropriate, adjust future content

---

*This playbook was generated by the Video Content Engine. Execute each phase in order for maximum impact.*
"""


def run_pipeline(config: dict[str, Any]):
    """Execute the full pipeline."""
    output_dir = Path(config["output_dir"])
    dirs = create_directory_structure(output_dir)
    
    print("=" * 60, file=sys.stderr)
    print("VIDEO CONTENT ENGINE — Full Pipeline Execution", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print(f"Interests: {', '.join(config['interests'])}", file=sys.stderr)
    print(f"Platforms: {', '.join(config['platforms'])}", file=sys.stderr)
    print(f"Budget: ${config['budget']}/month", file=sys.stderr)
    print(f"Cadence: {config['cadence']} videos/week", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    
    # Phase 1: Niche Intelligence
    print("\n▶ Phase 1: Niche Intelligence", file=sys.stderr)
    niche_output = run_script("niche_analyzer.py", [
        "--interests", ",".join(config["interests"]),
        "--platforms", ",".join(config["platforms"]),
        "--top-n", "10",
        "--output", str(dirs["intelligence"] / "niche-scorecard.md"),
    ])
    
    # Create placeholder files for competitive analysis and positioning
    (dirs["intelligence"] / "competitor-analysis.md").write_text(
        f"# Competitor Analysis\n\n"
        f"**Niche**: [Selected from scorecard]\n"
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d')}\n\n"
        f"Use web search to fill in competitor data for the selected niche.\n"
        f"See references/niche-research.md for the competitor analysis template.\n\n"
        f"## Top 5 Competitors\n\n"
        f"[Run web search for: \"[niche] youtube channel faceless\" and analyze top results]\n",
        encoding="utf-8",
    )
    
    (dirs["intelligence"] / "positioning.md").write_text(
        f"# Positioning Statement\n\n"
        f"## Formula\n\n"
        f"For [target audience] who [specific need/frustration],\n"
        f"[Channel Name] is the [content format] channel that [unique value proposition]\n"
        f"unlike [competitor approach] because [defensible differentiator].\n\n"
        f"## Your Positioning\n\n"
        f"[Complete after reviewing niche scorecard and competitor analysis]\n",
        encoding="utf-8",
    )
    print("  ✓ Niche scorecard generated", file=sys.stderr)
    
    # Phase 2: Brand System
    print("\n▶ Phase 2: Brand System", file=sys.stderr)
    
    # Visual style guide JSON template
    style_guide = {
        "brand_identity": {
            "channel_name": "[CHANNEL NAME]",
            "niche": "[SELECTED NICHE FROM PHASE 1]",
            "positioning": "[POSITIONING STATEMENT FROM PHASE 1]",
            "visual_personality": ["professional", "modern", "trustworthy", "bold", "clean"],
        },
        "art_style": {
            "primary_style": "[SELECTED FROM NICHE SCORECARD RECOMMENDATIONS]",
            "style_prompt_prefix": "[Your consistent prompt prefix — paste before every AI image prompt]",
            "style_prompt_suffix": "8K resolution, cinematic lighting, professional quality, highly detailed",
            "negative_prompt": "blurry, low quality, text, watermark, logo, amateur, distorted",
            "reference_artists_or_movements": [],
            "rendering_quality": "8K, cinematic",
        },
        "color_palette": {
            "primary": {"hex": "#1E2761", "usage": "60% — backgrounds, large areas"},
            "secondary": {"hex": "#CADCFC", "usage": "25% — supporting elements"},
            "accent": {"hex": "#FFFFFF", "usage": "10% — CTAs, highlights"},
            "text_primary": {"hex": "#FFFFFF", "usage": "Headlines on dark"},
            "text_secondary": {"hex": "#B0B0B0", "usage": "Captions"},
            "background_dark": {"hex": "#0D1117", "usage": "Dark sections"},
            "background_light": {"hex": "#F5F5F5", "usage": "Light sections"},
        },
        "typography": {
            "headline_font": "[SELECT — see visual-brand.md reference]",
            "body_font": "[SELECT — see visual-brand.md reference]",
            "text_overlay_rules": {
                "max_words": 4,
                "stroke_or_shadow": True,
                "placement": "lower-third or rule-of-thirds",
            },
        },
        "thumbnail_system": {
            "layout_formula": "3-element: subject (60%) + text (20%) + background (20%)",
            "emotion_triggers": ["curiosity", "shock", "desire"],
        },
    }
    
    (dirs["brand"] / "visual-style-guide.json").write_text(
        json.dumps(style_guide, indent=2), encoding="utf-8"
    )
    
    # Thumbnail system
    thumbnail_output = run_script("thumbnail_designer.py", [
        "--title", f"[First Video Title — {config['interests'][0]}]",
        "--style", "Cinematic Realism",
        "--niche", config["interests"][0],
        "--output", str(dirs["brand"] / "thumbnail-system.md"),
    ])
    
    (dirs["brand"] / "brand-kit.md").write_text(
        "# Brand Kit\n\n"
        "See `visual-style-guide.json` for the complete machine-readable brand system.\n"
        "See `thumbnail-system.md` for the 3-variant thumbnail design approach.\n\n"
        "## Quick Reference\n\n"
        "- **Primary Color**: [From style guide]\n"
        "- **Font Pairing**: [From style guide]\n"
        "- **Art Style**: [From style guide]\n"
        "- **Thumbnail Formula**: 3-element (subject + text + background)\n",
        encoding="utf-8",
    )
    print("  ✓ Brand system generated", file=sys.stderr)
    
    # Phase 3: Content Strategy
    print("\n▶ Phase 3: Content Strategy", file=sys.stderr)
    calendar_output = run_script("content_calendar.py", [
        "--niche", config["interests"][0],
        "--cadence", str(config["cadence"]),
        "--platforms", ",".join(config["platforms"]),
        "--output", str(dirs["strategy"] / "content-calendar-90day.md"),
    ])
    print("  ✓ 90-day calendar generated", file=sys.stderr)
    
    # Phase 4: SEO
    print("\n▶ Phase 4: SEO & Discovery", file=sys.stderr)
    sample_titles = "|".join([
        f"How {config['interests'][0].title()} Is Changing Everything",
        f"7 {config['interests'][0].title()} Mistakes Everyone Makes",
        f"The Complete Guide to {config['interests'][0].title()} in 2026",
    ])
    seo_output = run_script("seo_optimizer.py", [
        "--niche", config["interests"][0],
        "--titles", sample_titles,
        "--output", str(dirs["seo"] / "seo-package.md"),
    ])
    print("  ✓ SEO package generated", file=sys.stderr)
    
    # Phase 5: Scripts
    print("\n▶ Phase 5: Script Generation", file=sys.stderr)
    script_topics = [
        f"How {config['interests'][0].title()} Is Changing Everything in 2026",
        f"7 {config['interests'][0].title()} Mistakes That Cost You Money",
        f"The Truth About {config['interests'][0].title()} Nobody Tells You",
        f"{config['interests'][0].title()} Explained in 10 Minutes",
    ]
    
    for i, topic in enumerate(script_topics, 1):
        run_script("script_generator.py", [
            "--topic", topic,
            "--length", "10",
            "--style", config["content_type"],
            "--visual-style", "Cinematic Realism",
            "--output", str(dirs["scripts"] / f"script-{i:03d}.md"),
        ])
    print(f"  ✓ {len(script_topics)} scripts generated", file=sys.stderr)
    
    # Phase 6: Production Pipeline
    print("\n▶ Phase 6: Production Pipeline", file=sys.stderr)
    budget = config["budget"]
    
    if budget == 0:
        tier = "free"
    elif budget <= 50:
        tier = "value"
    else:
        tier = "premium"
    
    (dirs["production"] / "tool-chain.md").write_text(
        f"# Tool Chain — ${budget}/month Budget ({tier.title()} Tier)\n\n"
        f"See `references/production-pipeline.md` for the complete tool chain with alternatives.\n\n"
        f"## Selected Stack\n\n"
        f"Budget tier: **{tier.title()}** (${budget}/mo)\n\n"
        f"| Stage | Tool | Cost |\n"
        f"|-------|------|------|\n"
        f"| Images | {'Leonardo AI Free' if tier == 'free' else 'Midjourney' if tier == 'premium' else 'Midjourney Basic'} | {'$0' if tier == 'free' else '$30/mo' if tier == 'premium' else '$10/mo'} |\n"
        f"| Voiceover | {'Edge TTS' if tier == 'free' else 'ElevenLabs' if tier == 'premium' else 'ElevenLabs Starter'} | {'$0' if tier == 'free' else '$22/mo' if tier == 'premium' else '$5/mo'} |\n"
        f"| Music | YouTube Audio Library | $0 |\n"
        f"| Editing | {'CapCut' if tier != 'premium' else 'DaVinci Resolve + RunwayML'} | {'$0' if tier != 'premium' else '$15/mo'} |\n"
        f"| Captions | {'CapCut' if tier == 'free' else 'Whisper (local)'} | $0 |\n"
        f"| Thumbnails | Canva {'Free' if tier == 'free' else 'Pro'} | {'$0' if tier == 'free' else '$15/mo'} |\n",
        encoding="utf-8",
    )
    
    (dirs["production"] / "workflow-sop.md").write_text(
        "# Production Workflow SOP\n\n"
        "See `references/production-pipeline.md` for the full SOP with batch production plans.\n\n"
        "## Quick Reference — Single Video (Under 3 Hours)\n\n"
        "1. **PREP** (30 min): Open calendar entry, review script, verify SEO package\n"
        "2. **ASSETS** (45 min): Generate images, queue voiceover, select music\n"
        "3. **ASSEMBLY** (60 min): Timeline sync, music bed, captions, intro/outro\n"
        "4. **THUMBNAIL** (15 min): Apply brand template, insert AI background, add text\n"
        "5. **UPLOAD** (15 min): Schedule upload, paste metadata, set end screens\n",
        encoding="utf-8",
    )
    
    (dirs["production"] / "cost-breakdown.md").write_text(
        f"# Monthly Cost Breakdown\n\n"
        f"**Budget**: ${budget}/month\n"
        f"**Tier**: {tier.title()}\n\n"
        f"See `references/production-pipeline.md` for detailed cost breakdowns by tier.\n",
        encoding="utf-8",
    )
    print("  ✓ Production pipeline configured", file=sys.stderr)
    
    # Phase 7: Platform Ops
    print("\n▶ Phase 7: Platform Operations", file=sys.stderr)
    (dirs["platform_ops"] / "platform-configs.md").write_text(
        "# Platform Configurations\n\n"
        "See `references/platform-ops.md` for complete technical specs per platform.\n\n"
        "## Active Platforms\n\n" +
        "\n".join(f"- {p.title()}" for p in config["platforms"]) +
        "\n\n## Cross-Platform Posting Cadence\n\n"
        "See `references/platform-ops.md` → Weekly Posting Cadence section.\n",
        encoding="utf-8",
    )
    
    (dirs["platform_ops"] / "scheduling-plan.md").write_text(
        f"# Scheduling Plan\n\n"
        f"**Cadence**: {config['cadence']} videos/week\n"
        f"**Platforms**: {', '.join(config['platforms'])}\n\n"
        f"See `references/platform-ops.md` → Posting Schedule Optimization for optimal times.\n",
        encoding="utf-8",
    )
    print("  ✓ Platform ops configured", file=sys.stderr)
    
    # Phase 8: Analytics
    print("\n▶ Phase 8: Analytics & Optimization", file=sys.stderr)
    (dirs["analytics"] / "kpi-framework.md").write_text(
        "# KPI Framework\n\n"
        "See `references/analytics-optimization.md` for the complete KPI framework.\n\n"
        "## Primary KPIs (Track Daily)\n\n"
        "| KPI | Target (New Channel) |\n"
        "|-----|---------------------|\n"
        "| CTR | 4-6% |\n"
        "| AVD | 40-50% of video length |\n"
        "| APV | 35-45% |\n"
        "| Impressions | Growing week-over-week |\n"
        "| Sub Conversion | 2-4% |\n",
        encoding="utf-8",
    )
    
    (dirs["analytics"] / "ab-testing-sop.md").write_text(
        "# A/B Testing SOP\n\n"
        "See `references/analytics-optimization.md` → A/B Testing Framework.\n\n"
        "## Testing Log\n\n"
        "| Test # | Date | Video | Variable | Variant A | Variant B | Metric | Result | Learning |\n"
        "|--------|------|-------|----------|-----------|-----------|--------|--------|----------|\n"
        "| 001 | | | | | | | | |\n",
        encoding="utf-8",
    )
    print("  ✓ Analytics framework configured", file=sys.stderr)
    
    # Master Playbook
    print("\n▶ Generating Master Playbook", file=sys.stderr)
    playbook = generate_master_playbook(config, dirs, output_dir)
    (output_dir / "MASTER-PLAYBOOK.md").write_text(playbook, encoding="utf-8")
    print("  ✓ Master playbook generated", file=sys.stderr)
    
    # Summary
    print("\n" + "=" * 60, file=sys.stderr)
    print("✓ PIPELINE COMPLETE", file=sys.stderr)
    print(f"  Output directory: {output_dir}", file=sys.stderr)
    print(f"  Start with: MASTER-PLAYBOOK.md", file=sys.stderr)
    print("=" * 60, file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Video Content Engine — Master Pipeline")
    parser.add_argument("--interests", required=True, help="Comma-separated interests/topics")
    parser.add_argument("--platforms", default="youtube,instagram,x,tiktok",
                       help="Target platforms (comma-separated)")
    parser.add_argument("--budget", type=int, default=0, help="Monthly budget in USD")
    parser.add_argument("--cadence", type=int, default=3, help="Videos per week")
    parser.add_argument("--content-type", default="faceless",
                       choices=["faceless", "talking_head", "hybrid", "shorts_only"])
    parser.add_argument("--output-dir", default="./content-engine-output",
                       help="Output directory")
    
    args = parser.parse_args()
    
    config = {
        "interests": [i.strip() for i in args.interests.split(",")],
        "platforms": [p.strip() for p in args.platforms.split(",")],
        "budget": args.budget,
        "cadence": args.cadence,
        "content_type": args.content_type,
        "output_dir": args.output_dir,
    }
    
    run_pipeline(config)


if __name__ == "__main__":
    main()
