#!/usr/bin/env python3
"""
Content Calendar Generator — Produces 90-day upload calendars with
production-ready entries, series concepts, and milestone targets.

Usage:
    python scripts/content_calendar.py --niche "AI tools" --cadence 3 --platforms youtube,instagram,x
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


def generate_calendar_structure(
    niche: str,
    cadence: int,
    platforms: list[str],
    start_date: datetime | None = None,
) -> dict[str, Any]:
    """Generate a 90-day content calendar structure."""
    if start_date is None:
        start_date = datetime.now()
    
    calendar = {
        "metadata": {
            "niche": niche,
            "cadence_per_week": cadence,
            "platforms": platforms,
            "generated_at": datetime.now().isoformat(),
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": (start_date + timedelta(days=90)).strftime("%Y-%m-%d"),
        },
        "months": [],
        "series_concepts": [],
        "milestones": {},
    }
    
    # Month structures
    month_configs = [
        {
            "number": 1,
            "name": "Foundation",
            "objective": "Establish authority, test what resonates, feed the algorithm classification data",
            "content_mix": {
                "evergreen_search": 0.60,
                "pillar_establishing": 0.20,
                "quick_wins_trending": 0.20,
            },
            "focus": "Broad, high-search-volume topics to help YouTube classify the channel",
            "rules": [
                "First 3 videos must cover the broadest, most-searched topics",
                "Every video needs a companion Short",
                "Consistency over perfection — hit the upload schedule",
                "Descriptions must include timestamps/chapters",
            ],
        },
        {
            "number": 2,
            "name": "Optimization",
            "objective": "Double down on what analytics show is working, launch first series",
            "content_mix": {
                "evergreen": 0.40,
                "high_performing_variants": 0.30,
                "series_content": 0.20,
                "experimental": 0.10,
            },
            "focus": "Sequels and variations of Month 1 winners, first recurring series",
            "rules": [
                "Review Month 1 analytics before planning",
                "Create 2-3 variations of top performers",
                "Launch first named series",
                "A/B test thumbnails on top 3 videos",
                "Start cross-posting to secondary platforms",
            ],
        },
        {
            "number": 3,
            "name": "Scale & Monetize",
            "objective": "Push toward monetization, attract sponsors, build content moat",
            "content_mix": {
                "evergreen": 0.30,
                "series_content": 0.30,
                "collaboration_trend": 0.20,
                "sponsor_friendly": 0.20,
            },
            "focus": "Tentpole content, internal linking, sponsor-ready production quality",
            "rules": [
                "Every video references at least one other channel video",
                "Produce at least one tentpole video",
                "Create a channel trailer / best-of compilation",
                "Begin sponsor outreach if past 1K subscribers",
                "Document production SOPs for scaling",
            ],
        },
    ]
    
    for month_config in month_configs:
        total_videos = cadence * 4  # ~4 weeks per month
        entries = []
        
        for i in range(total_videos):
            week_num = (i // cadence) + 1
            day_in_week = i % cadence
            
            # Calculate the actual date
            week_offset = ((month_config["number"] - 1) * 4 + (week_num - 1)) * 7
            day_offset = [1, 3, 5][day_in_week] if cadence == 3 else [1, 4][day_in_week] if cadence == 2 else [3][0]
            video_date = start_date + timedelta(days=week_offset + day_offset)
            
            # Determine content type based on mix
            video_number = (month_config["number"] - 1) * total_videos + i + 1
            
            entry = {
                "video_number": video_number,
                "date": video_date.strftime("%Y-%m-%d"),
                "day_of_week": video_date.strftime("%A"),
                "week": week_num,
                "title": f"[VIDEO {video_number} — TITLE TO BE GENERATED]",
                "pillar": "[ASSIGN FROM CONTENT PILLARS]",
                "type": "[ASSIGN: evergreen / reactive / series / experimental]",
                "target_keyword": "[PRIMARY KEYWORD]",
                "hook_preview": "[FIRST 8 SECONDS — WRITE THE ACTUAL HOOK]",
                "thumbnail_concept": "[1-2 SENTENCE VISUAL DESCRIPTION]",
                "estimated_length_minutes": 10,
                "production_time_hours": 3,
                "companion_content": {
                    "youtube_short": "[REPURPOSE ANGLE FOR 60-SEC SHORT]",
                    "instagram_reel": "[ADAPTATION ANGLE]" if "instagram" in platforms else None,
                    "x_twitter": "[POST HOOK / THREAD ANGLE]" if "x" in platforms else None,
                    "tiktok": "[TREND-NATIVE ADAPTATION]" if "tiktok" in platforms else None,
                    "facebook": "[SHAREABLE ANGLE]" if "facebook" in platforms else None,
                    "linkedin": "[PROFESSIONAL ANGLE]" if "linkedin" in platforms else None,
                },
                "series_name": None,
                "internal_link_to": f"Video {max(1, video_number - 3)}" if video_number > 3 else None,
            }
            # Remove None companion content
            entry["companion_content"] = {
                k: v for k, v in entry["companion_content"].items() if v is not None
            }
            entries.append(entry)
        
        month = {
            **month_config,
            "total_videos": total_videos,
            "entries": entries,
        }
        calendar["months"].append(month)
    
    # Series concepts
    calendar["series_concepts"] = [
        {
            "name": f"[SERIES 1 NAME — {niche} Weekly Deep Dive]",
            "concept": f"Weekly exploration of one specific topic within {niche}, going deeper than any competitor",
            "format": "10-12 minute structured analysis with consistent opening format",
            "frequency": "Weekly",
            "target_episodes": 12,
            "launch_month": 2,
            "thumbnail_template": "Consistent color accent + series logo + episode number + topic text",
            "signature_opening": "[WRITE A RECURRING OPENING LINE OR PATTERN]",
        },
        {
            "name": f"[SERIES 2 NAME — {niche} Myth Busters]",
            "concept": f"Debunking common misconceptions in {niche} with evidence-based analysis",
            "format": "8-10 minutes, claim → evidence → verdict structure",
            "frequency": "Biweekly",
            "target_episodes": 6,
            "launch_month": 2,
            "thumbnail_template": "Red X over myth + green check over truth + bold text",
            "signature_opening": "[WRITE A RECURRING OPENING LINE OR PATTERN]",
        },
    ]
    
    # Milestones
    calendar["milestones"] = {
        "month_1": {
            "subscribers_target": "100-500",
            "views_target": "5,000-20,000 total",
            "videos_published": cadence * 4,
            "key_actions": [
                "Establish consistent upload schedule",
                "Test 3+ title/thumbnail approaches",
                "Identify top-performing content type",
            ],
        },
        "month_2": {
            "subscribers_target": "500-2,000",
            "views_target": "20,000-80,000 total",
            "videos_published": cadence * 4 * 2,
            "key_actions": [
                "Launch first series",
                "Double down on top-performing topics",
                "Begin cross-platform distribution",
                "A/B test thumbnails systematically",
            ],
        },
        "month_3": {
            "subscribers_target": "1,000-5,000",
            "views_target": "50,000-200,000 total",
            "videos_published": cadence * 4 * 3,
            "key_actions": [
                "Apply for YouTube Partner Program (if eligible)",
                "Produce tentpole content",
                "Begin sponsor outreach",
                "Document SOPs for potential team scaling",
            ],
        },
    }
    
    return calendar


def calendar_to_markdown(calendar: dict[str, Any]) -> str:
    """Convert calendar structure to markdown."""
    lines = [
        f"# 90-Day Content Calendar — {calendar['metadata']['niche']}",
        "",
        f"**Generated**: {calendar['metadata']['generated_at'][:10]}",
        f"**Upload Cadence**: {calendar['metadata']['cadence_per_week']} videos/week",
        f"**Platforms**: {', '.join(calendar['metadata']['platforms'])}",
        f"**Date Range**: {calendar['metadata']['start_date']} → {calendar['metadata']['end_date']}",
        "",
        "---",
        "",
    ]
    
    for month in calendar["months"]:
        lines.extend([
            f"## Month {month['number']}: {month['name']}",
            "",
            f"**Objective**: {month['objective']}",
            f"**Total Videos**: {month['total_videos']}",
            f"**Focus**: {month['focus']}",
            "",
            "**Content Mix**:",
        ])
        for mix_type, pct in month["content_mix"].items():
            lines.append(f"- {mix_type.replace('_', ' ').title()}: {int(pct * 100)}%")
        
        lines.extend(["", "**Rules**:"])
        for rule in month["rules"]:
            lines.append(f"- {rule}")
        
        lines.extend(["", "### Upload Schedule", ""])
        
        for entry in month["entries"]:
            lines.extend([
                f"#### Video #{entry['video_number']} — {entry['date']} ({entry['day_of_week']})",
                "",
                f"- **Title**: {entry['title']}",
                f"- **Pillar**: {entry['pillar']}",
                f"- **Type**: {entry['type']}",
                f"- **Target Keyword**: {entry['target_keyword']}",
                f"- **Hook**: {entry['hook_preview']}",
                f"- **Thumbnail**: {entry['thumbnail_concept']}",
                f"- **Length**: ~{entry['estimated_length_minutes']} min",
                f"- **Production Time**: ~{entry['production_time_hours']} hours",
            ])
            if entry["companion_content"]:
                lines.append("- **Companion Content**:")
                for platform, angle in entry["companion_content"].items():
                    lines.append(f"  - {platform.replace('_', ' ').title()}: {angle}")
            if entry["series_name"]:
                lines.append(f"- **Series**: {entry['series_name']}")
            if entry["internal_link_to"]:
                lines.append(f"- **Internal Link**: Reference {entry['internal_link_to']}")
            lines.append("")
        
        lines.append("---\n")
    
    # Series concepts
    lines.extend(["## Series Concepts", ""])
    for series in calendar["series_concepts"]:
        lines.extend([
            f"### {series['name']}",
            "",
            f"**Concept**: {series['concept']}",
            f"**Format**: {series['format']}",
            f"**Frequency**: {series['frequency']}",
            f"**Target Episodes**: {series['target_episodes']}",
            f"**Launch**: Month {series['launch_month']}",
            f"**Thumbnail Template**: {series['thumbnail_template']}",
            f"**Signature Opening**: {series['signature_opening']}",
            "",
        ])
    
    # Milestones
    lines.extend(["---", "", "## Growth Milestones", ""])
    for period, targets in calendar["milestones"].items():
        lines.extend([
            f"### {period.replace('_', ' ').title()}",
            f"- **Subscriber Target**: {targets['subscribers_target']}",
            f"- **Views Target**: {targets['views_target']}",
            f"- **Videos Published**: {targets['videos_published']}",
            "- **Key Actions**:",
        ])
        for action in targets["key_actions"]:
            lines.append(f"  - {action}")
        lines.append("")
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Content Calendar Generator")
    parser.add_argument("--niche", required=True, help="Content niche")
    parser.add_argument("--cadence", type=int, default=3, help="Videos per week (default: 3)")
    parser.add_argument("--platforms", default="youtube,instagram,x", help="Target platforms")
    parser.add_argument("--start-date", default=None, help="Start date (YYYY-MM-DD, default: today)")
    parser.add_argument("--output", default=None, help="Output file path")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    
    args = parser.parse_args()
    platforms = [p.strip() for p in args.platforms.split(",")]
    start = datetime.strptime(args.start_date, "%Y-%m-%d") if args.start_date else None
    
    calendar = generate_calendar_structure(args.niche, args.cadence, platforms, start)
    
    if args.format == "markdown":
        output = calendar_to_markdown(calendar)
    else:
        output = json.dumps(calendar, indent=2, default=str)
    
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Calendar written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
