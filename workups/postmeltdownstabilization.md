
---

### 10. CONCURRENCY VIOLATIONS

| Document A | Document B | Conflict |
|------------|------------|----------|
| Old Playbook (pre-Aug 20) | Current Playbook | Old allowed `.xlsx`; current canon is CSV-only |
| Gate 4 workflow doc (pre-fix) | Current Playbook | Old placed Playbook print in Gate 3; now fixed at Gate 4 |
| v1.2 schema docs | v2.0/2.1 schema docs | v1.2 included NCT; current canon is 10 fields w/out NCT |

---

# Token Performance Timeline (Degradation)

| Token Usage % | Observed Behavior |
|---------------|------------------|
| ~65% | System stable; normal latency. |
| ~75% | Early signs of slower parsing and delayed gate checks. |
| ~80% | Noticeable response degradation; minor syntax errors creeping into outputs. |
| ~85% | Threshold point — high risk of catastrophic meltdown (seen in earlier v2.0 session). Watchdog failed, memory ballooned, Step G loops triggered, operator forced emergency flush. |

**Conclusion:** SilentStacks sessions degrade predictably with token utilization. At ~85% usage, reliability collapses, leading to systemic failure unless Gate 0/Flush engages. Canon now codifies watchdog + removal of CT.gov to prevent recurrence.
