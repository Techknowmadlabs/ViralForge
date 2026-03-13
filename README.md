<div align="center">

# ViralForge

**Video content pipeline for social media platforms**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776ab.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-7c3aed.svg)](https://claude.ai)

End-to-end video content creation — from niche research through scriptwriting, SEO, production, and cross-platform publishing. Runs as a Claude Code skill or standalone Python CLI.

[Get Started](#quick-start) · [Architecture](#architecture) · [Pipeline](#the-8-phase-pipeline) · [CLI Tools](#cli-tools) · [Install as Skill](#install-as-claude-code-skill)

</div>

---

## Overview

ViralForge orchestrates an 8-phase pipeline covering niche selection, brand identity, content strategy, SEO, scriptwriting, production workflows, platform adaptation, and analytics. Each phase produces complete, ready-to-use outputs that feed directly into the next.

The system includes 7 Python CLI tools (stdlib-only, no pip dependencies), 8 reference playbooks totaling 50,000+ words of methodology, and cross-platform adaptation for YouTube, Instagram, TikTok, X, Facebook, and LinkedIn.

---

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                     VIRALFORGE PIPELINE                      │
├──────────┬──────────┬──────────┬──────────┬──────────┬───────┤
│ Phase 1  │ Phase 2  │ Phase 3  │ Phase 4  │ Phase 5  │   6   │
│  Intel   │  Brand   │ Strategy │   SEO    │  Script  │ Prod. │
├──────────┴──────────┴──────────┴──────────┴──────────┴───────┤
│ Phase 7: Platform Operations (6 platforms)                   │
├──────────────────────────────────────────────────────────────┤
│ Phase 4: Analytics, Optimization & Iteration                 │
└──────────────────────────────────────────────────────────────┘
```

---

## The 8-Phase Pipeline

| Phase | Name | What It Does | Script |
|-------|------|-------------|--------|
| 1 | Niche Intelligence | Scores niches across 6 dimensions (demand, competition, monetization, production ease, longevity, passion) | `niche_analyzer.py` |
| 2 | Visual Brand System | Generates visual identity with 12 style archetypes and scene prompt libraries | — |
| 3 | Content Strategy | Builds 90-day content calendars with pillar/cluster architecture | `content_calendar.py` |
| 4 | SEO & Discovery | Generates title variants, descriptions, tag strategies, and Shorts funnels | `seo_optimizer.py` |
| 5 | Scriptwriting Engine | Creates retention-optimized scripts with hooks, pattern interrupts, and visual cues | `script_generator.py` |
| 6 | Production Pipeline | Defines tool chains, SOPs, and cost-tiered workflows ($0 / $50 / $150/mo) | — |
| 7 | Platform Operations | Adapts master content for YouTube, Instagram, TikTok, X, Facebook, LinkedIn | `platform_adapter.py` |
| 8 | Analytics & Iteration | KPI frameworks, A/B testing protocols, retention analysis, monetization roadmaps | — |

The orchestrator `pipeline.py` runs all phases in sequence and generates a master playbook.

---

## CLI Tools

All scripts use Python 3.10+ stdlib only — no `pip install` required.

```bash
# Score and rank niches
python scripts/niche_analyzer.py --interests "ai,finance,health" --platforms youtube,instagram

# Generate 90-day content calendar
python scripts/content_calendar.py --niche "AI tools" --cadence 3 --platforms youtube,instagram,x

# Write a production-ready script
python scripts/script_generator.py --topic "How AI is changing healthcare" \
    --length 10 --style faceless --visual-style "Cinematic Realism"

# Generate SEO package (titles, descriptions, tags)
python scripts/seo_optimizer.py --niche "AI tools" --titles "title1|title2|title3"

# Design thumbnail concepts with A/B variants
python scripts/thumbnail_designer.py --title "VIDEO TITLE" --style "Cinematic Realism" --niche "AI tools"

# Adapt a script for multiple platforms
python scripts/platform_adapter.py --master-script script.md \
    --platforms youtube_shorts,instagram,x,tiktok,facebook,linkedin

# Run the full pipeline end-to-end
python scripts/pipeline.py --niche "AI tools" --platforms youtube,instagram,tiktok,x \
    --budget 50 --cadence 3
```

---

## Install as Claude Code Skill

```bash
cp video-content-engine.skill ~/.claude/skills/
```

Then in Claude Code:

```
> Run the full ViralForge pipeline for my AI tools YouTube channel
> Generate a 90-day content calendar for fitness tech on TikTok and Instagram
> Write a script about "7 AI Tools That Replace Your Marketing Team"
```

---

## Supported Platforms

| Platform | Format | Optimal Length | Key Strategy |
|----------|--------|---------------|-------------|
| YouTube Long-Form | 16:9 | 8–15 min | Retention architecture + SEO |
| YouTube Shorts | 9:16 | 30–60 sec | Hook in 1 second, loop design |
| Instagram Reels | 9:16 | 15–30 sec | Visual-first, trending audio |
| TikTok | 9:16 | 15–60 sec | Trend-native, comment bait |
| X (Twitter) | 16:9 / 1:1 | 30–120 sec | Opinion-led, debate-generating |
| Facebook | 1:1 / 9:16 | 3–5 min | Emotional, shareable |
| LinkedIn | 16:9 / 1:1 | 1–3 min | Professional thought leadership |

---

## Reference Playbooks

The `references/` directory contains detailed methodology for each phase:

| File | Covers |
|------|--------|
| `niche-research.md` | 6-dimension scoring, competitor analysis, positioning formulas |
| `visual-brand.md` | 12 visual styles, JSON style guide schema, scene prompt library |
| `content-strategy.md` | Content pillars, 90-day calendar architecture, batch production |
| `seo-discovery.md` | YouTube SEO, 12 title formulas, Shorts-to-long-form funnel |
| `scriptwriting.md` | Retention layers, 6 hook types, pattern interrupts, script format |
| `production-pipeline.md` | 7-stage tool chain, SOPs, 3 cost tiers |
| `platform-ops.md` | Platform specs, adaptation matrix, posting schedules |
| `analytics-optimization.md` | KPIs, A/B testing, retention curves, monetization, scaling |

---

## Project Structure

```
ViralForge/
├── SKILL.md                          # Skill definition & phase router
├── MASTER-PLAYBOOK.md                # Sample generated playbook
├── references/
│   ├── niche-research.md             # Phase 1: Market intelligence
│   ├── visual-brand.md               # Phase 2: Brand identity system
│   ├── content-strategy.md           # Phase 3: Content architecture
│   ├── seo-discovery.md              # Phase 4: SEO & discovery
│   ├── scriptwriting.md              # Phase 5: Script engineering
│   ├── production-pipeline.md        # Phase 6: Production workflow
│   ├── platform-ops.md               # Phase 7: Platform operations
│   └── analytics-optimization.md     # Phase 8: Analytics & iteration
└── scripts/
    ├── niche_analyzer.py             # Niche scoring engine
    ├── content_calendar.py           # Calendar generator
    ├── script_generator.py           # Script builder
    ├── seo_optimizer.py              # SEO package generator
    ├── thumbnail_designer.py         # Thumbnail concept designer
    ├── platform_adapter.py           # Cross-platform adapter
    └── pipeline.py                   # Master orchestrator
```

---

## Cost Tiers

| Tier | Monthly Cost | Tools |
|------|-------------|-------|
| Bootstrap | $0 | DaVinci Resolve, Canva Free, OBS, Audacity |
| Creator | ~$50 | CapCut Pro, Canva Pro, basic AI tools |
| Professional | ~$150 | Adobe Suite, premium AI, stock libraries |

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-phase`)
3. Commit your changes
4. Push to the branch and open a Pull Request

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

Built by [TechKnowmad AI](https://techknowmad.ai)

</div>

