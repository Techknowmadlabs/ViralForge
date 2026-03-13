# Phase 2: Visual Brand System & Art Direction

## Purpose

Build a complete, reusable visual identity system that ensures every piece of content is immediately recognizable as belonging to the brand. This phase produces a machine-readable style guide (JSON), thumbnail design system, and art direction playbook.

---

## Visual Style Selection

The visual style must match the niche's audience expectations while standing out from competitors. Use the competitor analysis from Phase 1 to identify visual gaps.

### Style Categories for AI-Generated Content

| Style | Best For | AI Tools | Example Niches |
|-------|----------|----------|----------------|
| **Cinematic Realism** | Authority, premium feel | Midjourney v6+, Flux Pro, DALL-E 3 | Finance, technology, science |
| **2D Animation / Motion Graphics** | Explanations, processes | RunwayML, Pika, SVG animation | Education, how-to, business |
| **Isometric Illustration** | Systems, comparisons, tech | Midjourney, custom prompts | Tech, productivity, SaaS |
| **Dramatic Dark Mode** | Mystery, intrigue, horror | Midjourney dark aesthetic | True crime, conspiracy, space |
| **Watercolor / Soft Illustration** | Calm, wellness, lifestyle | DALL-E 3, Stable Diffusion | Health, meditation, cooking |
| **Retro / Vintage** | Nostalgia, history, culture | Midjourney vintage prompts | History, pop culture, music |
| **Flat Design / Infographic** | Data, statistics, lists | Canva + AI, custom SVG | News, data journalism, finance |
| **Pixel Art / 8-bit** | Gaming, tech nostalgia | Pixel-specific models | Gaming, retro tech, coding |
| **Anime / Manga** | Storytelling, entertainment | Stable Diffusion anime models | Stories, mythology, entertainment |
| **Photojournalistic** | Real events, documentary | Stock + AI enhancement | Current events, documentary |
| **3D Rendered** | Products, architecture, sci-fi | Blender + AI, 3D model generators | Tech reviews, architecture, sci-fi |
| **Collage / Mixed Media** | Creative, avant-garde | Photoshop + AI compositing | Art, culture, fashion |

### Style Decision Framework

Ask these questions to select the right style:

1. **What emotion should viewers feel?** → Maps to color palette and atmosphere
2. **What's the information density?** → High density = cleaner styles (flat, isometric). Low density = richer styles (cinematic, watercolor)
3. **What's the production budget?** → $0 budget = styles achievable with free-tier AI tools
4. **What do competitors NOT do?** → Choose the visual gap from Phase 1 analysis
5. **What's the reusability?** → Styles with strong prompt consistency (isometric, flat) scale better than styles requiring manual iteration (cinematic, collage)

---

## Visual Style Guide (JSON Format)

Produce this JSON structure — it's designed to be directly pasteable into AI image generation tools, and serves as the single source of truth for all visual assets.

```json
{
  "brand_identity": {
    "channel_name": "",
    "niche": "",
    "positioning": "",
    "visual_personality": ["3-5 adjective descriptors"]
  },
  "art_style": {
    "primary_style": "",
    "style_prompt_prefix": "A detailed prompt prefix that goes before every image generation prompt to ensure consistency",
    "style_prompt_suffix": "Quality and rendering directives that go after every prompt",
    "negative_prompt": "Elements to explicitly exclude from all generations",
    "reference_artists_or_movements": ["For style inspiration, not copying"],
    "rendering_quality": "8K, cinematic, photorealistic, etc.",
    "aspect_ratios": {
      "youtube_thumbnail": "16:9",
      "youtube_video": "16:9",
      "instagram_reel": "9:16",
      "instagram_post": "1:1",
      "tiktok": "9:16",
      "x_video": "16:9",
      "facebook_video": "16:9"
    }
  },
  "color_palette": {
    "primary": {"hex": "", "usage": "60% of visual weight — backgrounds, large areas"},
    "secondary": {"hex": "", "usage": "25% — supporting elements, cards, overlays"},
    "accent": {"hex": "", "usage": "10% — CTAs, highlights, key data points"},
    "text_primary": {"hex": "", "usage": "Headlines, body text"},
    "text_secondary": {"hex": "", "usage": "Captions, supporting text"},
    "background_dark": {"hex": "", "usage": "Dark mode backgrounds"},
    "background_light": {"hex": "", "usage": "Light mode backgrounds"},
    "alert_or_emphasis": {"hex": "", "usage": "5% — warnings, critical highlights"}
  },
  "typography": {
    "headline_font": "",
    "body_font": "",
    "accent_font": "",
    "headline_size_range": "48-72pt",
    "body_size_range": "16-24pt",
    "caption_size_range": "12-14pt",
    "text_overlay_rules": {
      "max_words": 4,
      "stroke_or_shadow": true,
      "placement": "lower-third or rule-of-thirds intersection",
      "background_treatment": "semi-transparent dark bar, blur, or gradient fade"
    }
  },
  "character_design": {
    "has_recurring_character": false,
    "character_description": "",
    "character_prompt": "",
    "character_expressions": [],
    "character_consistency_rules": "Describe exactly how to maintain character consistency across generations"
  },
  "scene_composition": {
    "camera_angles": ["Describe 3-5 default camera angles"],
    "lighting_setup": "Describe the default lighting mood",
    "depth_of_field": "",
    "background_treatment": "",
    "foreground_elements": "",
    "border_or_frame_style": ""
  },
  "motion_design": {
    "transition_style": "",
    "text_animation": "",
    "zoom_behavior": "Ken Burns, static, dynamic push-in, etc.",
    "pacing": "Cuts per minute, hold duration for key visuals"
  },
  "thumbnail_system": {
    "layout_formula": "Describe the consistent thumbnail layout",
    "text_placement": "",
    "face_or_object_placement": "",
    "background_treatment": "",
    "color_override_rules": "When to deviate from brand colors for CTR",
    "emotion_triggers": ["curiosity", "shock", "desire", "fear", "satisfaction"],
    "a_b_test_variants": "Describe 2-3 thumbnail variant approaches to test"
  }
}
```

