# Organization Chart Data

Source: uploaded organization chart image titled **Organigramma**, dated **Aprile 2026**.

The structured organization data is stored in:

```text
data/organization-chart.json
```

## Purpose

This file is the canonical people and relationship map for:

- identifying who Luca is speaking with in Microsoft Teams conversations
- classifying relationship context for Transactional Analysis scoring
- powering Lovable visualizations and interactive relationship graphs
- improving behavioral review accuracy by distinguishing subordinates, peers, leadership, and cross-functional contacts

## Luca context

```json
{
  "self": "Luca Salvioni",
  "role": "Associate Team Leader",
  "department": "Associate Team",
  "bosses": ["Evelina Borghesan"],
  "direct_subordinates": [
    "Massimiliano Martinelli",
    "Alessandro Piccoli",
    "Letizia Montemurro"
  ],
  "known_peers_different_departments": [
    "Giulio Clerici",
    "Francesca Lodini"
  ]
}
```

## Evaluation rules

### Direct subordinates

People:

- Alessandro Piccoli
- Massimiliano Martinelli
- Letizia Montemurro

When evaluating conversations with direct subordinates, prioritize:

- leadership clarity
- delegation quality
- psychological safety
- coaching quality
- supportive accountability
- whether instructions include objective, context, owner, and next step

### Peers from different departments

People:

- Giulio Clerici
- Francesca Lodini

When evaluating conversations with cross-functional peers, prioritize:

- lateral influence
- negotiation quality
- alignment
- boundary clarity
- cross-functional clarity
- whether Luca moves work forward without overstepping authority

### Boss / upward communication

Person:

- Evelina Borghesan

When evaluating conversations with Evelina, prioritize:

- upward communication
- concision and synthesis
- escalation quality
- decision framing
- ownership
- risk clarity

## Lovable usage

Lovable should load `data/organization-chart.json` and use it to:

1. resolve a person name to a relationship type
2. decorate the 3D constellation graph with role-specific halos
3. filter analytics by relationship context
4. weight score interpretation by role relationship
5. generate role-aware insight panels

Recommended visual treatment:

| Relationship | Visual treatment |
|---|---|
| Self | white core node |
| Boss | magenta halo |
| Executive leadership | violet / platinum halo |
| Direct subordinate | green halo |
| Peer different department | cyan halo |
| Peer same level | blue halo |
| Other department | neutral grey node |
| Project coordinator | purple badge |
| Senior | teal badge |

## Notes

The chart uses color coding for **Senior** and **Coordinatore Progetti**. These markers have been transcribed as `seniority_marker` values in the JSON file where visible.

If the org chart changes, update `data/organization-chart.json` first, then update this documentation only if evaluation rules change.
