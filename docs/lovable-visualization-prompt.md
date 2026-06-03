# Lovable Prompt: Behavioral Constellation

Build a stunning interactive data visualization web app for a behavioral communication review system.

## Project name

**Behavioral Constellation**

## Purpose

Create a premium, cinematic dashboard that visualizes how words, communication behaviors, Transactional Analysis ego states, role relationships, and performance scores evolve over time.

The app should feel like a mix between:

- a high-end data art installation
- an executive analytics dashboard
- an interactive 3D knowledge graph
- a personal behavioral operating system

## Core concept

The hero visualization is a **3D constellation of communication patterns**.

Each node represents one of:

- a recurring word or phrase
- a behavioral pattern
- a Transactional Analysis ego state
- a person or role relationship
- a scored communication dimension
- a detected risk pattern
- a strength pattern
- a conversation context

Connections represent co-occurrence, influence, or repeated association.

Examples:

- `timeline` connected to `Adult clarity`
- `no no` connected to `compressed correction`
- `thanks` connected to `Nurturing Parent`
- `Giulio` connected to `peer / lateral influence`
- `Letizia` connected to `direct report / delegation quality`
- `Evelina` connected to `boss / upward communication`
- `Adult` connected to `resolution orientation`
- `Critical Parent edge` connected to `abrupt correction`
- `pricing` connected to `strategic effectiveness`

## Primary design direction

Make the first screen astonishing.

Use:

- dark cinematic background
- glowing 3D nodes
- animated curved edges
- depth of field
- subtle particle field
- smooth camera orbit
- hover glow
- click-to-focus behavior
- elegant glassmorphism panels
- premium typography
- minimal neon accents
- refined motion, not gimmicky motion

The experience should feel like exploring a living behavioral map.

## Technical stack

Use:

- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- Framer Motion
- React Three Fiber or three.js for 3D
- Recharts, Visx, or ECharts for standard charts

Use mock data first, but structure the app so it can later consume Google Sheets or JSON exports.

## Pages and sections

### 1. Hero: 3D Behavioral Constellation

A full-screen interactive 3D graph.

Features:

- Node types have different shapes, sizes, and colors.
- Node size reflects frequency or importance.
- Edge thickness reflects strength of relationship.
- Filters for:
  - time range
  - person
  - role relationship
  - ego state
  - behavior type
  - score band
- Click a node to open an insight panel.
- Click a person to show associated communication patterns.
- Click an ego state to show related phrases, scores, and trend changes.
- Click a behavior to show examples and recommendations.

Node categories:

- Words / phrases
- Behaviors
- Ego states
- People
- Role relationships
- Scores
- Risks
- Strengths
- TA games

Example node styling:

- Adult: calm blue-white glow
- Nurturing Parent: warm gold glow
- Critical Parent edge: sharp red-orange glow
- Adapted Child: muted violet glow
- Direct reports: green halo
- Peers: cyan halo
- Boss: magenta halo
- Strength patterns: bright stable nodes
- Risk patterns: pulsing warning nodes

### 2. Executive Summary Panel

Show:

- current overall score
- weekly change
- strongest current behavior
- weakest current behavior
- dominant ego state
- most improved dimension
- highest-risk relationship context
- top recommendation

Use large numeric cards with subtle animated counters.

### 3. Daily Trend Dashboard

Charts:

- overall score over time
- meaningful replies per day
- strong / solid / watch reply distribution
- Adult-state clarity over time
- emotional regulation over time
- directness over time
- resolution orientation over time

### 4. Transactional Analysis View

Charts:

- ego-state distribution over time
- transaction type distribution
- complementary vs crossed-risk trend
- detected game patterns over time
- role-specific ego-state distribution

Include a visual PAC triangle:

- Parent
- Adult
- Child

Make it interactive:

- Click each section to filter charts and reveal examples.

### 5. Relationship Context View

Show communication quality by relationship type:

- direct subordinates
- peers from different departments
- boss
- other

Role rules:

- Alessandro, Massimiliano, Letizia are direct subordinates.
- Giulio and Francesca are peers from different departments.
- Evelina is the boss.

For direct subordinates, emphasize:

- leadership clarity
- delegation quality
- psychological safety
- coaching
- accountability

For peers, emphasize:

- lateral influence
- negotiation
- alignment
- boundary clarity
- cross-functional clarity

For boss, emphasize:

- upward communication
- concision
- escalation quality
- decision framing
- ownership

Charts:

- average score by relationship type
- score trend by person
- strongest pattern by person
- weakest pattern by person
- communication risk by role context

