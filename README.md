# Behavioral Review Bootstrap

This repository bootstraps a Microsoft Teams behavioral review system using a
Transaction Analysis framing for professional communication.

## Default scope

- Timezone: `Europe/Rome`
- Current day only
- 1:1 and group chats first
- Excludes bots, system messages, meeting chats, and historical backfill by default

## Scoring model

Each meaningful reply is scored deterministically on:

1. Adult clarity
2. Collaborative tone
3. De-escalation
4. Actionability
5. Respect / friction management

The weighted result becomes a daily `0-100` score and feeds daily, weekly, and
all-time rollups.

## Thresholds

- Positive example: message score `>= 1.25`
- Negative example: message score `<= -0.75`
- Good day: daily score `>= 70`
- Watch day: daily score `45-69`
- Risk day: daily score `< 45`

## Outputs

- Daily history for charting
- Rolling seven-day summary
- All-time summary
- Google Sheets dashboard as the preferred chart destination

## Privacy

- Raw Teams messages do not belong in GitHub
- Full narrative reports must stay in approved private storage
- GitHub should contain only code, prompts, workflows, schemas, and safe structured outputs
