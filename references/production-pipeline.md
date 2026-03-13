# Phase 6: Production Pipeline & Tool Chain

## Purpose

Define the exact tools, workflows, and automations needed to go from finished script to uploaded video with maximum efficiency and minimum cost. This phase produces a tool chain specification, step-by-step SOPs, batch production plans, and cost breakdowns.

---

## Tool Chain Architecture

The production pipeline has 7 stages. Each stage has a recommended primary tool (best quality), a free alternative, and an automation path.

### Stage 1: Script → Visual Asset Generation

| Tool | Tier | Cost | Best For |
|------|------|------|----------|
| **Midjourney v6+** | Premium | $30/mo | Highest quality, best for cinematic/artistic styles |
| **DALL-E 3** (via ChatGPT Plus) | Premium | $20/mo | Good for illustrations, consistent characters |
| **Flux Pro** (via Replicate/fal.ai) | Premium | Pay-per-image ~$0.05 | Best prompt adherence, good for batch generation |
| **Stable Diffusion** (local or cloud) | Free-Premium | Free-$20/mo | Most customizable, fine-tunable, unlimited generations |
| **Leonardo AI** | Free-Premium | Free-$24/mo | Good free tier, strong for stylized content |
| **Ideogram** | Free-Premium | Free-$20/mo | Best for text-in-images (thumbnails) |
| **Canva AI** | Free-Premium | Free-$15/mo | Quick thumbnails and simple graphics |

**Automation**: Batch generate all images for a video in one session. Use the visual style guide JSON (from Phase 2) as a prompt prefix for every generation.

### Stage 2: Script → Voiceover

| Tool | Tier | Cost | Best For |
|------|------|------|----------|
| **ElevenLabs** | Premium | $22/mo (100K chars) | Most natural, best for long-form, voice cloning |
| **Play.ht** | Premium | $31/mo | Good natural voices, API automation |
| **Murf AI** | Premium | $26/mo | Business-oriented voices |
| **Google Cloud TTS** | Free-Premium | Free tier generous | Solid quality, API-friendly, cost-effective at scale |
| **Azure Neural TTS** | Free-Premium | Free tier generous | Excellent quality, many languages |
| **Edge TTS** (edge-tts Python package) | Free | $0 | Surprising quality for free. Good for prototyping |
| **Tortoise TTS / XTTS** (local) | Free | $0 | Open source, voice cloning capable, needs GPU |

**Automation**: Feed the script's NARRATION sections directly into the TTS API. Parse visual cues as timing markers. Generate audio for the entire script in one API call or batch.

### Stage 3: Background Music & Sound Effects

| Tool | Tier | Cost | Best For |
|------|------|------|----------|
| **Epidemic Sound** | Premium | $15/mo | Largest library, YouTube-safe, mood search |
| **Artlist** | Premium | $17/mo | High quality, unlimited downloads |
| **Uppbeat** | Free-Premium | Free tier good | Free with attribution, clean search |
| **YouTube Audio Library** | Free | $0 | Built-in, guaranteed YouTube-safe |
| **Pixabay Music** | Free | $0 | CC0, no attribution required |
| **Suno AI / Udio** | Free-Premium | Free tier | AI-generated custom music for unique branding |
| **Freesound.org** | Free | $0 | Sound effects, CC licensed |

**Automation**: Create a music library organized by mood (energetic, calm, dramatic, mysterious, uplifting). Pre-assign music moods to content pillars so selection is instant.

### Stage 4: Video Assembly / Editing

| Tool | Tier | Cost | Best For |
|------|------|------|----------|
| **CapCut** (desktop) | Free | $0 | Best free editor, excellent auto-captions, templates |
| **DaVinci Resolve** | Free | $0 | Professional grade, color grading, effects |
| **Adobe Premiere Pro** | Premium | $23/mo | Industry standard, best plugin ecosystem |
| **RunwayML** | Premium | $15-76/mo | AI-powered editing, image-to-video, motion |
| **Pika** | Free-Premium | Free tier | Image-to-video, AI motion |
| **HeyGen** | Premium | $29/mo | AI avatar videos (if using virtual presenters) |
| **Descript** | Free-Premium | Free-$24/mo | Text-based editing, filler word removal |
| **FFmpeg** (CLI) | Free | $0 | Programmable batch processing, format conversion |

