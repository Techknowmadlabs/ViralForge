---
name: video-content-engine
description: "End-to-end video content creation engine for social media platforms (YouTube, Instagram, Facebook/Meta, X/Twitter, TikTok, LinkedIn). Trigger on: video content creation, faceless YouTube channels, social media video strategy, content calendars, video scripts, YouTube SEO, thumbnail design, video production pipelines, Shorts/Reels/TikTok content, CPM optimization, niche research, batch production, or any task involving planning, scripting, producing, or optimizing video content. Also trigger on: building a YouTube channel, video monetization strategy, content brand creation."
---

# Video Content Engine

End-to-end video content creation system. Produces complete, ready-to-use outputs from initial parameters through published, platform-optimized content.

## Operating Principles

All outputs are production-ready. No placeholders, no incomplete sections. Scripts are shootable, thumbnail concepts are executable, SEO packages are paste-ready, calendars are actionable.

Each phase produces complete outputs that feed directly into the next. The user provides initial parameters (niche, interests, budget, goals) and receives a complete content operation.

---

## Phase Router

Identify what the user needs and read the corresponding reference file(s). For full pipeline builds, execute phases sequentially.

| Phase | What It Does | Reference File |
|-------|-------------|----------------|
| **1. Intelligence** | Niche selection, competitor analysis, market gaps, positioning | [niche-research.md](references/niche-research.md) |
| **2. Brand System** | Visual identity, style guides, art direction, thumbnail system | [visual-brand.md](references/visual-brand.md) |
| **3. Strategy** | Content calendars, series concepts, upload cadence, growth milestones | [content-strategy.md](references/content-strategy.md) |
| **4. SEO & Discovery** | Keywords, metadata, tags, descriptions, Shorts funnels, algorithm signals | [seo-discovery.md](references/seo-discovery.md) |
| **5. Scriptwriting** | Production scripts with hooks, retention architecture, visual cues, CTAs | [scriptwriting.md](references/scriptwriting.md) |
| **6. Production** | Tool chains, asset generation, voiceover, music, editing, batch workflows | [production-pipeline.md](references/production-pipeline.md) |
| **7. Platform Ops** | Platform-specific optimization, cross-posting, format adaptation, scheduling | [platform-ops.md](references/platform-ops.md) |
| **8. Analytics** | Performance tracking, A/B frameworks, iteration loops, monetization | [analytics-optimization.md](references/analytics-optimization.md) |

---

## Full Pipeline Execution

When the user wants the complete system (e.g., "build me a faceless YouTube channel" or "create a video content operation"), execute all 8 phases in sequence. Collect these parameters upfront:

```
REQUIRED INPUTS:
- niche_interests: [user's topic areas, expertise]
- platforms: [youtube, instagram, facebook, x, tiktok, linkedin] (default: all)
- budget_monthly: [USD amount] (default: $0 — free tools only)
- upload_cadence: [videos per week] (default: 3)
- content_type: [faceless, talking_head, hybrid, shorts_only] (default: faceless)
- monetization_goal: [adsense, sponsorships, products, affiliate, all] (default: all)
- timeline: [days to first upload] (default: 7)
```

### Execution Order

1. **Read [niche-research.md](references/niche-research.md)** → Produce: niche scorecard, competitor map, positioning statement
2. **Read [visual-brand.md](references/visual-brand.md)** → Produce: visual style guide JSON, thumbnail system, brand kit
3. **Read [content-strategy.md](references/content-strategy.md)** → Produce: 90-day calendar, series concepts, milestone targets
4. **Read [seo-discovery.md](references/seo-discovery.md)** → Produce: keyword database, description templates, tag strategy
5. **Read [scriptwriting.md](references/scriptwriting.md)** → Produce: first 4 complete scripts with visual cues
6. **Read [production-pipeline.md](references/production-pipeline.md)** → Produce: tool chain spec, workflow SOP, cost breakdown
7. **Read [platform-ops.md](references/platform-ops.md)** → Produce: platform configs, cross-post strategy, scheduling plan
8. **Read [analytics-optimization.md](references/analytics-optimization.md)** → Produce: KPI dashboard spec, A/B testing framework, iteration SOP

### Output Packaging

Package all outputs into a structured deliverable:

```
content-engine-output/
├── 01-intelligence/
│   ├── niche-scorecard.md
│   ├── competitor-analysis.md
│   └── positioning.md
├── 02-brand/
│   ├── visual-style-guide.json
│   ├── thumbnail-system.md
│   └── brand-kit.md
├── 03-strategy/
│   ├── content-calendar-90day.md
│   ├── series-concepts.md
│   └── milestones.md
├── 04-seo/
│   ├── keyword-database.md
│   ├── description-templates.md
│   └── tag-strategy.md
├── 05-scripts/
│   ├── script-001.md
│   ├── script-002.md
│   ├── script-003.md
│   └── script-004.md
├── 06-production/
│   ├── tool-chain.md
│   ├── workflow-sop.md
│   └── cost-breakdown.md
├── 07-platform-ops/
│   ├── platform-configs.md
│   └── scheduling-plan.md
├── 08-analytics/
│   ├── kpi-framework.md
│   └── ab-testing-sop.md
└── MASTER-PLAYBOOK.md
```

---

## Script-Assisted Operations

All scripts are in the `scripts/` directory, use Python 3.10+ stdlib only.

```bash
# Score and rank niches
python scripts/niche_analyzer.py --interests "topic1,topic2,topic3" --platforms youtube,instagram

# Generate 90-day content calendar
python scripts/content_calendar.py --niche "NICHE" --cadence 3 --platforms youtube,instagram,x

# Write a production-ready script
python scripts/script_generator.py --topic "TOPIC" --length 10 --style faceless --visual-style "STYLE"

# Generate SEO package
python scripts/seo_optimizer.py --niche "NICHE" --titles "title1|title2|title3"

# Adapt for multiple platforms
python scripts/platform_adapter.py --master-script script.md --platforms youtube,instagram,x,tiktok

# Design thumbnail concepts
python scripts/thumbnail_designer.py --title "VIDEO TITLE" --style "VISUAL STYLE" --niche "NICHE"
```

---

## Quality Standards

**Scripts**: Hook (question, stat, or pattern interrupt) within the first 8 seconds. `[VISUAL]` tags at every scene break. Pattern interrupts every 60–90 seconds. Retention architecture with open loops and payoff structure. Subscribe CTA at peak engagement (not opening or closing).

**Thumbnails**: 3-element rule (face/object + text + background). High contrast. Readable at mobile scale (48×27px preview). No more than 4 words of overlay text.

**SEO**: Primary keyword, 3 secondary keywords, optimized description with timestamps, 15–20 tags (broad + long-tail), Shorts-to-long-form funnel path.

**Calendars**: Every entry includes title, thumbnail concept, script hook, target keyword, and production time estimate. No placeholder entries.

**Platform Adaptation**: Each platform version is natively optimized, not cropped or truncated. Instagram gets vertical-first visual storytelling. X gets opinion-driven hooks with thread potential. TikTok gets trend-aware hooks with sound selection notes.

---

## Anti-Patterns

This skill does not:

- Produce generic "Top 10" lists without a unique angle
- Write scripts that read like blog posts — scripts are written for spoken delivery
- Suggest tools without specifying exact template types, dimensions, and design rules
- Create keyword-stuffed descriptions — descriptions read naturally while remaining algorithmically effective
- Produce calendars with vague titles like "Video about [topic]" — every title is ready to publish
- Suggest upload schedules without production time estimates
- Ignore platform-specific algorithm signals
- Write hooks that start with "In this video" — hooks create an open loop or tension before any framing

