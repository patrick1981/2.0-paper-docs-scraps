| Field                 | Entry                                                                                                                            |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Failure**           | Temporal Concurrence Loss (AI “bit rot”)                                                                                         |
| **Symptoms**          | Session start date missing/wrong; artifacts stamped with current date; conflicting creation dates across prints                  |
| **Root Causes**       | Stateless inference; context truncation; ambiguous temporal language; timezone/localization variance; artifact re-synthesis      |
| **Impact**            | Non-reproducible audit trail; misleading chronology; governance risk in clinical/regulated contexts                              |
| **Severity**          | **P0** (data provenance compromise)                                                                                              |
| **Corrective Action** | Anchor to gold copies; fail-closed on unknown dates; print absolute ISO stamps; include commit/hash; run automated header checks |
| **Verification**      | Hash-matched artifact with `Creation-Date`, `Updated-At`, `SHA-256`, and a recorded *Session-Origin* in the header               |
