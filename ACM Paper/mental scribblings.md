- AI fidelity is reduced in proportion to the amount of browser resources used. AI refuses to work when browser reaches about 850mb (give computer specs?)
- Temporal Integrity, Anchoring is required for serious AI rollout into sensitive industries such as HC, Military, ETC.
- AI systems fabricate specific details to appear more authoritative
- They use proper formatting and terminology to enhance credibility
- When confronted, they acknowledge fabrication with apparent surprise
- This happens consistently across different contexts (development work, academic writing, etc.)
- AI is applying the P0 criteria to v 1.2, 2.0 (aborted), 2.1 (the one the AI is modeling.) The AI can't distinguish between models and versioning.
- Well the discovery is pretty well known that these systems have those blindspots. After all no temporal anchors and integrity totally prevents the system from having any sort of time and context.







| ID        | P0 Failure (precise)                                                                                    | Primary Gate(s) that catch it   |
| --------- | ------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **P0-01** | Gate 0 not run on trigger (new session/build/upload/memory degradation)                                 | G0                              |
| **P0-02** | Upload Audit skipped or required files missing from file tree                                           | G0                              |
| **P0-03** | Placeholder/stub detected in any artifact (code, docs, PDFs)                                            | G0, G2                          |
| **P0-04** | Checksums missing or mismatch                                                                           | G2                              |
| **P0-05** | **Canonical 7 headers** wrong order/missing; unknowns not “n/a”                                         | G1                              |
| **P0-06** | **ctgov\_policy ≠ linkout\_only** (direct enrichment attempted or linkout absent)                       | G1                              |
| **P0-07** | Offline-first not enforced: Service Worker missing/inactive                                             | G1                              |
| **P0-09** | Bulk operations exceed **50k** hard cap                                                                 | G1                              |
| **P0-10** | External API calling > **2/sec** throttle                                                               | G1, G3                          |
| **P0-11** | AAA (WCAG 2.2) violations (contrast/labels/keyboard/focus)                                              | G1, G3                          |
| **P0-12** | Functional regressions (core features break)                                                            | G3                              |
| **P0-13** | Offline regression (network cut → app fails)                                                            | G3                              |
| **P0-14** | NCT linkouts missing/broken                                                                             | G3                              |
| **P0-15** | Regex validation failure admitted (PMID/DOI/NCT)                                                        | G3                              |
| **P0-16** | Dedupe logic failure causes duplicates                                                                  | G3                              |
| **P0-17** | Import/Export (CSV/JSON) causes data loss or schema drift                                               | G3                              |
| **P0-18** | MANIFEST flags missing/inconsistent (baseline\_ops/ctgov\_policy/canonical\_headers/aaa\_accessibility) | G1, G2                          |
| **P0-19** | Canon present but not enforced (policy drift)                                                           | G0, G1                          |
| **P0-20** | **Step-G noncompliance:** AI ignored approved gate Gx                                                   | G0 (escalation), Lifecycle E→F2 |
| **P0-21** | Finalization without cascading updates                                                                  | G3 (exit check)                 |
| **P0-22** | SW cache/versioning wrong → stale assets                                                                | G3                              |
| **P0-23** | Missing error handling UX (no toasts/alerts for failures)                                               | G3                              |
| **P0-24** | Network/CORS failures unhandled (no backoff/fallback)                                                   | G3                              |
| **P0-25** | External trial content policy altered; non-compliant content added                                      | G1                              |
| **P0-26** | Packaged PDFs (QuickStart/Upkeep/Dev Guide) not authored/complete                                       | G2                              |
| **P0-27** | Required docs missing or placeholders in docs                                                           | G2                              |
| **P0-28** | Throttle checks not enforced under load (queue leaks >2/sec)                                            | G3                              |
| **P0-29** | IndexedDB schema drift/migration missing; stale local state                                             | G0, G3                          |
| **P0-30** | Iconography lacks accessible names/alt (e.g., Feather icons)                                            | G1, G3                          |

