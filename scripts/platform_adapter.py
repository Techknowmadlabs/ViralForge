#!/usr/bin/env python3
"""
Platform Adapter — Transforms a master script into platform-native
content for YouTube Shorts, Instagram Reels, TikTok, X/Twitter,
Facebook, and LinkedIn.

Usage:
    python scripts/platform_adapter.py --master-script script.md \
        --platforms youtube_shorts,instagram,x,tiktok,facebook,linkedin
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


PLATFORM_SPECS = {
    "youtube_shorts": {
        "name": "YouTube Shorts",
        "resolution": "1080x1920 (9:16)",
        "max_length_sec": 180,
        "optimal_length_sec": "30-60",
        "format": "MP4, vertical",
        "captions": "Burned-in (platform adds its own)",
        "sound": "Critical — Shorts shelf is sound-on",
        "hook_time_sec": 1,
        "cta_style": "Subscribe overlay + pinned comment with long-form link",
        "content_strategy": "Extract the single most surprising moment from the master script",
        "loop_design": True,
        "text_on_screen": True,
    },
    "instagram": {
        "name": "Instagram Reels",
        "resolution": "1080x1920 (9:16)",
        "max_length_sec": 90,
        "optimal_length_sec": "15-30",
        "format": "MP4",
        "captions": "Burned-in text mandatory",
        "sound": "Trending audio significantly boosts reach",
        "hook_time_sec": 1,
        "cta_style": "'Save this' or 'Share with someone who needs this'",
        "content_strategy": "Visual-first storytelling with less narration, more on-screen text",
        "loop_design": True,
        "text_on_screen": True,
        "hashtags": "5-10, mix niche + trending",
        "cover_image": "Custom 1080x1920",
    },
    "tiktok": {
        "name": "TikTok",
        "resolution": "1080x1920 (9:16)",
        "max_length_sec": 600,
        "optimal_length_sec": "15-60",
        "format": "MP4, MOV",
        "captions": "On-screen text carrying the narrative",
        "sound": "Trending sounds boost discovery massively",
        "hook_time_sec": 0.5,
        "cta_style": "Comment-bait ending ('What would you do?')",
        "content_strategy": "Casual, native feel. Not overly produced. Trend-aware hooks.",
        "loop_design": True,
        "text_on_screen": True,
        "hashtags": "3-5, at least one trending",
        "stitch_duet": "Enable for engagement",
    },
    "x": {
        "name": "X (Twitter)",
        "resolution": "1920x1080 (16:9) or 1080x1080 (1:1)",
        "max_length_sec": 140,
        "optimal_length_sec": "30-120",
        "format": "MP4",
        "captions": "Optional but recommended",
        "sound": "Mixed — many watch muted in feed",
        "hook_time_sec": 2,
        "cta_style": "Provocative question or hot take in tweet text",
        "content_strategy": "Opinion-led, personality-forward, debate-generating",
        "loop_design": False,
        "text_on_screen": False,
        "thread": "2-3 follow-up tweets expanding the point",
    },
    "facebook": {
        "name": "Facebook",
        "resolution": "1080x1080 (1:1) for feed, 1080x1920 (9:16) for Reels",
        "max_length_sec": 14400,
        "optimal_length_sec": "180-300 (feed) or 15-60 (Reels)",
        "format": "MP4",
        "captions": "Essential — Facebook autoplay is muted",
        "sound": "Secondary — most watch muted",
        "hook_time_sec": 3,
        "cta_style": "'Tag someone who needs to see this' or 'Share with a friend'",
        "content_strategy": "Shareable, emotional hook, square format for feed engagement",
        "loop_design": False,
        "text_on_screen": True,
    },
    "linkedin": {
        "name": "LinkedIn",
        "resolution": "1920x1080 (16:9) or 1080x1080 (1:1)",
        "max_length_sec": 900,
        "optimal_length_sec": "60-180",
        "format": "MP4",
        "captions": "Recommended — many watch in offices without sound",
        "sound": "Secondary",
        "hook_time_sec": 3,
        "cta_style": "Professional CTA: 'What's your take?' or 'Thoughts?'",
        "content_strategy": "Professional framing, career relevance, thought leadership",
        "loop_design": False,
        "text_on_screen": False,
        "text_post": "Key takeaways as text post with video embedded",
    },
}

HOOK_ADAPTATIONS = {
    "youtube_shorts": "Shock + speed. No preamble. Hit the insight in 1 second.",
    "instagram": "Aesthetic + save-worthy. Visual hook with branded text overlay.",
    "tiktok": "Trend-native + debate. Use trending format or sound. Casual, authentic feel.",
    "x": "Opinion + provocation. Take a strong position. Make someone want to reply.",
    "facebook": "Emotional + shareable. Lead with a story or relatable moment.",
    "linkedin": "Professional + actionable. Business insight with career relevance.",
}


def parse_master_script(script_path: str) -> dict[str, Any]:
    """Parse a master script file and extract key components."""
    content = Path(script_path).read_text(encoding="utf-8")
    
    parsed = {
        "raw_content": content,
        "title": "",
        "sections": [],
        "visual_cues": [],
        "narration_blocks": [],
        "hooks": [],
        "pattern_interrupts": [],
        "cta": "",
        "total_word_count": 0,
    }
    
    # Extract title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        parsed["title"] = title_match.group(1).strip()
    
    # Extract sections
    section_pattern = r'^##\s+(.+?)(?=\n##|\Z)'
    sections = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    parsed["sections"] = sections
    
    # Extract visual cues
    visual_cues = re.findall(r'\[VISUAL:([^\]]+)\]', content)
    parsed["visual_cues"] = [v.strip() for v in visual_cues]
    
    # Extract narration blocks
    narration_blocks = re.findall(r'NARRATION:\s*\n"([^"]*)"', content, re.DOTALL)
    parsed["narration_blocks"] = [n.strip() for n in narration_blocks]
    
    # Word count
    words = re.findall(r'\b\w+\b', content)
    parsed["total_word_count"] = len(words)
    
    return parsed


def generate_platform_adaptation(
    master: dict[str, Any],
    platform: str,
    topic: str = "",
) -> str:
    """Generate a platform-specific script adaptation."""
    spec = PLATFORM_SPECS[platform]
    hook_style = HOOK_ADAPTATIONS[platform]
    title = master.get("title", topic) or topic
    
    lines = [
        f"# {spec['name']} Adaptation: {title}",
        "",
        f"**Platform**: {spec['name']}",
        f"**Resolution**: {spec['resolution']}",
        f"**Optimal Length**: {spec['optimal_length_sec']} seconds",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        "## Technical Requirements",
        "",
        f"- **Format**: {spec['format']}",
        f"- **Captions**: {spec['captions']}",
        f"- **Sound**: {spec['sound']}",
        f"- **Hook Window**: {spec['hook_time_sec']} second(s)",
        f"- **CTA Style**: {spec['cta_style']}",
    ]
    
    if spec.get("hashtags"):
        lines.append(f"- **Hashtags**: {spec['hashtags']}")
    if spec.get("thread"):
        lines.append(f"- **Thread**: {spec['thread']}")
    if spec.get("text_post"):
        lines.append(f"- **Text Post**: {spec['text_post']}")
    
    lines.extend([
        "",
        "---",
        "",
        "## Content Strategy",
        "",
        f"**Approach**: {spec['content_strategy']}",
        f"**Hook Adaptation**: {hook_style}",
        "",
        "---",
        "",
        "## Adapted Script",
        "",
    ])
    
    # Platform-specific script structure
    if platform in ("youtube_shorts", "instagram", "tiktok"):
        lines.extend([
            f"[VISUAL: Opening frame — MUST hook in {spec['hook_time_sec']} second(s). Vertical 9:16. Scroll-stopping.]",
        ])
        if spec["text_on_screen"]:
            lines.append("[TEXT ON SCREEN: Hook text — 5-7 words, bold, high contrast, centered]")
        if platform in ("instagram", "tiktok"):
            lines.append("[AUDIO: Trending sound — search for current trending sounds in this niche]")
        lines.extend([
            "",
            "NARRATION (15-20 seconds):",
            f'"[Extract the single most impactful insight from the master script. Deliver with maximum impact. No filler.]"',
            "",
            "[VISUAL: Proof/evidence — show the result, the data, or the dramatic moment]",
        ])
        if spec["text_on_screen"]:
            lines.append("[TEXT ON SCREEN: Key stat or result in large, bold text]")
        lines.extend([
            "",
            "NARRATION (10-15 seconds):",
            '"[The \'so what\' — why this matters to the viewer personally. One sentence.]"',
            "",
        ])
        if spec["loop_design"]:
            lines.extend([
                "[VISUAL: Loop point — visual connects back to opening frame]",
                "[TEXT ON SCREEN: CTA text]",
                "",
                "NARRATION (5-10 seconds):",
                '"[End with engagement trigger — question, challenge, or cliffhanger for rewatch]"',
            ])
        lines.extend([
            "",
            "---",
            "",
            "## Engagement Triggers",
            "",
        ])
        if platform == "youtube_shorts":
            lines.extend([
                "- **Pinned Comment**: Link to the full long-form video",
                "- **Loop Design**: End frame visually mirrors opening for seamless replay",
                "- **Subscribe Overlay**: Brief flash at peak moment",
            ])
        elif platform == "instagram":
            lines.extend([
                "- **Caption CTA**: 'Save this for later 📌' or 'Share with someone who needs this'",
                f"- **Hashtags**: [5-10 relevant hashtags mixing niche + trending]",
                "- **Cover Image**: Custom cover matching brand aesthetic",
                "- **Stories Cross-Promo**: Share to Stories with 'New Reel' sticker",
            ])
        elif platform == "tiktok":
            lines.extend([
                "- **Comment Bait**: End with 'What would you do?' or 'Am I wrong?'",
                f"- **Hashtags**: [3-5 hashtags, at least one trending]",
                "- **Stitch/Duet**: Enabled for user-generated engagement",
                "- **Reply Videos**: Plan to reply to top comments with follow-up content",
            ])
    
    elif platform == "x":
        lines.extend([
            "### Tweet Text (This is as important as the video)",
            "",
            f'"[PROVOCATIVE STATEMENT or QUESTION about {title}. Take a strong position. Make someone want to reply — agree or disagree.]"',
            "",
            "### Video (30-120 seconds)",
            "",
            "[VISUAL: Opinion-driven, personality-forward, raw/authentic feel. 16:9 or 1:1.]",
            "",
            "NARRATION:",
            '"[Strong opinion about the topic. Back it with one data point or example. End with a question that invites debate.]"',
            "",
            "### Thread (2-3 follow-up tweets)",
            "",
            "**Tweet 2**: [Expand on the video's core argument with additional evidence]",
            "**Tweet 3**: [Present the counter-argument, then refute it]",
            "**Tweet 4**: [Call to action — link to full video or ask for engagement]",
            "",
            "---",
            "",
            "## Engagement Strategy",
            "",
            "- **Quote Tweet**: Encourage viewers to quote tweet with their take",
            "- **Reply**: Engage with every reply in the first 30 minutes",
            "- **Timing**: Post at 8-10 AM or 12-1 PM in target timezone",
        ])
    
    elif platform == "facebook":
        lines.extend([
            "### Post Text (Keep under 200 characters for full display)",
            "",
            f'"[EMOTIONAL HOOK about {title}. Lead with a relatable story or surprising fact. End with \'Tag someone who needs to see this.\']"',
            "",
            "### Video (3-5 minutes, square 1:1 for feed)",
            "",
            "[VISUAL: Condensed version of master script. Square format. Captions burned in — most watch muted.]",
            "",
            "NARRATION:",
            '"[Emotionally-driven condensation of the master script. Lead with the human story, then the information. Facebook audiences respond to emotion over pure information.]"',
            "",
            "[TEXT ON SCREEN: Key points as readable text throughout — assume no audio]",
            "",
            "---",
            "",
            "## Distribution",
            "",
            "- **Groups**: Cross-post to 3-5 relevant Facebook groups with unique captions per group",
            "- **Timing**: Post at 1-4 PM on Wed/Thu/Fri",
            "- **Boost**: Consider $5-10 boost on high-performing videos to reach new audiences",
        ])
    
    elif platform == "linkedin":
        lines.extend([
            "### Text Post (Published alongside the video)",
            "",
            "```",
            f"[PROFESSIONAL INSIGHT HOOK about {title}]",
            "",
            "Here's what I've learned:",
            "",
            "→ [Key takeaway 1]",
            "→ [Key takeaway 2]",
            "→ [Key takeaway 3]",
            "",
            "The bottom line: [One-sentence conclusion with career/business relevance]",
            "",
            "What's your experience with this? I'd love to hear your perspective.",
            "",
            "#[ProfessionalHashtag1] #[ProfessionalHashtag2] #[ProfessionalHashtag3]",
            "```",
            "",
            "### Video (1-3 minutes, 16:9 or 1:1)",
            "",
            "[VISUAL: Professional, clean, authoritative. Thought leadership framing.]",
            "",
            "NARRATION:",
            '"[Professional reframing of the master script\'s core insight. Focus on career impact, business implications, and actionable advice. Tone: authoritative but approachable.]"',
            "",
            "---",
            "",
            "## LinkedIn Strategy",
            "",
            "- **Engagement**: Reply to every comment — LinkedIn algorithm rewards conversation",
            "- **Timing**: Post at 7-8 AM or 12 PM Tue/Wed/Thu",
            "- **Tag**: Tag 2-3 relevant connections or companies for reach",
            "- **Repurpose**: Extract quote cards for LinkedIn carousel posts",
        ])
    
    # Production notes
    lines.extend([
        "",
        "---",
        "",
        "## Production Notes",
        "",
        f"- **Source**: Adapted from master script for '{title}'",
        f"- **Resolution**: {spec['resolution']}",
        f"- **Captions Required**: {'Yes — burned in' if spec['text_on_screen'] else 'Recommended'}",
        f"- **Sound Strategy**: {spec['sound']}",
        "- **Export Settings**: [Match platform specs above]",
        "",
        "*This adaptation is designed to be platform-native — not a lazy crop/trim of the YouTube version.*",
    ])
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Platform Adapter")
    parser.add_argument("--master-script", required=True, help="Path to master script markdown file")
    parser.add_argument("--platforms", default="youtube_shorts,instagram,x,tiktok",
                       help="Platforms to adapt for (comma-separated)")
    parser.add_argument("--topic", default="", help="Video topic (if not parseable from script)")
    parser.add_argument("--output-dir", default=None, help="Output directory for adapted scripts")
    
    args = parser.parse_args()
    platforms = [p.strip() for p in args.platforms.split(",")]
    
    # Parse master script
    master = parse_master_script(args.master_script)
    topic = args.topic or master.get("title", "Untitled")
    
    for platform in platforms:
        if platform not in PLATFORM_SPECS:
            print(f"WARNING: Unknown platform '{platform}'. Skipping.", file=sys.stderr)
            continue
        
        adaptation = generate_platform_adaptation(master, platform, topic)
        
        if args.output_dir:
            output_path = Path(args.output_dir) / f"{platform}_adaptation.md"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(adaptation, encoding="utf-8")
            print(f"  → {output_path}", file=sys.stderr)
        else:
            print(adaptation)
            print("\n" + "=" * 80 + "\n")
    
    if args.output_dir:
        print(f"\nAll adaptations written to {args.output_dir}/", file=sys.stderr)


if __name__ == "__main__":
    main()
