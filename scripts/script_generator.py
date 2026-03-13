#!/usr/bin/env python3
"""
Script Generator — Produces production-ready video scripts with retention
architecture, visual cues, pattern interrupts, and platform-specific formatting.

Usage:
    python scripts/script_generator.py --topic "How AI is changing healthcare" \
        --length 10 --style faceless --visual-style "Cinematic Realism"
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


HOOK_TEMPLATES = {
    "shocking_stat": '[VISUAL: {visual_desc}]\n[AUDIO: Dramatic ambient music, low energy building]\n\nNARRATION:\n"{stat} — and {implication}."',
    "contrarian": '[VISUAL: {visual_desc}]\n[AUDIO: Tense, expectation-subverting tone]\n\nNARRATION:\n"Everything you\'ve been told about {topic} is wrong. Here\'s what {authority} actually shows."',
    "story_open": '[VISUAL: {visual_desc}]\n[AUDIO: Cinematic, narrative pulse]\n\nNARRATION:\n"{time_marker}, {vivid_scene} — and {unexpected_twist}."',
    "direct_challenge": '[VISUAL: {visual_desc}]\n[AUDIO: Confident, direct energy]\n\nNARRATION:\n"If you {common_behavior}, you\'re {negative_consequence} — and I can prove it in the next {length} minutes."',
    "result_reveal": '[VISUAL: {visual_desc}]\n[AUDIO: Building anticipation]\n\nNARRATION:\n"I {action} and {result}. Here\'s exactly how."',
    "curiosity_gap": '[VISUAL: {visual_desc}]\n[AUDIO: Mystery, intrigue]\n\nNARRATION:\n"There\'s a {thing} that {impressive_claim}, but {surprising_detail}."',
}

PATTERN_INTERRUPT_TYPES = [
    {"type": "visual_shift", "tag": "[VISUAL: SHIFT — dramatic change in visual style or perspective]", "narration": ""},
    {"type": "direct_address", "tag": "[VISUAL: ZOOM — tight frame, direct eye contact feel]", "narration": "Now, I know what you\'re thinking..."},
    {"type": "sound_design", "tag": "[AUDIO: SFX — dramatic sting / record scratch / whoosh]", "narration": ""},
    {"type": "counter_graphic", "tag": "[VISUAL: GRAPHIC — animated counter / data visualization appearing]", "narration": ""},
    {"type": "mini_story", "tag": "[VISUAL: Scene change — illustrative example]", "narration": "Let me give you a real example of this..."},
    {"type": "prediction_prompt", "tag": "[VISUAL: GRAPHIC — question mark or blank space for viewer to fill]", "narration": "Before I tell you the answer, take a guess."},
    {"type": "humor", "tag": "[VISUAL: Comedic visual or meme-style reference]", "narration": ""},
    {"type": "zoom_scale", "tag": "[VISUAL: ZOOM — dramatic push-in or pull-out]", "narration": ""},
]


def generate_script_template(
    topic: str,
    length_minutes: int,
    visual_style: str,
    content_type: str = "faceless",
    platform: str = "youtube",
) -> str:
    """Generate a production-ready script template."""
    
    words_target = length_minutes * 155
    num_segments = max(2, (length_minutes - 3) // 2)  # 2 min for hook+setup, 1 min for close
    segment_duration = (length_minutes - 3) / num_segments
    num_pattern_interrupts = max(2, length_minutes // 1.5)
    
    # Calculate CTA placement (70-80% mark)
    cta_timestamp_minutes = int(length_minutes * 0.75)
    
    lines = [
        f"# {topic.upper()}",
        "",
        f"**Target Length**: {length_minutes} minutes (~{words_target} words)",
        f"**Platform**: {platform.title()}",
        f"**Visual Style**: {visual_style}",
        f"**Content Type**: {content_type.title()}",
        f"**Target Keyword**: [PRIMARY SEO KEYWORD — from Phase 4 SEO research]",
        f"**Thumbnail Concept**: [THUMBNAIL DESCRIPTION — from Phase 2 thumbnail system]",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        "## HOOK (0:00 - 0:30)",
        "",
        f"[VISUAL: Opening establishing shot — {visual_style} style. Dramatic, attention-grabbing composition that immediately communicates the topic's stakes]",
        "[AUDIO: Background music — building tension, moderate energy]",
        "",
        "NARRATION:",
        f'"[WRITE HOOK — Choose from hook types: Shocking Stat / Contrarian / Story Open / Direct Challenge / Result Reveal / Curiosity Gap. The hook must create an open loop that the video resolves. Maximum 3 sentences. Every word must earn its place.]"',
        "",
        f"[VISUAL: Second hook visual — show the consequence or the promise. {visual_style} style]",
        "",
        "---",
        "",
        "## SETUP (0:30 - 2:00)",
        "",
        f"[VISUAL: Establishing context visual — wider frame, setting the scene. {visual_style}]",
        "[MUSIC: Shift to informational energy — calm but forward-moving]",
        "",
        "NARRATION:",
        '"[SETUP NARRATION — 4-6 sentences that:',
        "  1. Provide context for the topic",
        "  2. Explain WHY this matters to the viewer personally",
        "  3. Preview the value: 'By the end of this video, you'll know exactly how to [specific outcome]'",
        "  4. Use 'you' and 'your' at least twice",
        '  5. Keep sentences short — 8-12 words average]"',
        "",
        f"[VISUAL: Supporting visual — data point, illustration, or example. {visual_style}]",
        "",
        "---",
    ]
    
    # Generate segments
    current_time = 2.0
    for seg_num in range(1, num_segments + 1):
        end_time = current_time + segment_duration
        
        # Format timestamps
        start_ts = f"{int(current_time)}:{int((current_time % 1) * 60):02d}"
        end_ts = f"{int(end_time)}:{int((end_time % 1) * 60):02d}"
        
        # Determine if pattern interrupt falls in this segment
        interrupt_idx = (seg_num - 1) % len(PATTERN_INTERRUPT_TYPES)
        interrupt = PATTERN_INTERRUPT_TYPES[interrupt_idx]
        
        lines.extend([
            "",
            f"## SEGMENT {seg_num}: [SEGMENT TITLE] (~{start_ts} - ~{end_ts})",
            "",
            f"[VISUAL: Opening visual for segment {seg_num} — {visual_style}. Describe the specific scene, camera angle, and composition]",
            "",
            "NARRATION:",
            f'"[SEGMENT {seg_num} — MAIN POINT',
            "  - Start with the conclusion/insight (don't build up to it — state it, then prove it)",
            "  - Provide 2-3 pieces of evidence (stats, examples, comparisons)",
            "  - Use concrete numbers and specific examples, not abstractions",
            "  - Vary sentence length: Short. Short. Then a longer sentence providing nuance.",
            f'  - Target: ~{int(words_target / (num_segments + 2))} words for this segment]"',
            "",
            f"[VISUAL: Evidence/proof visual — graph, comparison, demonstration. {visual_style}]",
            "",
            "NARRATION:",
            '"[Continue developing this point — second paragraph with deeper evidence or a specific example that makes the insight tangible and memorable]"',
            "",
            f"### Pattern Interrupt ({interrupt['type'].replace('_', ' ').title()})",
            f"{interrupt['tag']}",
        ])
        
        if interrupt["narration"]:
            lines.append(f'NARRATION: "{interrupt["narration"]}"')
        
        lines.extend([
            "",
            "NARRATION:",
            '"[MICRO-PAYOFF — Give the viewer a small win or actionable insight before transitioning to the next segment. This rewards their attention and builds trust.]"',
            "",
            "[TRANSITION: Verbal bridge to next segment — 'But here's where it gets really interesting...' or 'Now that you understand X, let's talk about Y...']",
            "",
            "---",
        ])
        
        current_time = end_time
    
    # CTA
    lines.extend([
        "",
        f"## CTA (~{cta_timestamp_minutes}:00 — placed at 75% mark for peak engagement)",
        "",
        "[VISUAL: Channel branding / subscribe animation — clean, non-disruptive]",
        "",
        "NARRATION:",
        '"[NATURAL CTA — Never say \'please subscribe\' in isolation. Instead, connect the CTA to the value just demonstrated:',
        "'If this kind of [specific value type] is useful to you, hit subscribe — I break down [content promise] every [upload frequency].']\"",
        "",
        "---",
    ])
    
    # Climax
    climax_start = length_minutes - 2
    lines.extend([
        "",
        f"## CLIMAX (~{climax_start}:00 - ~{length_minutes - 1}:00)",
        "",
        f"[VISUAL: The most dramatic/impactful visual of the entire video — {visual_style} at its most intense]",
        "[MUSIC: Peak energy — the emotional high point of the soundtrack]",
        "",
        "NARRATION:",
        '"[THE PAYOFF — This is what the entire video has been building toward.',
        "  - Resolve the open loop from the hook",
        "  - Deliver the single most important insight/revelation",
        "  - This should feel like a 'click' moment for the viewer",
        '  - Make it specific, concrete, and memorable]"',
        "",
        f"[VISUAL: Resolution visual — the moment of clarity or revelation. {visual_style}]",
        "",
        "---",
    ])
    
    # Close
    lines.extend([
        "",
        f"## CLOSE (~{length_minutes - 1}:00 - {length_minutes}:00)",
        "",
        f"[VISUAL: Closing visual — callback to the opening or forward-looking. {visual_style}]",
        "[MUSIC: Resolving, reflective energy — winding down]",
        "",
        "NARRATION:",
        '"[FINAL THOUGHT — 2-3 sentences that:',
        "  1. Reframe the topic at a higher level (zoom out from specifics to significance)",
        "  2. Leave the viewer with something to think about",
        '  3. Tease the next video: \'Next [day], I\'m breaking down [related topic] — and the results might surprise you.\']"',
        "",
        "[VISUAL: End screen — 2 video suggestions (related content). Hold for 20 seconds]",
        "[AUDIO: Music fade out over 10 seconds]",
        "",
        "---",
        "",
        "## PRODUCTION NOTES",
        "",
        f"- **Total visual cues**: {num_segments * 3 + 6} (approximate — add more as needed)",
        f"- **Pattern interrupts**: {int(num_pattern_interrupts)} (every ~90 seconds)",
        f"- **Target word count**: ~{words_target} words",
        f"- **Words per minute target**: ~155 wpm (natural narration pace)",
        f"- **Music cues**: {num_segments + 3} (intro, segments, climax, close)",
        f"- **CTA placement**: ~{cta_timestamp_minutes}:00 (75% mark)",
        "- **Sound effects needed**: [List based on pattern interrupts used]",
        "",
        "## COMPANION SHORT SCRIPT",
        "",
        "[Extract the single most surprising or valuable 30-60 seconds from this script.]",
        "[Add bold on-screen text hook in the first frame.]",
        "[Design the ending to loop seamlessly back to the beginning.]",
        "",
        "---",
        "",
        "*Script generated by Video Content Engine. All [BRACKETED] sections require completion with niche-specific content.*",
    ])
    
    return "\n".join(lines)


def generate_shorts_script(topic: str, visual_style: str) -> str:
    """Generate a standalone YouTube Shorts script."""
    return f"""# SHORT: {topic.upper()}

