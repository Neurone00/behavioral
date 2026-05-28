# Behavioral Review Bootstrap

This repository bootstraps a Microsoft Teams behavioral review system using a
Transaction Analysis framing for professional communication.

## Default scope

- Timezone: `Europe/Rome`
- Current day only
- 1:1 and group chats first
- Excludes bots, system messages, meeting chats, and historical backfill by default

## Scoring model

Each meaningful reply is scored deterministically on five dimensions.

1. Adult clarity
2. Collaborative tone
3. De-escalation
4. Actionability
5. Respect / friction management

The weighted result becomes a daily `0-100` score and feeds daily, weekly, and
all-time rollups.

## Evaluation criteria

| Dimension | Weight | Strong signal | Weak signal |
| --- | ---: | --- | --- |
| Adult clarity | 0.30 | Factual, clear, bounded, problem-solving, low ambiguity | Confused, vague, reactive, or needlessly opaque |
| Collaborative tone | 0.20 | Invites cooperation, acknowledges others, keeps rapport intact | Dismissive, isolating, or adversarial framing |
| De-escalation | 0.20 | Reduces tension, keeps focus on the solution, avoids emotional heat | Escalates pressure, sarcasm, blame, or defensiveness |
| Actionability | 0.15 | Includes a clear next step, decision, constraint, or request | Adds noise without helping the work move forward |
| Respect / friction management | 0.15 | Direct without contempt; firm while preserving workability | Contempt, scolding energy, hostility, or unnecessary sharpness |

## Message scoring scale

- `+3`: Exceptionally constructive; strong Adult tone and strong work value
- `+2`: Clearly helpful and collaborative
- `+1`: Net positive and workable
- `0`: Neutral; functional but not especially strong or weak
- `-1`: Noticeably sharp, sloppy, or mildly escalatory
- `-2`: High-friction; likely to be felt as blunt or difficult
- `-3`: Severely counterproductive or contempt-laden

## Thresholds

- Positive example: message score `>= 1.25`
- Negative example: message score `<= -0.75`
- Good day: daily score `>= 70`
- Watch day: daily score `45-69`
- Risk day: daily score `< 45`

## TA interpretation rules

- `Adult`: factual, bounded, practical, and problem-solving
- `Critical Parent`: dismissive, scolding, contempt-adjacent, or moralizing
- `Adapted Child`: defensive, avoidant, appeasing, or apologetic without substance
- `Free Child`: humor or spontaneity that helps rapport without undermining the work

All TA classifications are evidence-based hypotheses from the text, not
personality judgments or diagnoses.

## Outputs

- Daily history for charting
- Rolling seven-day summary
- All-time summary
- Google Sheets dashboard as the preferred chart destination

## Privacy

- Raw Teams messages do not belong in GitHub
- Full narrative reports must stay in approved private storage
- GitHub should contain only code, prompts, workflows, schemas, and safe structured outputs
