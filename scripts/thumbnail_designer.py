#!/usr/bin/env python3
"""
Thumbnail Designer — Generates thumbnail concepts with AI image prompts,
composition guidelines, and A/B test variants.

Usage:
    python scripts/thumbnail_designer.py --title "7 AI Tools That Replace Your Marketing Team" \
        --style "Cinematic Realism" --niche "AI tools"
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


EMOTION_TRIGGERS = {
    "curiosity": {
        "face_expression": "wide eyes, raised eyebrows, slightly open mouth",
        "color_emphasis": "Yellow and orange accents on dark background",
        "text_style": "Question format or incomplete statement with '...'",
        "composition": "Subject looking at something off-frame, mystery element partially hidden",
    },
    "shock": {
        "face_expression": "jaw dropped, eyes wide, hands on head or covering mouth",
        "color_emphasis": "Red and black, high contrast, aggressive angles",
        "text_style": "ALL CAPS, exclamation, or 'EXPOSED' / 'CAUGHT' / 'REVEALED'",
        "composition": "Dramatic reveal moment, before/after split, breaking news layout",
    },
    "desire": {
        "face_expression": "satisfied smile, confident posture, aspirational pose",
        "color_emphasis": "Gold, green (money), luxurious tones",
        "text_style": "Specific numbers or results, '$XX,XXX' format",
        "composition": "Subject with the result/prize, aspirational lifestyle elements",
    },
    "fear": {
        "face_expression": "worried, anxious, hand on chin thinking",
        "color_emphasis": "Red warnings, dark ominous backgrounds",
        "text_style": "'Don't...', 'WARNING:', 'STOP', 'Before it's too late'",
        "composition": "Danger element prominent, subject in defensive position",
    },
    "satisfaction": {
        "face_expression": "thumbs up, checklist pose, nod of approval",
        "color_emphasis": "Green checkmarks, clean bright backgrounds",
        "text_style": "'The Only Guide You Need', 'Complete', 'Everything'",
        "composition": "Organized layout, numbered steps visible, clean and trustworthy",
    },
}

THUMBNAIL_LAYOUTS = {
    "split_screen": {
        "description": "Left/right or top/bottom comparison",
        "best_for": "Before/after, vs comparisons, contrarian content",
        "composition": "50/50 split with clear divider, contrasting colors on each side",
    },
    "hero_center": {
        "description": "Central subject with text around it",
        "best_for": "Product reveals, person-focused, single concept",
        "composition": "Subject fills 60% of frame center, text top or bottom, clean background",
    },
    "diagonal_energy": {
        "description": "Elements arranged on a diagonal for dynamic energy",
        "best_for": "Action content, urgency, breaking news",
        "composition": "Main element on diagonal, supporting elements offset, dynamic angle",
    },
    "grid_reveal": {
        "description": "Multiple elements in a grid with one highlighted",
        "best_for": "Lists, rankings, collections",
        "composition": "2x2 or 3x3 grid with one element larger/brighter, others slightly muted",
    },
    "mystery_tease": {
        "description": "Partially hidden element with curiosity text",
        "best_for": "Reveals, secrets, surprising content",
        "composition": "Key element blurred/hidden/partially covered, question mark or '?' visible",
    },
}


def generate_thumbnail_concepts(
    title: str,
    visual_style: str,
    niche: str,
    num_variants: int = 3,
) -> list[dict]:
    """Generate thumbnail concept variants for A/B testing."""
    concepts = []
    
    # Variant A: Emotion-Led
    concepts.append({
        "variant": "A",
        "strategy": "Emotion-Led",
        "wins_when": "Topic has a strong emotional hook (shock, curiosity, desire)",
        "layout": "hero_center",
        "primary_element": {
            "type": "face_or_dramatic_object",
            "description": f"[AI-generated face/object showing extreme emotion related to '{title}'. {visual_style} style. High detail, dramatic lighting.]",
            "frame_percentage": "50-60%",
            "ai_prompt": f"[STYLE PREFIX] A dramatic close-up portrait showing [EMOTION] expression, related to {niche}. {visual_style} art style, cinematic lighting, shallow depth of field, 16:9 aspect ratio, vibrant and eye-catching [STYLE SUFFIX]",
        },
        "text_overlay": {
            "text": "[2-4 WORDS — extract the emotional core of the title]",
            "max_words": 4,
            "placement": "lower-third or upper-right",
            "style": "Bold sans-serif, high contrast stroke/shadow, readable at 48px",
            "color": "[HIGH CONTRAST against background — white on dark, black on light, or accent color]",
        },
        "background": {
            "treatment": "Blurred or gradient-faded version of the scene",
            "color_scheme": "[Brand colors from style guide, adjusted for CTR optimization]",
        },
        "mobile_test": "Must be legible and compelling at 168x94px (smallest YouTube render)",
    })
    
    # Variant B: Curiosity-Led
    concepts.append({
        "variant": "B",
        "strategy": "Curiosity-Led",
        "wins_when": "Topic reveals something surprising or challenges expectations",
        "layout": "mystery_tease",
        "primary_element": {
            "type": "provocative_scene",
            "description": f"[Scene that raises a question. Something unexpected, partially hidden, or contradictory related to '{title}'. {visual_style} style.]",
            "frame_percentage": "40-50%",
            "ai_prompt": f"[STYLE PREFIX] A mysterious scene related to {niche}, showing [UNEXPECTED ELEMENT] with dramatic composition. Something partially hidden or revealed. {visual_style}, cinematic, 16:9 [STYLE SUFFIX]",
        },
        "text_overlay": {
            "text": "[QUESTION or INCOMPLETE STATEMENT that demands clicking to resolve]",
            "max_words": 4,
            "placement": "center or top-third",
            "style": "Bold, possibly with question mark or '...' to create information gap",
            "color": "Yellow or white on dark — curiosity colors",
        },
        "background": {
            "treatment": "Dark, atmospheric, sense of mystery",
            "color_scheme": "Dark palette with one bright accent pulling the eye",
        },
        "mobile_test": "The question/mystery must be visible at thumbnail scale",
    })
    
    # Variant C: Value-Led
    concepts.append({
        "variant": "C",
        "strategy": "Value-Led",
        "wins_when": "Audience is actively searching for solutions (how-to, tutorial, guide)",
        "layout": "grid_reveal",
        "primary_element": {
            "type": "organized_value_display",
            "description": f"[Clean, organized visual showing the value proposition. Numbers, results, or structured preview of what the viewer will learn. {visual_style} style.]",
            "frame_percentage": "60-70%",
            "ai_prompt": f"[STYLE PREFIX] A clean, organized infographic-style scene related to {niche}. Professional, trustworthy, with clear structure showing value/results. {visual_style}, bright and inviting, 16:9 [STYLE SUFFIX]",
        },
        "text_overlay": {
            "text": "[CLEAR BENEFIT STATEMENT — specific number or promise]",
            "max_words": 4,
            "placement": "top-center or side",
            "style": "Clean, professional, trust-building. Green for positive results, specific numbers prominent",
            "color": "Brand primary color, clean contrast",
        },
        "background": {
            "treatment": "Light, clean, professional — trust-building",
            "color_scheme": "Light background with brand accent colors",
        },
        "mobile_test": "The value proposition must be clear at thumbnail scale",
    })
    
    return concepts[:num_variants]


def concepts_to_markdown(
    title: str,
    concepts: list[dict],
    visual_style: str,
    niche: str,
) -> str:
    """Convert thumbnail concepts to markdown documentation."""
    lines = [
        f"# Thumbnail Concepts: {title}",
        "",
        f"**Visual Style**: {visual_style}",
        f"**Niche**: {niche}",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        "## The 3-Element Rule",
        "",
        "Every thumbnail contains exactly 3 elements:",
        "1. **Primary Subject** (50-60% of frame) — face/emotion OR dramatic object",
        "2. **Text Overlay** (20-30% of frame) — 2-4 words, readable at 48px",
        "3. **Background** (remaining) — mood-setting, contrast-providing",
        "",
        "---",
    ]
    
    for concept in concepts:
        lines.extend([
            "",
            f"## Variant {concept['variant']}: {concept['strategy']}",
            "",
            f"**Wins When**: {concept['wins_when']}",
            f"**Layout**: {concept['layout']}",
            "",
            "### Primary Element",
            f"- **Type**: {concept['primary_element']['type']}",
            f"- **Description**: {concept['primary_element']['description']}",
            f"- **Frame %**: {concept['primary_element']['frame_percentage']}",
            "",
            "**AI Generation Prompt**:",
            f"```",
            concept['primary_element']['ai_prompt'],
            "```",
            "",
            "### Text Overlay",
            f"- **Text**: {concept['text_overlay']['text']}",
            f"- **Max Words**: {concept['text_overlay']['max_words']}",
            f"- **Placement**: {concept['text_overlay']['placement']}",
            f"- **Style**: {concept['text_overlay']['style']}",
            f"- **Color**: {concept['text_overlay']['color']}",
            "",
            "### Background",
            f"- **Treatment**: {concept['background']['treatment']}",
            f"- **Color Scheme**: {concept['background']['color_scheme']}",
            "",
            f"**Mobile Legibility Check**: {concept['mobile_test']}",
            "",
            "---",
        ])
    
    lines.extend([
        "",
        "## A/B Testing Protocol",
        "",
        "1. Upload with Variant A thumbnail",
        "2. After 48 hours and 1,000+ impressions, record CTR",
        "3. Switch to Variant B",
        "4. After 48 hours and 1,000+ impressions, record CTR",
        "5. Keep the winner. Test Variant C against winner if needed.",
        "6. Log result in A/B testing spreadsheet",
        "",
        "## Emotion Trigger Reference",
        "",
        "| Emotion | Face Expression | Color | Text Style |",
        "|---------|----------------|-------|-----------|",
    ])
    
    for emotion, details in EMOTION_TRIGGERS.items():
        lines.append(
            f"| {emotion.title()} | {details['face_expression']} | "
            f"{details['color_emphasis']} | {details['text_style']} |"
        )
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Thumbnail Designer")
    parser.add_argument("--title", required=True, help="Video title")
    parser.add_argument("--style", default="Cinematic Realism", help="Visual art style")
    parser.add_argument("--niche", required=True, help="Content niche")
    parser.add_argument("--variants", type=int, default=3, help="Number of variants (1-3)")
    parser.add_argument("--output", default=None, help="Output file path")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    
    args = parser.parse_args()
    
    concepts = generate_thumbnail_concepts(args.title, args.style, args.niche, args.variants)
    
    if args.format == "markdown":
        output = concepts_to_markdown(args.title, concepts, args.style, args.niche)
    else:
        output = json.dumps(concepts, indent=2)
    
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Thumbnail concepts written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
