# Master Playbook

Executive summary linking all 8 phases of the ViralForge pipeline.

---

## Pipeline Overview

| Phase | Reference | Script | Produces |
|-------|-----------|--------|----------|
| 1. Intelligence | `references/niche-research.md` | `niche_analyzer.py` | Niche scorecard, competitor map, positioning statement |
| 2. Brand System | `references/visual-brand.md` | — | Visual style guide JSON, thumbnail system, brand kit |
| 3. Strategy | `references/content-strategy.md` | `content_calendar.py` | 90-day content calendar, series concepts, milestone targets |
| 4. SEO & Discovery | `references/seo-discovery.md` | `seo_optimizer.py` | Keyword database, description templates, tag strategy |
| 5. Scriptwriting | `references/scriptwriting.md` | `script_generator.py` | Production-ready scripts with hooks, retention architecture |
| 6. Production | `references/production-pipeline.md` | — | Tool chain spec, workflow SOPs, cost breakdown |
| 7. Platform Ops | `references/platform-ops.md` | `platform_adapter.py` | Platform configs, cross-post strategy, scheduling plan |
| 8. Analytics | `references/analytics-optimization.md` | — | KPI dashboard spec, A/B testing framework, iteration SOP |

---

## Quick Start

```bash
# 1. Analyze your niche
python scripts/niche_analyzer.py --interests "AI,productivity,automation" --platforms youtube,instagram,tiktok

# 2. Generate 90-day calendar
python scripts/content_calendar.py --niche "AI tools" --cadence 3 --platforms youtube,instagram,x

# 3. Write your first script
python scripts/script_generator.py --topic "7 AI Tools That Replace Your Marketing Team" \
    --length 10 --style faceless --visual-style "Cinematic Realism"

# 4. Generate SEO package
python scripts/seo_optimizer.py --niche "AI tools" --titles "7 AI Tools That Replace Your Marketing Team"

# 5. Design thumbnails
python scripts/thumbnail_designer.py --title "7 AI Tools That Replace Your Marketing Team" \
    --style "Cinematic Realism" --niche "AI tools"

# 6. Adapt for all platforms
python scripts/platform_adapter.py --master-script output/script-001.md \
    --platforms youtube_shorts,instagram,x,tiktok,facebook,linkedin

# 7. Run the full pipeline
python scripts/pipeline.py --interests "AI,productivity" --niche "AI tools" --cadence 3
```

---

## Design Principles

1. Each phase produces complete, ready-to-use outputs
2. Each platform gets natively optimized content, not resized crops
3. Analytics feed back into strategy through structured iteration loops
4. No placeholders — every output is usable as-is
5. Each video builds on the performance data of previous ones

