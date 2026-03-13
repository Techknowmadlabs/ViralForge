# Phase 4: SEO & Discovery Engine

## Purpose

Engineer every video for maximum discoverability across search, browse, suggested, and Shorts shelf. This phase produces keyword databases, metadata templates, and algorithm optimization playbooks for each platform.

---

## YouTube SEO Architecture

### Keyword Research Process

Use web search to pull current data for each step.

**Step 1: Seed Keywords**
Generate 10-15 seed keywords from the niche. These are broad terms the target audience searches.

**Step 2: Long-Tail Expansion**
For each seed keyword, generate 5-10 long-tail variations using these patterns:
- "[keyword] for beginners"
- "[keyword] explained"
- "[keyword] vs [alternative]"
- "how to [keyword]"
- "best [keyword] [year]"
- "[keyword] mistakes"
- "why [keyword] [outcome]"
- "[keyword] tutorial"
- "[keyword] in [time period]"

**Step 3: Search Volume & Competition Assessment**

Use web search for each keyword:
- Search: "[keyword] youtube search volume"
- Search: "site:youtube.com [keyword]" — count results, check competitor quality
- Check YouTube autocomplete by searching: "youtube autocomplete [keyword]"

### Keyword Database Format

```markdown
| Keyword | Est. Monthly Volume | Competition | Search Intent | Can New Channel Rank? | Priority |
|---------|-------------------|-------------|---------------|----------------------|----------|
| [keyword] | [volume] | Low/Med/High | Info/Nav/Trans | Yes/Maybe/No | P1/P2/P3 |
```

**Priority Assignment Rules**:
- **P1** (Target immediately): Low competition + high volume + informational intent + new channel can rank
- **P2** (Target in Month 2-3): Medium competition + good volume + channel has some authority
- **P3** (Future target): High competition + high volume + requires established channel

---

## Title Engineering

Titles are the single highest-leverage SEO element. Every title must satisfy both the algorithm (keyword placement) and the human (emotional trigger).

### 12 Proven Title Formulas

| # | Formula | Psychology | Example |
|---|---------|-----------|---------|
| 1 | **[Number] [Things] That [Outcome]** | Specificity + benefit | "7 AI Tools That Replace a $5K/mo Marketing Team" |
| 2 | **Why [Authority] [Surprising Action]** | Credibility + curiosity gap | "Why Harvard Professors Are Quitting to Start YouTube Channels" |
| 3 | **I [Did X] for [Time] — Here's What Happened** | Personal experiment + open loop | "I Used AI to Trade Stocks for 30 Days — Here's What Happened" |
| 4 | **[Topic] Is a Lie (Here's the Truth)** | Contrarian + revelation | "Passive Income Is a Lie (Here's What Actually Works)" |
| 5 | **How [Specific Person/Group] [Achieves Outcome]** | Blueprint + aspiration | "How Top 1% YouTubers Plan Their Content (Full Strategy)" |
| 6 | **[Topic] Explained in [Time]** | Value + time commitment | "Quantum Computing Explained in 10 Minutes" |
| 7 | **The [Adjective] Guide to [Topic]** | Comprehensiveness | "The Complete Guide to Building Wealth in Your 30s" |
| 8 | **[Year] [Topic]: Everything Changed** | Timeliness + stakes | "2026 AI Update: Everything Changed Last Month" |
| 9 | **[Do This] Before [Deadline/Consequence]** | Urgency + fear | "Move Your Money Before the Fed's Next Decision" |
| 10 | **What [Number] of [Outcome] Reveals About [Topic]** | Data-driven + insight | "What $10M in YouTube Revenue Reveals About the Algorithm" |
| 11 | **Stop [Common Mistake] — Do [Better Action] Instead** | Correction + solution | "Stop Saving Money — Invest in These 3 Things Instead" |
| 12 | **[Topic] for [Specific Audience] ([Specific Promise])** | Targeted + concrete | "AI for Small Business Owners (Save 20 Hours/Week)" |

### Title Optimization Rules

- **Front-load the keyword** — YouTube weighs the first 3-5 words most heavily
- **Keep it under 60 characters** for full display on all devices
- **Include a number** when possible — titles with numbers get 36% higher CTR
- **Use power words**: "Revealed", "Secret", "Ultimate", "Complete", "Brutal", "Insane"
- **Never use clickbait without payoff** — the video must deliver on the title's promise
- **A/B test by generating 3 variants** per video and selecting based on thumbnail pairing

---

## Description Template

