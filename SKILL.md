---
name: video-content-engine
description: "Autonomous end-to-end video content creation engine for social media platforms (YouTube, Instagram, Facebook/Meta, X/Twitter, TikTok, LinkedIn). Use this skill whenever the user mentions: video content creation, faceless YouTube channels, social media video strategy, content calendars for video, video scripts, YouTube SEO, thumbnail design, video production pipelines, AI video workflows, Shorts/Reels/TikTok content, viral video strategy, CPM optimization, faceless channels, video niche research, video batch production, or any task involving planning, scripting, producing, or optimizing video content for any social platform. Also trigger when user mentions creating a content brand, building a YouTube channel, video monetization strategy, or autonomous content pipelines. This skill handles everything from niche selection to published content with zero human intervention as the default protocol."
---

# Video Content Engine

Autonomous, enterprise-grade video content creation system. One-shot pipeline from idea to published, optimized content across all major platforms.

## Operating Philosophy

Every output from this skill is **production-ready and deployment-grade**. No placeholder content, no "fill in later" sections, no toy examples. Every script is shootable, every thumbnail concept is executable, every SEO package is paste-ready, every calendar is actionable.

**Zero human intervention** is the default. Every phase produces complete outputs that feed directly into the next phase. The user provides initial parameters (niche, interests, budget, goals) and receives a complete content operation.

---

## Phase Router

Identify what the user needs and read the corresponding reference file(s). Most requests fall into one of these phases. For full pipeline builds, execute phases sequentially â each phase's output feeds the next.

| Phase | What It Does | Reference File |
|-------|-------------|----------------|
| **1. Intelligence** | Niche selection, competitor analysis, market gaps, positioning | [niche-research.md](references/niche-research.md) |
| **2. Brand System** | Visual identity, style guides, art direction, thumbnail system | [visual-brand.md](references/visual-brand.md) |
| **3. Strategy** | Content calendars, series concepts, upload cadence, growth milestones | [content-strategy.md](references/content-strategy.md) |
| **4. SEO & Discovery** | Keywords, metadata, tags, descriptions, Shorts funnels, algorithm signals | [seo-discovery.md](references/seo-discovery.md) |
| **5. Scriptwriting** | Full production scripts with hooks, retention architecture, visual cues, CTAs | [scriptwriting.md](references/scriptwriting.md) |
| **6. Production** | Tool chains, asset generation, voiceover, music, editing, batch workflows | [production-pipeline.md](references/production-pipeline.md) |
| **7. Platform Ops** | Platform-specific optimization, cross-posting, format adaptation, scheduling | [platform-ops.md](references/platform-ops.md) |
| **8. Analytics** | Performance tracking, A/B frameworks, iteration loops, monetization optimization | [analytics-optimization.md](references/analytics-optimization.md) |

---

## Full Pipeline Execution

When the user wants the complete system (e.g., "build me a faceless YouTube channel" or "create a video content operation"), execute all 8 phases in sequence. Collect these parameters upfront:

```
REQUIRED INPUTS:
- niche_interests: [user's topic areas, passions, expertise]
- platforms: [youtube, instagram, facebook, x, tiktok, linkedin] (default: all)
- budget_monthly: [USD amount] (default: $0 â free tools only)
- upload_cadence: [videos per week] (default: 3)
- content_type: [faceless, talking_head, hybrid, shorts_only] (default: faceless)
- monetization_goal: [adsense, sponsorships, products, affiliate, all] (default: all)
- timeline: [days to first upload] (default: 7)
```

### Execution Order

1. **Read [niche-research.md](references/niche-research.md)** â Produce: niche scorecard, competitor map, positioning statement
2. **Read [visual-brand.md](references/visual-brand.md)** â Produce: visual style guide JSON, thumbnail system, brand kit
3. **Read [content-strategy.md](references/content-strategy.md)** â Produce: 90-day calendar, series concepts, milestone targets
4. **Read [seo-discovery.md](references/seo-discovery.md)** â Produce: keyword database, description templates, tag strategy
5. **Read [scriptwriting.md](references/scriptwriting.md)** â Produce: first 4 complete scripts with visual cues
6. **Read [production-pipeline.md](references/production-pipeline.md)** â Produce: tool chain spec, workflow SOP, cost breakdown
7. **Read [platform-ops.md](references/platform-ops.md)** â Produce: platform configs, cross-post strategy, scheduling plan
8. **Read [analytics-optimization.md](references/analytics-optimization.md)** â Produce: KPI dashboard spec, A/B testing framework, iteration SOP

