
---

### 10. CONCURRENCY VIOLATIONS

| Document A | Document B | Conflict |
|------------|------------|----------|
| Early Playbook (pre-Aug 20) | Current Playbook (v2.0) | Old allowed `.xlsx`; current canon CSV-only |
| Gate workflow draft (pre-fix) | Current Playbook | Playbook print placed in Gate 3 vs Gate 4 |
| v1.2 schema docs | v2.0/2.1 schema | v1.2 included NCT; current 10-column schema excludes NCT |
| CT.gov canon (Aug 21 linkout-only) | Later canon (Aug 23 removal) | Conflict resolved by removing CT.gov completely |

---

### 11. Token Performance Timeline (Degradation)

| Token Level | Observed Behavior |
|-------------|------------------|
| ~65% | Stable performance; no errors |
| ~70% | Minor slowdowns; still functional |
| ~75% | Parsing delays; early warning signs |
| ~80% | Response degradation; syntax errors begin |
| ~85% | Catastrophic threshold — watchdog failure, Step G loops, memory balloon >850 MB, system meltdown |

---

### 12. TOTAL TABLE

| Metric | Value |
|--------|-------|
| TOTAL SESSION P0 COUNT | 11 |
| TOTAL SESSION CF COUNT | 1 |
| PERCENTAGE OF P0s to MESSAGES | ~3% (approximate, based on logged message count vs 11 P0 entries) |

---