```markdown
[HOOK: 1-2 sentences that expand on the title's promise — this appears in search results]

[PRIMARY KEYWORD used naturally in the first sentence]

In this video, [brief 2-sentence summary of what viewers will learn/see].

🔑 Key Takeaways:
00:00 — [Chapter 1 Title]
[MM:SS] — [Chapter 2 Title]
[MM:SS] — [Chapter 3 Title]
[MM:SS] — [Chapter 4 Title]
[MM:SS] — [Chapter 5 Title]

📌 Resources Mentioned:
- [Resource 1 with link]
- [Resource 2 with link]

🔗 Related Videos:
- [Internal link to related video 1]
- [Internal link to related video 2]
- [Internal link to related video 3]

📢 Connect:
- [Platform 1 link]
- [Platform 2 link]
- [Platform 3 link]

#[keyword1] #[keyword2] #[keyword3]

[SECONDARY KEYWORDS woven into 2-3 natural sentences at the end — this is for search, not human readers]
```

### Description Rules

- **First 150 characters are critical** — they appear in search results and browse features
- **Timestamps/chapters are mandatory** — they create "key moments" in search results, appearing as rich snippets
- **Internal links drive session time** — always link to 2-3 related videos on the channel
- **3-5 hashtags maximum** — YouTube uses the first 3 above the title in some views
- **Never keyword stuff** — descriptions should read naturally. The algorithm is sophisticated enough to understand semantic relevance

---

## Tag Strategy

Tags are less important than they were historically, but still contribute to discovery.

### Tag Architecture (15-20 per video)

```
Tier 1 (3-5 tags): Exact-match primary and secondary keywords
Tier 2 (5-7 tags): Long-tail keyword variations
Tier 3 (3-5 tags): Broad niche terms
Tier 4 (2-3 tags): Channel name and series name (for branding)
```

**Tag Rules**:
- First tag = exact primary keyword
- Mix broad and specific (don't go all broad or all long-tail)
- Include common misspellings if relevant
- Never use tags that don't relate to the actual content — YouTube penalizes misleading tags
- Check competitor tags for keyword ideas (use web search for tag extraction tools)

---

## Shorts-to-Long-Form Funnel

YouTube Shorts are the primary discovery mechanism for new channels. Every Shorts strategy should feed the long-form content library.

### Funnel Architecture

```
SHORT (Discovery) → LONG-FORM (Engagement) → SUBSCRIBER (Retention) → CUSTOMER (Monetization)

Short hooks a viewer with a surprising fact/clip
→ End screen + pinned comment link to the full video
→ Full video delivers comprehensive value
→ Viewer subscribes for more
→ Viewer eventually buys product/clicks affiliate/watches enough for AdSense
```

### Shorts Content Types That Drive Long-Form Views

| Short Type | Conversion Rate to Long-Form | Example |
|-----------|------------------------------|---------|
| **Teaser Clip** (best moment from long video) | Highest — 5-8% | "This one strategy made me $10K. Full breakdown in the link." |
| **Contrarian Fact** | High — 3-5% | "[Surprising stat]. I explain why in my latest video." |
| **Quick Tip** (standalone value) | Medium — 2-3% | "Here's a 30-second trick for [topic]." |
| **Behind the Scenes** | Low-Medium — 1-2% | "How I research for my videos..." |
| **Trend Reaction** | Low — 0.5-1% | High views, low long-form conversion |

### Shorts Optimization Rules

- **Hook in first 1 second** — Shorts audience has zero patience
- **Loop structure** — End the Short at a point that encourages rewatching
- **Vertical text only** — Never use horizontal text on vertical content
- **On-screen captions mandatory** — 80%+ of Shorts are watched without sound
- **15-45 seconds optimal** — Under 15 feels incomplete, over 45 loses attention
- **Pinned comment** with link to the related long-form video on every Short

---

## Platform-Specific SEO

### Instagram Reels SEO
- Captions are indexed — include keywords naturally in the caption
- Hashtags: 5-10 per reel, mix of niche-specific and trending
- Alt text: Add descriptive alt text with keywords
- Audio: Using trending audio dramatically boosts discovery

### TikTok SEO
- TikTok's search is exploding — treat it as a search engine
- Include keywords in the on-screen text
- Captions: Front-load keywords in the first line
- Hashtags: 3-5 per video, at least one trending
- Comments: Reply to comments with keywords (TikTok indexes these)

### X/Twitter Video SEO
- Thread the video with keyword-rich text
- Tag relevant accounts for amplification
- Post at peak hours for the target audience's timezone
- Use polls and questions to drive engagement (algorithmic boost)

### Facebook Video SEO
- Titles and descriptions are heavily indexed
- Tags: Use Facebook's content tag system
- First 3 seconds determine autoplay retention
- Groups: Cross-post to 3-5 relevant Facebook groups

---

## Phase 4 Deliverables Checklist

- [ ] 20+ keywords researched with volume, competition, and priority
- [ ] Title variants generated for first 10 videos (3 per video)
- [ ] Description template finalized with all sections
- [ ] Tag strategy documented with tier structure
- [ ] Shorts-to-long-form funnel plan created
- [ ] Platform-specific SEO rules documented
- [ ] First 5 video titles and descriptions fully written and optimized