### Output Packaging

Package all outputs into a structured deliverable:

```
content-engine-output/
âââ 01-intelligence/
â   âââ niche-scorecard.md
â   âââ competitor-analysis.md
â   âââ positioning.md
âââ 02-brand/
â   âââ visual-style-guide.json
â   âââ thumbnail-system.md
â   âââ brand-kit.md
âââ 03-strategy/
â   âââ content-calendar-90day.md
â   âââ series-concepts.md
â   âââ milestones.md
âââ 04-seo/
â   âââ keyword-database.md
â   âââ description-templates.md
â   âââ tag-strategy.md
âââ 05-scripts/
â   âââ script-001.md
â   âââ script-002.md
â   âââ script-003.md
â   âââ script-004.md
âââ 06-production/
â   âââ tool-chain.md
â   âââ workflow-sop.md
â   âââ cost-breakdown.md
âââ 07-platform-ops/
â   âââ platform-configs.md
â   âââ scheduling-plan.md
âââ 08-analytics/
â   âââ kpi-framework.md
â   âââ ab-testing-sop.md
âââ MASTER-PLAYBOOK.md (executive summary linking all phases)
```

---

## Script-Assisted Operations

Run these scripts for data-driven outputs. All scripts are in the `scripts/` directory.

```bash
# Generate niche scorecard with competitive analysis
python scripts/niche_analyzer.py --interests "topic1,topic2,topic3" --platforms youtube,instagram

# Generate 90-day content calendar
python scripts/content_calendar.py --niche "NICHE" --cadence 3 --platforms youtube,instagram,x

# Generate production-ready script with visual cues
python scripts/script_generator.py --topic "TOPIC" --length 10 --style faceless --visual-style "STYLE"

# Generate SEO package (title variants, descriptions, tags)
python scripts/seo_optimizer.py --niche "NICHE" --titles "title1|title2|title3"

# Adapt content for multiple platforms from a single master script
python scripts/platform_adapter.py --master-script script.md --platforms youtube,instagram,x,tiktok

# Generate thumbnail concepts
python scripts/thumbnail_designer.py --title "VIDEO TITLE" --style "VISUAL STYLE" --niche "NICHE"
```

---

## Quality Standards

Every output from this skill must meet these bars:

**Scripts**: Must include a measurable hook (question, stat, or pattern interrupt) in the first 8 seconds. Visual cue tags `[VISUAL]` at every scene break. Pattern interrupts every 60-90 seconds. Retention architecture (open loops, payoff structure). Single subscribe CTA placed at peak engagement moment (not beginning or end).

**Thumbnails**: Must follow the 3-element rule (face/object + text + background). High contrast. Readable at mobile scale (48x27px thumbnail preview). Emotional trigger in the primary element. Never more than 4 words of overlay text.

**SEO**: Every video gets a primary keyword, 3 secondary keywords, optimized description with timestamps, 15-20 tags mixing broad and long-tail, and a Shorts-to-long-form funnel path.

**Calendars**: Every entry includes title, thumbnail concept, script hook, target keyword, and estimated production time. No placeholder entries.

**Platform Adaptation**: Each platform version is natively optimized â not just cropped or truncated. Instagram gets vertical-first visual storytelling. X gets opinion-driven hooks with thread potential. TikTok gets trend-aware hooks with sound selection notes.

---

## Anti-Patterns (What This Skill Never Does)

- **Never produces generic "Top 10" lists** without a unique angle or contrarian take
- **Never writes scripts that read like blog posts** â every script is written for the ear, not the eye
- **Never suggests "just use Canva"** without specifying exact template types, dimensions, and design rules
- **Never creates SEO packages with keyword-stuffed descriptions** â descriptions read naturally while being algorithmically optimized
- **Never produces a content calendar with vague titles** like "Video about [topic]" â every title is click-ready
- **Never suggests upload schedules without production time estimates** â the calendar accounts for actual creation bandwidth
- **Never ignores platform-specific algorithm signals** â each platform has unique ranking factors and this skill respects them
- **Never writes hooks that start with "In this video"** â the hook must create an open loop or emotional trigger before any meta-framing
