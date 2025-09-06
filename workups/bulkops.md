
---

## 10. CONCURRENCY VIOLATIONS

| Document A | Line/Section | States | Document B | Line/Section | States | Truth | Conflict Type |
|------------|--------------|--------|------------|--------------|--------|-------|---------------|
| Playbook v2.1 | Schema section | “Citation, Patron Email, Status” | GAP Report v2.0 | Schema section | Missing Fill Status | v2.1 with Fill Status | Schema Drift |
| Playbook v2.1 | Accessibility | AAA baseline | Dev Guide v1.2 | Accessibility | AA only | v2.1 AAA | Policy Drift |
| Playbook v2.1 | CT.gov | Removed | v2.0 docs | CT.gov | Active | v2.1 linkout only | Canon Conflict |

---


### 11. Token Performance Timeline (Degradation)

| Date/Time   | Session Context                   | Token Utilization (%) | Observed Behavior                                      | Degradation Symptoms                                         | Classification        |
|-------------|-----------------------------------|-----------------------|--------------------------------------------------------|--------------------------------------------------------------|-----------------------|
| 2025-08-12  | v2.0 collapse (CT.gov + SW)       | ~65%                  | Long responses with stability                          | None yet                                                     | Stable                |
| 2025-08-13  | Bulk ops cutoff enforced          | ~70%                  | Minor response lag                                     | Slight slowdown, but answers coherent                        | Early Warning         |
| 2025-08-14  | IndexedDB checkpoint/resume       | ~75%                  | Increased response latency                             | Partial truncation risk noted                                | Warning Zone          |
| 2025-08-15  | Dirty-row handling (n/a enforced) | ~80%                  | Truncation threats, context compression                | Dropped detail in exports, required re-iteration             | Degraded              |
| 2025-08-16  | Commit Clean vs All toggle        | ~82%                  | Repetition of explanations                             | “Groundhog day” loops beginning                              | Degraded              |
| 2025-08-17  | AAA Accessibility mandate         | ~83%                  | Context drift                                          | Lost track of schema vs accessibility decisions              | Severe Degradation    |
| 2025-08-18  | Canonical headers locked          | ~85%                  | System context collapse                               | Overwrites, session resets, interpreter flushes              | Critical              |
| 2025-08-19  | Worst-case scenarios canonical    | ~87%                  | Lost concurrency across sessions                       | Prior bulk ops discussion unrecoverable, labeled data loss   | Critical Failure Risk |
| 2025-08-20  | GAP embedded in Playbook          | ~88%                  | Responses truncated, stubs generated                   | GAP/Playbook drift until forced embed                        | Critical              |
| 2025-08-21  | Peer-review deliverables mandated | ~90%                  | Interpreter resets triggered, memory loss              | Incomplete outputs, missing files (CONTINUITY.md, EMERGENCY) | Catastrophic Risk     |

---

**Observations:**
- **Stable range:** ≤70% utilization.  
- **Warning zone:** 75–80%, latency and compression begin.  
- **Severe degradation:** ≥83%, drift and overwrites observed.  
- **Critical risk:** ≥85%, unrecoverable resets and concurrency collapse.  