---

## Scene Prompt Library

Create 15-20 reusable scene prompts that cover common visual needs. These are the building blocks — they get customized per video but maintain brand consistency.

### Scene Prompt Template

```
[STYLE PREFIX from style guide]
[SCENE DESCRIPTION: specific, detailed, actionable]
[MOOD/ATMOSPHERE: lighting, time of day, weather, emotion]
[COMPOSITION: camera angle, framing, depth]
[COLOR DIRECTION: reference brand palette]
[STYLE SUFFIX from style guide]
--no [NEGATIVE PROMPT from style guide]
```

### Required Scene Categories

Every brand needs prompts in these categories:

1. **Hero/Title Card** — The opening visual or thumbnail background
2. **Explanation Scene** — Visual for when narration explains a concept
3. **Comparison Scene** — Side-by-side or before/after visuals
4. **Data/Statistic Scene** — Background for when presenting numbers
5. **Transition Scene** — Visual bridge between topics
6. **Emotional Peak** — The most dramatic or impactful visual
7. **Call-to-Action Scene** — Subscribe/follow prompt background
8. **B-Roll Atmospheric** — Mood-setting establishing shots
9. **Close-Up Detail** — For emphasis or dramatic effect
10. **Wide Establishing** — Context-setting wide shots
11. **Character/Person Scene** — If using recurring characters
12. **Technology/Interface** — For tech or digital topics
13. **Nature/Environment** — For wellness, science, geography topics
14. **Historical/Vintage** — For retrospective content
15. **Future/Conceptual** — For forward-looking content

---

## Thumbnail Design System

Thumbnails drive 80% of click-through rate. This system ensures every thumbnail is engineered for clicks, not just aesthetically pleasant.

### The 3-Element Thumbnail Formula

Every thumbnail contains exactly 3 elements:

1. **Primary Subject** (50-60% of frame) — A face showing strong emotion, or a dramatic object/scene
2. **Text Overlay** (20-30% of frame) — 2-4 words maximum, high contrast, readable at 48px height
3. **Background/Context** (remaining) — Sets the mood, provides contrast, frames the subject

### Thumbnail Psychology Rules

- **Faces with extreme emotions outperform everything** — If using faces, they must show genuine emotion (shock, joy, anger, curiosity), not neutral expressions
- **High contrast is non-negotiable** — The thumbnail must be legible and attention-grabbing at 168x94px (the smallest YouTube renders it)
- **Color theory for CTR**: Red/orange = urgency/energy. Blue/green = trust/calm. Yellow = curiosity/warning. Purple = luxury/mystery. Use colors that contrast with YouTube's white/gray UI
- **Implied motion** — Arrows, blur trails, or dynamic composition that suggests movement
- **Information gap** — The thumbnail should raise a question that only watching answers. Never give away the punchline

### Thumbnail Variants for A/B Testing

For every video, produce 3 thumbnail concepts:

| Variant | Strategy | When It Wins |
|---------|----------|-------------|
| **A: Emotion-Led** | Face/reaction + minimal text | When the topic has a strong emotional hook |
| **B: Curiosity-Led** | Provocative image + question text | When the topic reveals something surprising |
| **C: Value-Led** | Clear benefit statement + supporting visual | When the audience is solution-seeking |

---

## Brand Consistency Enforcement

### The 5-Second Recognition Test

If a viewer scrolls past 10 videos on a feed, they should recognize the brand's video within 5 seconds by visual style alone — before reading any text.

### Consistency Checklist (Apply to Every Asset)

- [ ] Color palette matches the style guide (within 10% variance)
- [ ] Typography follows the font pairing rules
- [ ] Art style matches the primary style prompt
- [ ] Thumbnail follows the 3-element formula
- [ ] Motion/transition style is consistent
- [ ] No stylistic elements borrowed from a competitor
- [ ] Visual density matches the niche's audience expectations

### Permitted Deviations

- **Seasonal content** may use holiday-specific accent colors while maintaining primary palette
- **Collaboration content** may blend brand styles but the home brand's style should dominate (60%+)
- **Trend-riding content** (especially TikTok/Reels) may relax style rules for native platform feel — but thumbnails and long-form content stay on-brand

---

## Phase 2 Deliverables Checklist

- [ ] Visual style selected with rationale
- [ ] Complete JSON style guide produced (all fields populated)
- [ ] 15-20 reusable scene prompts written
- [ ] Thumbnail design system documented with 3 variant approaches
- [ ] Brand consistency checklist finalized
- [ ] Style guide tested: generate 3 sample images using the prompts and verify consistency