### 6. Behavior Pattern Explorer

An interactive table/card grid of recurring behaviors.

Each behavior card includes:

- behavior name
- short description
- linked phrases
- linked people
- linked ego state
- score impact
- frequency trend
- recommended Adult-state rewrite

Example behaviors:

- Fast operational alignment
- Compressed correction
- Supportive closure
- Clear commercial framing
- Abrupt negation
- Delegation clarity
- Lateral negotiation
- Upward escalation

### 7. Word to Behavior Map

Show how words or phrases cluster into behaviors.

Examples:

- `ok`, `perfetto`, `vai` -> action closure
- `no no`, `non quello`, `dimentica` -> compressed correction
- `grazie`, `buon lavoro`, `ci sono` -> supportive repair
- `timeline`, `tempistiche`, `oggi` -> operational clarity

Use an interactive Sankey or force-directed graph below the 3D hero.

### 8. Recommendations Engine

Show personalized recommendations:

- one high-impact habit for tomorrow
- one phrase to avoid or soften
- one Adult-state template to use
- one relationship-specific recommendation

Example:

> Before correcting a direct report, state the objective first, then the clarification, then the next step.

Use the format:

```text
Objective -> Clarification -> Next Step
```

### 9. Data / Admin View

A practical section for import/export and debugging.

Support mock data shaped like:

```json
{
  "date": "2026-06-03",
  "conversation_id": "abc123",
  "person": "Letizia Montemurro",
  "relationship": "direct_subordinate",
  "dominant_ego_state": "Adult",
  "secondary_ego_state": "Nurturing Parent",
  "transaction_type": "complementary",
  "possible_game_detected": false,
  "game_pattern": "",
  "adult_state_clarity": 8.5,
  "emotional_regulation": 8,
  "directness": 8,
  "respectfulness": 8.5,
  "accountability": 7.5,
  "boundary_setting": 7,
  "curiosity": 7,
  "concision": 8,
  "strategic_effectiveness": 8.5,
  "conflict_deescalation": 8,
  "resolution_orientation": 8.5,
  "overall_score": 8.1,
  "phrases": ["perfetto", "per qualsiasi cosa ci sono"],
  "behaviors": ["supportive closure", "delegation clarity"],
  "strength_flags": ["clear next step"],
  "risk_flags": []
}
```

Mock dataset:

Create at least 60 mock records across 30 days so the dashboard feels alive.

Include realistic variation across:

- direct reports
- peers
- boss
- Adult
- Nurturing Parent
- Critical Parent edge
- crossed-risk moments
- strong / solid / watch score bands

## Design requirements

- Fully responsive.
- Desktop-first, but usable on tablet.
- Keep 3D performance smooth.
- Provide reduced-motion fallback.
- Use accessible contrast.
- Do not make charts look generic.
- Use elegant empty states.
- Use tooltips with clear explanations.
- Use a persistent filter bar.
- Use a timeline scrubber for the 3D graph.
- Use a focus mode when clicking a node.

## Interaction details

- Hovering a node highlights nearest connected nodes.
- Clicking a node freezes the camera and opens a side panel.
- Double-clicking a node filters the entire dashboard.
- Timeline scrubber animates the constellation across days.
- Relationship filter changes node halos.
- Ego-state filter changes graph color emphasis.
- Standard charts below should update when filters change.

## Visual inspiration

Aim for the level of polish found in high-end interactive data journalism, WebGL portfolio sites, and premium analytics products.

Think:

- Observable-style exploratory data
- narrative data visualization
- Apple-like motion restraint
- Bloomberg-style information density
- cybernetic / constellation / neural-network visual language

Do not copy any specific site. Create an original interface.

## Homepage layout

1. Fullscreen 3D constellation hero.
2. Floating executive summary glass panel.
3. Timeline scrubber at bottom.
4. Scroll down into standard analytical dashboard.
5. End with recommendation cards and data table.

## Tone

The product should feel intelligent, precise, and slightly futuristic.

Avoid therapy cliches.
Avoid generic HR-dashboard aesthetics.
This is a performance analytics tool for communication behavior.

## Deliverables

- Build the full frontend.
- Include mock data.
- Include reusable data schema.
- Include reusable components.
- Include clear comments where live Google Sheets or API data can be connected later.
- Include a README section explaining how to replace mock data with real JSON.
- Make the design visually impressive immediately on first load.

## App title

**Behavioral Constellation**

## Tagline

Map the hidden structure of your communication.