**Automation**: Create project templates in the editor with pre-configured:
- Aspect ratio presets for each platform
- Brand color overlays and lower thirds
- Intro/outro sequences
- Caption styles
- Music bed track structure

### Stage 5: Captions & Subtitles

| Tool | Tier | Cost | Best For |
|------|------|------|----------|
| **CapCut Auto Captions** | Free | $0 | Best free auto-captions with styled templates |
| **Descript** | Free-Premium | Free-$24/mo | Highly accurate, editable transcript |
| **Whisper** (OpenAI, local) | Free | $0 | Open source, highest accuracy, programmable |
| **Rev** | Premium | $1.50/min | Human-verified accuracy |
| **SubtitleEdit** | Free | $0 | Manual SRT editing |

**Automation**: Run Whisper on the generated voiceover to produce an SRT file. Use a script to style the SRT (word-by-word highlighting, custom fonts, positioning).

### Stage 6: Thumbnail Production

| Tool | Tier | Cost | Best For |
|------|------|------|----------|
| **Canva** | Free-Premium | Free-$15/mo | Fastest for template-based thumbnails |
| **Photoshop** | Premium | $23/mo | Most control, best compositing |
| **Figma** | Free | $0 | Template system, batch production |
| **GIMP** | Free | $0 | Open source Photoshop alternative |
| **AI Image Generator** + **Canva** | Varies | Varies | Generate background with AI, add text/overlays in Canva |

**Automation**: Build 3 thumbnail templates in Canva/Figma (one per variant from Phase 2). For each new video, generate the background image, drop it into the template, change the text.

### Stage 7: Upload & Scheduling

| Tool | Tier | Cost | Best For |
|------|------|------|----------|
| **YouTube Studio** | Free | $0 | Native, scheduling, analytics |
| **Meta Business Suite** | Free | $0 | Facebook + Instagram scheduling |
| **TweetDeck / X Pro** | Free-Premium | Free-$8/mo | X scheduling |
| **Buffer** | Free-Premium | Free-$6/mo/channel | Multi-platform scheduling |
| **Hootsuite** | Premium | $99/mo | Enterprise multi-platform |
| **Later** | Free-Premium | Free-$25/mo | Visual planning, Instagram-focused |
| **TubeBuddy** | Free-Premium | Free-$8/mo | YouTube SEO, A/B thumbnail testing |
| **VidIQ** | Free-Premium | Free-$8/mo | YouTube keyword research, competitor tracking |

---

## Production SOP: Idea to Upload

### Single Video SOP (Target: Under 3 Hours)

```
PHASE 1: PREP (30 minutes)
├── Open the content calendar entry for this video
├── Review the script (already written in Phase 5)
├── Verify the SEO package is complete (title, description, tags from Phase 4)
├── Confirm the visual style guide is loaded (from Phase 2)

PHASE 2: ASSET GENERATION (45 minutes)
├── Open AI image generator with style guide prefix loaded
├── Generate images for each [VISUAL] tag in the script (batch generate)
├── Generate thumbnail backgrounds (3 variants)
├── Queue voiceover generation (paste full narration into TTS tool)
├── Select background music from pre-organized library
├── Download/generate sound effects for pattern interrupts

PHASE 3: ASSEMBLY (60 minutes)
├── Import all assets into video editor
├── Place voiceover on timeline
├── Sync images to narration (match [VISUAL] tags to script timestamps)
├── Add music bed (volume: narration 100%, music 15-20%)
├── Add sound effects at pattern interrupt points
├── Add captions (auto-generate, then review)
├── Add intro/outro from template
├── Add subscribe CTA overlay at designated timestamp
├── Export in platform-specific formats

PHASE 4: THUMBNAIL (15 minutes)
├── Open thumbnail template
├── Insert AI-generated background
├── Add text overlay (from title formula)
├── Add face/reaction element (if applicable)
├── Export 3 variants for A/B testing

PHASE 5: UPLOAD & METADATA (15 minutes)
├── Upload to YouTube (schedule for optimal time)
├── Paste description from SEO template
├── Add tags from tag strategy
├── Set thumbnail
├── Add end screens (2 videos)
├── Add cards (at CTA timestamp and key moments)
├── Set chapters (from description timestamps)
├── Cross-post adapted versions to secondary platforms
├── Schedule companion Short
```

