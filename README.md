# Notra

Personal writing voice profile and article archive for AI content generation.

## What is this?

This repo contains my writing DNA — extracted from my Medium articles — so AI tools can generate content that matches my writing style.

## Structure

```
Notra/
├── voice-profile/
│   └── voice-profile.md    # Complete writing voice analysis & AI prompt template
├── articles/                # Raw Medium articles (source material)
│   ├── 01_*.md - 05_*.md   # Cat behavior articles
│   ├── 06_*.md             # Brain & Metaverse
│   ├── 07_*.md             # Siberian cats
│   └── 08_*.md - 10_*.md   # Tech/Productivity (Microsoft Loop, Gmail)
├── web-agency/              # Automated client intake form for web agency
│   ├── scripts/
│   │   └── create-intake-form.py   # Tally.so form creation via API (174 blocks, 7 pages)
│   └── docs/
│       └── client-intake-form-spec.md  # Full form specification
└── README.md
```

## How to Use

### For AI Content Generation

Copy the prompt template from `voice-profile/voice-profile.md` (Section 8) and paste it into any AI tool (ChatGPT, Claude, etc.) along with your topic. The AI will write in my voice.

### For Reference

Read through the `articles/` folder to see real examples of my writing across different topics.

## Web Agency — Client Intake Form

Automated client intake form builder for a web agency pipeline. Creates a 7-page, 174-block Tally.so form via API to collect business data from Thai SME clients before building their website.

- **Script**: `web-agency/scripts/create-intake-form.py` — Creates the full form programmatically
- **Spec**: `web-agency/docs/client-intake-form-spec.md` — Complete field-by-field specification
- **Stack**: Python + Tally.so API (undocumented patterns discovered through reverse engineering)
- **Form**: 7 pages covering business info, online presence, branding, services, website preferences, domain/delivery, and additional notes

### Key Technical Discoveries

The Tally.so API has several undocumented requirements not in official docs:
1. `groupType` must match the block's own type (not `"QUESTION"`)
2. Each input block needs its own unique `groupUuid`
3. Choice options require `isFirst`/`isLast` boolean flags
4. HTML tags like `<br>`, `<small>` are rejected in TITLE/FORM_TITLE blocks

### Usage

```bash
export TALLY_API_KEY="your-api-key"
python3 web-agency/scripts/create-intake-form.py
```

## Source

All articles scraped from [medium.com/@ohmm](https://medium.com/@ohmm)

## Author

**Ohm Mekavichai** (มิ่งรัฐ เมฆวิชัย)
- Medium: [@ohmm](https://medium.com/@ohmm)
- GitHub: [@mingrath](https://github.com/mingrath)
