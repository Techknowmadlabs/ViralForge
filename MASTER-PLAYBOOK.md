# ViralForge Master Playbook

> Executive summary linking all 8 phases of the Video Content Engine.

---

## Pipeline Overview

This playbook connects the complete ViralForge pipeline — from niche intelligence to published, optimized content across all major platforms.

### Phase 1: Intelligence
**File**: `references/niche-research.md`
**Produces**: Niche scorecard, competitor map, positioning statement
**Script**: `python scripts/niche_analyzer.py --interests "topic1,topic2" --platforms youtube,instagram`

### Phase 2: Brand System
**File**: `references/visual-brand.md`
**Produces**: Visual style guide JSON, thumbnail system, brand kit

### Phase 3: Strategy
**File**: `references/content-strategy.md`
**Produces**: 90-day content calendar, series concepts, milestone targets
**Script**: `python scripts/content_calendar.py --niche "NICHE" --cadence 3`

### Phase 4: SEO & Discovery
**File**: `references/seo-discovery.md`
**Produces**: Keyword database, description templates, tag strategy
**Script**: `python scripts/seo_optimizer.py --niche "NICHE" --titles "title1|title2"`

### Phase 5: Scriptwriting
**File**: `references/scriptwriting.md`
**Produces**: Production-ready scripts with hooks, retention architecture, visual cues
**Script**: `python scripts/script_generator.py --topic "TOPIC" --length 10 --style faceless`

### Phase 6: Production
**File**: `references/production-pipeline.md`
**Produces**: Tool chain spec, workflow SOPs, cost breakdown

### Phase 7: Platform Ops
**File**: `references/platform-ops.md`
**Produces**: Platform configs, cross-post strategy, scheduling plan
**Script**: `python scripts/platform_adapter.py --master-script script.md --platforms youtube_shorts,instagram,x,tiktok`

### Phase 8: Analytics
**File**: `references/analytics-optimization.md`
**Produces**: KPI dashboard spec, A/B testing framework, iteration SOP

---

## Quick Start

```bash
# 1. Analyze your niche
python scripts/niche_analyzer.py --interests "AI,productivity,automation" --platforms youtube,instagram,tiktok

# 2. Generate 90-day calendar
python scripts/content_calendar.py --niche "AI tools" --cadence 3 --platforms youtube,instagram,x

# 3. Write your first script
python scripts/script_generator.py --topic "7 AI Tools That Replace Your Marketing Team" --length 10 --style faceless --visual-style "Cinematic Realism"

# 4. Generate SEO package
python scripts/seo_optimizer.py --niche "AI tools" --titles "7 AI Tools That Replace Your Marketing Team"

# 5. Design thumbnails
python scripts/thumbnail_designer.py --title "7 AI Tools That Replace Your Marketing Team" --style "Cinematic Realism" --niche "AI tools"

# 6. Adapt for all platforms
python scripts/platform_adapter.py --master-script output/script-001.md --platforms youtube_shorts,instagram,x,tiktok,facebook,linkedin

# 7. Run the full pipeline
python scripts/pipeline.py --interests "AI,productivity" --niche "AI tools" --cadence 3
```

---

## Design Principles

1. **Zero human intervention** — every phase produces complete, deployment-ready outputs
2. **Platform-native** — each platform gets natively optimized content, not lazy crops
3. **Data-driven iteration** — analytics feed back into strategy via the OODA loop
4. **Production-grade** — no placeholders, no toy examples, no "fill in later"
5. **Compound growth** — each video builds the flywheel for the next
