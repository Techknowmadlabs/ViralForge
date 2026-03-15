# ViralForge

End-to-end video content pipeline. Automates research, scriptwriting, SEO optimization, visual planning, and multi-platform distribution.

## Components

| Script | Function |
|--------|----------|
| `niche_analyzer.py` | Market research and niche viability scoring |
| `script_generator.py` | Video script generation with hooks and structure |
| `seo_optimizer.py` | Title, description, tag optimization for search |
| `thumbnail_designer.py` | Thumbnail concept generation and layout |
| `content_calendar.py` | Publishing schedule and content planning |
| `platform_adapter.py` | Multi-platform format adaptation (YouTube, TikTok, Shorts) |
| `pipeline.py` | Full pipeline orchestration |

## Usage

```bash
git clone https://github.com/TECHKNOWMAD-LABS/ViralForge.git
cd ViralForge

# Run the full pipeline
python scripts/pipeline.py --niche "your-niche" --platform youtube

# Run individual components
python scripts/niche_analyzer.py --query "topic"
python scripts/seo_optimizer.py --title "Your Video Title"
```

## Reference Documentation

The `references/` directory contains strategy guides:

- `niche-research.md` — Niche selection methodology
- `scriptwriting.md` — Script structure and hooks
- `seo-discovery.md` — SEO optimization techniques
- `content-strategy.md` — Content calendar planning
- `visual-brand.md` — Visual identity and thumbnails
- `analytics.md` — Performance tracking
- `platform-ops.md` — Platform-specific operations
- `production-pipeline.md` — Pipeline architecture

## Platform Support

ViralForge runs as a Claude Code skill and can be adapted for:
- Claude Code (native skill)
- MCP servers (via cortex cross-platform adapters)
- Standalone Python CLI
- CI/CD scheduled pipelines (GitHub Actions)

## Security

- Automated security scanning on every push (Bandit + secret detection)
- Dependabot monitoring for dependency vulnerabilities
- See [SECURITY.md](https://github.com/TECHKNOWMAD-LABS/.github/blob/main/SECURITY.md)

## License

MIT — see [LICENSE](LICENSE).