### Batch Production SOP (4-7 Videos in One Session)

```
SESSION DURATION: 5-7 hours

BATCH PREP (60 minutes):
├── Review all scripts for the batch
├── Create a master asset list (all [VISUAL] tags across all scripts)
├── Organize by similarity (batch similar image prompts together)

BATCH GENERATION (90 minutes):
├── Generate ALL images for ALL videos in one session
│   (similar prompts back-to-back for style consistency)
├── Generate ALL voiceovers in one session
│   (same voice settings, same session = consistent tone)
├── Select ALL music tracks (one per video)

BATCH ASSEMBLY (120-180 minutes):
├── Use editor templates — duplicate the template for each video
├── Assembly-line approach: place all voiceovers, then all images, then all music
├── Generate captions for all videos in one batch (Whisper CLI)

BATCH THUMBNAILS (30-45 minutes):
├── Generate all thumbnail backgrounds in one AI session
├── Apply to templates — change text for each video

BATCH UPLOAD (30-45 minutes):
├── Upload all to YouTube as unlisted/scheduled
├── Apply metadata to all
├── Schedule across the week at optimal times
├── Create all companion Shorts from hero moments
```

---

## Cost Breakdown Templates

### $0/month Budget (All Free Tools)

| Stage | Tool | Cost |
|-------|------|------|
| Images | Leonardo AI (free tier) or Stable Diffusion (local) | $0 |
| Voiceover | Edge TTS or Google Cloud TTS free tier | $0 |
| Music | YouTube Audio Library + Pixabay | $0 |
| Editing | CapCut Desktop or DaVinci Resolve | $0 |
| Captions | CapCut Auto Captions or Whisper (local) | $0 |
| Thumbnails | Canva Free + GIMP | $0 |
| Upload | YouTube Studio + Meta Business Suite | $0 |
| **TOTAL** | | **$0/month** |

### ~$50/month Budget (Best Value)

| Stage | Tool | Cost |
|-------|------|------|
| Images | Midjourney Basic | $10/mo |
| Voiceover | ElevenLabs Starter | $5/mo |
| Music | Uppbeat Free + YouTube Audio Library | $0 |
| Editing | CapCut Desktop | $0 |
| Captions | Whisper (local) | $0 |
| Thumbnails | Canva Pro | $15/mo |
| Upload + SEO | TubeBuddy Pro | $8/mo |
| Scheduling | Buffer Free | $0 |
| **TOTAL** | | **~$38/month** |

### ~$150/month Budget (Premium Quality)

| Stage | Tool | Cost |
|-------|------|------|
| Images | Midjourney Standard | $30/mo |
| Voiceover | ElevenLabs Creator | $22/mo |
| Music | Epidemic Sound | $15/mo |
| Editing | DaVinci Resolve (free) + RunwayML | $15/mo |
| Captions | Descript Pro | $24/mo |
| Thumbnails | Canva Pro | $15/mo |
| Upload + SEO | TubeBuddy Legend + VidIQ Pro | $16/mo |
| Scheduling | Buffer Essentials | $6/mo |
| **TOTAL** | | **~$143/month** |

---

## Automation Opportunities

For users with programming capability, these steps can be fully automated:

| Task | Automation Method | Time Saved |
|------|------------------|-----------|
| Image generation | API batch calls to Midjourney/DALL-E/Flux | 30 min/video |
| Voiceover generation | TTS API with script parser | 15 min/video |
| Caption generation | Whisper CLI pipeline | 10 min/video |
| Metadata writing | Template + variable substitution script | 10 min/video |
| Thumbnail background | API call to image generator | 5 min/video |
| Upload | YouTube Data API v3 | 10 min/video |
| Cross-platform posting | Buffer/Hootsuite API or custom scripts | 15 min/video |
| **Total per video** | | **~95 min saved** |

Python automation script structure is available in the `scripts/` directory.

---

## Phase 6 Deliverables Checklist

- [ ] Tool chain selected for user's budget tier
- [ ] Single-video SOP documented
- [ ] Batch production SOP documented
- [ ] Cost breakdown calculated with selected tools
- [ ] Editor templates created (aspect ratios, intros, outros, caption styles)
- [ ] Music library organized by mood
- [ ] Automation opportunities identified and prioritized
- [ ] First video produced end-to-end using the SOP (proof of concept)
