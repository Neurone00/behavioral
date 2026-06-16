# Lovable Prompt: Behavioral Review Visualization Page

Build a visually astonishing, production-ready web page for a behavioral review system based on Microsoft Teams communication analysis and Transactional Analysis.

This is not a landing page. Build the actual experience as the first screen.

## Product context
- The dataset comes from a daily behavioral review pipeline.
- The system analyzes only meaningful replies by Luca Salvioni.
- The system scores communication deterministically on a 0-10 scale.
- The page must never expose raw Teams message text.
- Use only safe structured fields such as date, score, ego_state, transaction_type, escalation, counterpart, chat_type, and derived signal labels.
- Treat all TA labels as evidence-based work communication hypotheses, not personality claims.

## Visual ambition
The first viewport should feel like a fusion of Reuters Graphics, The Pudding, Distill, and premium creative WebGL work:
- Reuters-level clarity and editorial restraint once data needs to be read.
- The Pudding-style boldness, visual essay pacing, and surprise.
- Distill-style explorable interaction where the user learns by manipulating the scene.
- A data-art opening that feels luxurious, cinematic, and tactile, not gimmicky.

The opening experience must be a full-bleed 3D scene, not a card, not a dashboard grid, not a generic SaaS layout.

## Core concept
Create a hero visualization called `Behavior Constellation`.

It is a 3D living network made of:
- word-like signal nodes from derived labels such as `clarifying_question`, `risk_context`, `compressed_judgment`, `repair`, `delegation`, `approval`, `next_step`
- behavioral state nodes such as `Adult`, `Critical Parent`, `Nurturing Parent`, `Adapted Child`, `Free Child`
- transaction nodes such as `complementary` and `crossed_risk`
- escalation nodes such as `de-escalating`, `stable`, and `mild_risk`

The network should show how language-pattern signals connect to behavior labels over time.

## Hero interaction
In the opening 3D scene:
- Use Three.js or React Three Fiber.
- Render floating word/signal particles as luminous typographic anchors in space.
- Connect them with animated filaments that brighten when relationships strengthen.
- Let the network slowly breathe and rotate with subtle camera drift.
- On hover or tap, isolate the local neighborhood and surface a compact annotation panel.
- On scrub through time, reconfigure the network so the user sees how behavior clusters shift day by day.
- Make the transition from diffuse signal cloud to interpretable structure feel magical and smooth.
- The scene should begin atmospheric, then become analytical as the user interacts.

## Analytical story arc
After the 3D opening, transition into a disciplined visual analysis page with standard charts.

Include these sections in this order:
1. Hero 3D `Behavior Constellation`
2. Daily score trajectory
3. Ego state distribution over time
4. Complementary vs crossed-risk transaction trend
5. Escalation pattern view
6. Counterpart relationship map
7. Signal-to-behavior matrix
8. Coaching insights and notable shifts

## Required charts and modules
Build these modules:
- A line chart for daily average score across time.
- A stacked bar or stream chart for ego state counts over time.
- A diverging or grouped bar chart for complementary vs crossed-risk transactions.
- A compact heatmap showing which derived signals most often correlate with lower or higher scores.
- A relationship view showing counterparts grouped by relationship type such as direct report, peer, boss, collaborator.
- A scatter or dot-strip view showing how concise vs high-actionability replies cluster.
- A ranked panel for strongest positive patterns and highest-friction patterns.

## Interaction design
- Every chart should coordinate with the 3D scene.
- Hovering a chart element should highlight the corresponding cluster in the network.
- Filtering by date, counterpart, ego state, transaction type, or escalation should update the entire page.
- Include a time scrubber that animates the hero scene and all charts together.
- Include a mode toggle between `Overview`, `Conversations`, and `Coaching`.

## Tone and aesthetics
- No purple-heavy default palette.
- Avoid generic dark blue dashboards.
- Use a sophisticated palette: deep graphite, warm bone, oxidized teal, ember, acid yellow accents, and restrained coral for risk.
- Typography should feel editorial and intentional, not default UI fonts.
- The hero scene should feel premium, almost gallery-like, but the charts below must remain very readable.
- Motion should be meaningful and calm.
- No floating decorative cards everywhere.
- No rounded toy UI.
- No cheesy AI-glow overload.

## Layout rules
- Desktop: immersive first viewport with the next analytical section peeking below the fold.
- Mobile: preserve the wow factor, but simplify the 3D network into a performant, touch-friendly composition.
- Do not let text overlap or spill out of controls.
- The first screen must immediately signal that this is about communication patterns, not finance or CRM data.

## Data model assumptions
Expect records like:
- `date`
- `counterpart`
- `chat_type`
- `ego_state`
- `transaction_type`
- `escalation`
- `signals[]`
- `overall_score`
- optional role metadata like `relationship_to_luca`

Use mock data if needed, but structure the app so it can later ingest the real chart-ready files from:
- `data/charts/daily_trend.csv`
- `data/charts/transaction_trend.csv`
- `data/charts/ego_state_trend.csv`
- `data/daily/*.json`
- `config/review-profiles/ta-daily-review-v1.json`

## Implementation guidance
- Prefer React with React Three Fiber for the 3D hero.
- Use D3 or Observable Plot patterns for the chart section.
- Keep state architecture clean so every filter drives every module.
- Add tasteful transitions between sections.
- Make performance a first-class concern.
- The result should look custom-designed, not template-generated.

## Deliverable expectation
Produce a polished single-page app prototype that feels museum-grade in the hero and newsroom-grade in the analysis.

The page should make a user feel:
- curiosity in the first 5 seconds
- understanding in the next 30 seconds
- insight after 2 minutes

Build something that would genuinely stand out in a modern gallery of interactive data visualization work.