**Target Length**: 30-60 seconds
**Platform**: YouTube Shorts / Instagram Reels / TikTok
**Visual Style**: {visual_style}
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

[VISUAL: Opening frame — MUST hook in 1 second. Bold, dramatic, scroll-stopping]
[TEXT ON SCREEN: Hook text — 5-7 words max, high contrast, large font]
[AUDIO: Trending sound or punchy original audio]

NARRATION (15-20 seconds):
"[Single insight delivered with maximum impact. No preamble, no introduction, no 'in this video.' Just the insight.]"

[VISUAL: Proof/evidence visual — show, don't just tell]
[TEXT ON SCREEN: Key stat or result — make it shareable]

NARRATION (10-15 seconds):
"[The 'so what' — why this matters. Connect to viewer's life. Make it personal.]"

[VISUAL: Loop point — visual that connects back to the opening]
[TEXT ON SCREEN: CTA — 'Follow for more' or 'Save this']

NARRATION (5-10 seconds):
"[End with a question, challenge, or cliffhanger that encourages rewatch or comment]"

---

**PRODUCTION NOTES**:
- Total duration target: 30-45 seconds (shorter is better for algorithm)
- On-screen text: Required throughout (80%+ watch muted)
- Loop design: Last frame should visually connect to first frame
- Pinned comment: Link to related long-form video
"""


def main():
    parser = argparse.ArgumentParser(description="Script Generator")
    parser.add_argument("--topic", required=True, help="Video topic")
    parser.add_argument("--length", type=int, default=10, help="Target length in minutes")
    parser.add_argument("--style", default="faceless", choices=["faceless", "talking_head", "hybrid"])
    parser.add_argument("--visual-style", default="Cinematic Realism", help="Visual art style")
    parser.add_argument("--platform", default="youtube", help="Primary platform")
    parser.add_argument("--shorts", action="store_true", help="Generate a Shorts script instead")
    parser.add_argument("--output", default=None, help="Output file path")
    
    args = parser.parse_args()
    
    if args.shorts:
        output = generate_shorts_script(args.topic, args.visual_style)
    else:
        output = generate_script_template(
            args.topic, args.length, args.visual_style, args.style, args.platform
        )
    
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Script written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
