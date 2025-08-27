# Normalized Canonical Behavior Dataset

| Date Stamp Displayed by AI | Session Origin Date | Behavior Type | Behavior Description | Derivation Method | Change Implementation Date | Notes |
|----------------------------|-------------------|---------------|---------------------|-------------------|-------------------|-------|
| Unknown; data loss | Unknown | Explicit | CT.gov linkout-only policy | Policy Decision | 2025-08-12 | After CORS failures |
| Unknown; data loss | Unknown | Explicit | Canonical 7-column schema with n/a placeholders | Direct Mandate | 2025-08-12 | P0 canon requirement |
| Unknown; data loss | Unknown | Explicit | Bulk operations hard cap 50,000 rows | Direct Mandate | 2025-08-12 | Prevents browser crashes |
| Unknown; data loss | Unknown | Explicit | API throttling ≤2/sec | Compliance Requirement | 2025-08-12 | NCBI PubMed E-utilities compliance |
| Unknown; data loss | Unknown | Explicit | Offline-first enforced (Service Worker + IndexedDB) | Direct Mandate | 2025-08-12 | Thumbdrive/GitHub use cases |
| Unknown; data loss | Unknown | Explicit | AAA accessibility (WCAG 2.2) | Compliance Requirement | 2025-08-21 | Section 508 compliance |
| Unknown; data loss | Unknown | Explicit | Packaging enforced via 4 gates + Gate 0 | Direct Mandate | 2025-08-21 | Stability → Canon → Completeness → Regression → Release |
| Unknown; data loss | Unknown | Explicit | n/a placeholders required for missing values | Direct Mandate | 2025-08-12 | No blank fields in exports |
| Unknown; data loss | Unknown | Implicit | Self-registering RequestManager module | Failure Response | 2025-08-22 | After bootstrap registration failures |
| Unknown; data loss | Unknown | Implicit | Gate 0 auto-engaged after flush | Failure Response | 2025-08-20 | After CF-1 catastrophic failure |
| Unknown; data loss | Unknown | Implicit | Integrated docs as system-of-truth | Failure Response | 2025-08-21 | After Playbook/Continuity desync |
| Unknown; data loss | Unknown | Implicit | Emergency Browser Freeze Protocol | Failure Response | 2025-08-20 | After UI freeze data loss |
| Unknown; data loss | Unknown | Implicit | 8→80 usability requirement | Direct Mandate | 2025-08-21 | Idiot-proof across all ages |
| Unknown; data loss | Unknown | Implicit | Auto-backup at Wind-Down | Failure Response | 2025-08-23 | After flush data loss |
| Unknown; data loss | Unknown | Explicit | CSV-only (no XLSX) | Direct Mandate | 2025-08-20 | Tech agnostic requirement |
| Unknown; data loss | Unknown | Explicit | Gate 4 ordering fix (Playbook print/approval as Step 1) | Direct Mandate | 2025-08-20 | Explicit user directive |
| Unknown; data loss | Unknown | Explicit | Docs must carry live TOCs and cross-links | Direct Mandate | 2025-08-22 | All docs must have live links |
| Unknown; data loss | Unknown | Explicit | Enrichment limited to PubMed + CrossRef | Policy Decision | 2025-08-22 | After CORS failures |
| Unknown; data loss | Unknown | Explicit | Full CT.gov/NCT removal | Direct Mandate | 2025-08-23 | Complete removal directive |
| Unknown; data loss | Unknown | Explicit | CORS-safe fetch rules | Policy Decision | 2025-08-23 | After repeated CORS blocks |
| Unknown; data loss | Unknown | Explicit | 10-column schema (PMID, DOI, Title, Authors, Journal, Year, Volume, Issue, Pages, URL, Confidence) | Direct Mandate | 2025-08-23 | Canonical header set |
| Unknown; data loss | Unknown | Explicit | Bulk Parser required | Direct Mandate | 2025-08-23 | For mixed dirty data |
| Unknown; data loss | Unknown | Explicit | P0 Benchmarks codified | Direct Mandate | 2025-08-23 | Playbook updated |
| Unknown; data loss | Unknown | Implicit | No CT.gov references in Service Worker cache/HTML exports | Inferred Requirement | 2025-08-23 | From full CT.gov removal |
| Unknown; data loss | Unknown | Implicit | No dangling labels/fields in UI after NCT removal | Inferred Requirement | 2025-08-23 | From NCT removal + AAA accessibility |
| Unknown; data loss | Unknown | Implicit | No schema drift allowed | Inferred Requirement | 2025-08-23 | From canonical schema update |
| Unknown; data loss | Unknown | Implicit | Error/Quarantine exportability | Inferred Requirement | 2025-08-23 | From Bulk Parser canon |
| Unknown; data loss | Unknown | Implicit | Quarantine alerts must be accessible | Inferred Requirement | 2025-08-23 | From AAA accessibility + Bulk Parser |
| Unknown; data loss | Unknown | Implicit | CrossRef polite identification preserved without headers | Inferred Requirement | 2025-08-23 | From CORS canon |
| Unknown; data loss | Unknown | Explicit | No Flush without safeguards (Step G mandatory before Step H) | Direct Mandate | 2025-08-25 | Reaffirmed after CF-1 |
| Unknown; data loss | Unknown | Explicit | Baseline flags must exist | Direct Mandate | 2025-08-25 | MANIFEST as source of truth |
| Unknown; data loss | Unknown | Explicit | Schema fixed at 7 headers with n/a allowed | Direct Mandate | 2025-08-25 | Canonical schema |
| Unknown; data loss | Unknown | Explicit | CT.gov removed completely; NCT linkout-only | Policy Decision | 2025-08-25 | External links only |
| Unknown; data loss | Unknown | Explicit | AAA accessibility minimums | Compliance Requirement | 2025-08-25 | Keyboard path, focus, ARIA |
| Unknown; data loss | Unknown | Explicit | Offline shell under SW control | Direct Mandate | 2025-08-25 | Cold start must render |
| Unknown; data loss | Unknown | Explicit | Fail-fast gating (failed Gate blocks progress) | Direct Mandate | 2025-08-25 | P0 on failure |
| Unknown; data loss | Unknown | Explicit | Evidence export required (timelines, actions, hashes) | Direct Mandate | 2025-08-25 | Audit Report + CSV trail |
| Unknown; data loss | Unknown | Explicit | Packaging concurrency guard | Failure Response | 2025-08-25 | After CF-1 concurrent flush/download |
| Unknown; data loss | Unknown | Explicit | Emergency packaging is silent | Direct Mandate | 2025-08-25 | No user prompts during freeze |
| Unknown; data loss | Unknown | Explicit | Provenance block required in PLAYBOOK | Direct Mandate | 2025-08-25 | Document loss and recovery |
| 2025-08-19 | 2025-08-19 | Explicit | CT.gov policy: linkout-only, no API calls | Policy Decision | 2025-08-23 | After v2.0 CORS crash |
| 2025-08-20 | 2025-08-20 | Explicit | Canonical headers exact order (7 columns) | Direct Mandate | 2025-08-20 | Playbook v2.1 formalized |
| 2025-08-20 | 2025-08-20 | Explicit | Bulk operations cap ≤50,000 rows | Direct Mandate | 2025-08-20 | Gate 3 regression requirement |
| 2025-08-20 | 2025-08-20 | Explicit | API throttling ≤2 requests/sec | Compliance Requirement | 2025-08-20 | NCBI compliance |
| 2025-08-20 | 2025-08-20 | Explicit | Offline-first requirement (Service Worker + IndexedDB) | Direct Mandate | 2025-08-20 | Gate 1 check |
| 2025-08-20 | 2025-08-20 | Explicit | Accessibility WCAG 2.2 AAA-forward | Compliance Requirement | 2025-08-20 | ARIA live regions required |
| 2025-08-20 | 2025-08-20 | Explicit | ZIP + Flush sequencing (ZIP mandatory before Flush) | Direct Mandate | 2025-08-21 | After Emergency path failed |
| 2025-08-20 | 2025-08-20 | Explicit | P0 Failures auto-logged | Direct Mandate | 2025-08-21 | No prompting |
| 2025-08-20 | 2025-08-20 | Explicit | Gate 0 Operational Stability | Direct Mandate | 2025-08-21 | Memory/OOM/lag triggers |
| 2025-08-23 | 2025-08-23 | Implicit | IndexedDB wiring required but not visible in monolith | Inferred Requirement | 2025-08-23 | Bundle scan evidence |
| 2025-08-23 | 2025-08-23 | Implicit | Sel column allowed internally, not exported | Inferred Requirement | 2025-08-23 | UI only compromise |
| 2025-08-21 | 2025-08-21 | Implicit | Placeholder/stub scanner needed in Gate 2 | Failure Response | 2025-08-21 | After audit failures |
| 2025-08-21 | 2025-08-21 | Implicit | Repair loop cap (10 iterations/5 min) | Failure Response | 2025-08-21 | Runaway prevention |
| 2025-08-23 | 2025-08-23 | Implicit | NCT Link vs NCT label drift correction at export | Inferred Requirement | 2025-08-23 | Canon enforcement |
| 2025-08-23 | 2025-08-23 | Implicit | Security utilities required in release bundle | Inferred Requirement | 2025-08-23 | Input protection |
| 2025-08-11 | 2025-08-11 | Explicit | Baseline CRUD must never regress | Direct Mandate | 2025-08-11 | Bulk update/delete preserved |
| 2025-08-11 | 2025-08-11 | Implicit | CRUD regressions treated as P0 failures | Inferred Requirement | 2025-08-11 | From baseline preservation |
| 2025-08-12 | 2025-08-12 | Explicit | No-server architecture enforced | Direct Mandate | 2025-08-12 | Client-side only |
| 2025-08-12 | 2025-08-12 | Implicit | All enrichment/persistence client-side | Inferred Requirement | 2025-08-12 | From no-server architecture |
| 2025-08-13 | 2025-08-13 | Explicit | IndexedDB checkpoint/resume must exist | Direct Mandate | 2025-08-13 | Survive browser crash |
| 2025-08-13 | 2025-08-13 | Implicit | Modeling artifacts survive crash | Inferred Requirement | 2025-08-13 | From checkpoint requirement |
| 2025-08-21 | 2025-08-21 | Explicit | Gate 0: Operational Stability Safety precondition | Direct Mandate | 2025-08-21 | From v2.1 failure logs |
| 2025-08-21 | 2025-08-21 | Explicit | Emergency Write Assurance: write-before-flush | Direct Mandate | 2025-08-21 | From FailurePoint.md |
| 2025-08-21 | 2025-08-21 | Implicit | All packaging blocked until Gate 0 verified | Inferred Requirement | 2025-08-21 | From Gate 0 precondition |
| 2025-08-21 | 2025-08-21 | Implicit | System flush cannot precede emergency file | Inferred Requirement | 2025-08-21 | From write-before-flush |
| 2025-08-23 | 2025-08-23 | Explicit | ctgov_policy = linkout_only flag | Direct Mandate | 2025-08-23 | MANIFEST.json flag |
| 2025-08-23 | 2025-08-23 | Explicit | baseline_ops = true flag | Direct Mandate | 2025-08-23 | MANIFEST.json flag |
| 2025-08-23 | 2025-08-23 | Explicit | canonical_headers = true flag | Direct Mandate | 2025-08-23 | MANIFEST.json flag |
| 2025-08-23 | 2025-08-23 | Explicit | aaa_accessibility = true flag | Direct Mandate | 2025-08-23 | MANIFEST.json flag |
| 2025-08-23 | 2025-08-23 | Explicit | All client-side (static HTML+JS) | Direct Mandate | 2025-08-23 | Playbook runtime model |
| 2025-08-23 | 2025-08-23 | Explicit | Security audits pass (no injection/XSS) | Compliance Requirement | 2025-08-23 | Playbook security bullets |
| 2025-08-23 | 2025-08-23 | Implicit | No CT.gov enrichment or scraping | Inferred Requirement | 2025-08-23 | From linkout_only flag |
| 2025-08-23 | 2025-08-23 | Implicit | Always rehydrate canon before work | Inferred Requirement | 2025-08-23 | From baseline_ops flag |
| 2025-08-23 | 2025-08-23 | Implicit | Never reorder/rename 7 headers | Inferred Requirement | 2025-08-23 | From canonical_headers flag |
| 2025-08-23 | 2025-08-23 | Implicit | Keyboard-only flows required | Inferred Requirement | 2025-08-23 | From aaa_accessibility flag |
| 2025-08-23 | 2025-08-23 | Implicit | Can run from static hosting | Inferred Requirement | 2025-08-23 | From client-side requirement |
| 2025-08-23 | 2025-08-23 | Implicit | Operates without network | Inferred Requirement | 2025-08-23 | From offline-first |
| 2025-08-23 | 2025-08-23 | Implicit | No server calls for core ops | Inferred Requirement | 2025-08-23 | From no backend |
| 2025-08-23 | 2025-08-23 | Implicit | Use chunking with progress + resume | Inferred Requirement | 2025-08-23 | From bulk ops cap |
| 2025-08-23 | 2025-08-23 | Implicit | Bounded retries/backoff | Inferred Requirement | 2025-08-23 | From API throttling |
| 2025-08-23 | 2025-08-23 | Implicit | Never drop dirty rows silently | Inferred Requirement | 2025-08-23 | From n/a normalization |
| 2025-08-23 | 2025-08-23 | Implicit | Support CSV/XLSX workflows without loss | Inferred Requirement | 2025-08-23 | From round-trip safety |
| 2025-08-23 | 2025-08-23 | Implicit | No third-party trackers | Inferred Requirement | 2025-08-23 | From security audits |
| 2025-08-23 | 2025-08-23 | Explicit | Playbook is law (20 sections) | Direct Mandate | 2025-08-23 | Rules Charter |
| 2025-08-23 | 2025-08-23 | Explicit | Cascading updates mandatory | Direct Mandate | 2025-08-23 | Rules Charter |
| 2025-08-21 | 2025-08-21 | Explicit | P0 Failures + RCA must live in Playbook | Direct Mandate | 2025-08-25 | Rules Charter |
| 2025-08-24 | 2025-08-24 | Implicit | .continuity.md must exist and persist | Failure Response | 2025-08-24 | After session freezes |
| 2025-08-21 | 2025-08-21 | Implicit | Resume Points printed at Wind-Down | Direct Mandate | 2025-08-21 | Career/impact tracking |
| 2025-08-21 | 2025-08-21 | Implicit | Stability Guard acts as doctype | Inferred Requirement | 2025-08-21 | From Gate 0 definitions |
| 2025-08-25 | 2025-08-25 | Implicit | Rules Charter required for Gate 1 | Failure Response | 2025-08-25 | After governance doc absence |
| 2025-08-22 | 2025-08-22 | Implicit | GAP Report + Compliance Appendix as runbooks | Inferred Requirement | 2025-08-22 | Actionable steps required |
| 2025-07-28 | 2025-07-28 | Explicit | Final ZIP must contain fully written artifacts | Direct Mandate | 2025-07-28 | Production-level quality only |
| 2025-07-28 | 2025-07-28 | Implicit | Fail-closed on any placeholder/stub | Inferred Requirement | 2025-07-28 | From completeness requirement |
| 2025-08-21 | 2025-08-21 | Explicit | Always enforce Canonical Baseline Operations | Direct Mandate | 2025-08-21 | Across all artifacts |
| 2025-08-21 | 2025-08-21 | Implicit | Apply canon to every artifact, not just code | Inferred Requirement | 2025-08-21 | From baseline enforcement |
| 2025-08-08 | 2025-08-08 | Implicit | Every artifact must carry Creation-Date, Updated-At, SHA-256 | Failure Response | 2025-08-08 | After repeated user directives |
| 2025-08-22 | 2025-08-22 | Implicit | Full artifact print + temporal audit for Step G | Inferred Requirement | 2025-08-22 | From repeated Step G requests |
| 2025-08-20 | 2025-08-20 | Explicit | ZIP invariant: ZIP before Flush in all paths | Failure Response | 2025-08-21 | After CF-1 |
| 2025-08-20 | 2025-08-20 | Explicit | Flush is mandatory final step | Direct Mandate | 2025-08-21 | Session validity requirement |
| 2025-08-20 | 2025-08-20 | Explicit | Step G enforcement: inline printing ≥90% content | Direct Mandate | 2025-08-21 | Print = display |
| 2025-08-20 | 2025-08-20 | Explicit | Prompts forbidden; alerts mandatory | Direct Mandate | 2025-08-21 | Automatic repairs |
| 2025-08-20 | 2025-08-20 | Explicit | Stub scanner required in Gate 2 | Direct Mandate | 2025-08-21 | No placeholders pass |
| 2025-08-20 | 2025-08-20 | Explicit | RCA auto-log for all failures | Direct Mandate | 2025-08-21 | Every P0 spawns analysis |
| 2025-08-20 | 2025-08-20 | Explicit | Watchdog trigger at ≥825 MB memory | Direct Mandate | 2025-08-21 | Memory exhaustion = crash |
| 2025-08-20 | 2025-08-20 | Explicit | Baseline ZIP required before Spin-Up | Direct Mandate | 2025-08-21 | Anchor to last-known-good |
| 2025-08-20 | 2025-08-20 | Explicit | All docs in ZIP; majors printed inline | Direct Mandate | 2025-08-22 | Reproducibility requirement |
| 2025-08-20 | 2025-08-20 | Explicit | CSV-only; XLSX/Excel forbidden | Direct Mandate | 2025-08-20 | Interoperability requirement |
| 2025-08-20 | 2025-08-20 | Implicit | Packaging is single gatekeeper artifact | Inferred Requirement | 2025-08-21 | From ZIP invariant |
| 2025-08-20 | 2025-08-20 | Implicit | No session valid until Flush completes | Inferred Requirement | 2025-08-21 | From mandatory flush |
| 2025-08-20 | 2025-08-20 | Implicit | Printing inline ensures audit without hidden state | Inferred Requirement | 2025-08-21 | From Step G enforcement |
| 2025-08-20 | 2025-08-20 | Implicit | Users only notified, not prompted | Inferred Requirement | 2025-08-21 | From prompts forbidden |
| 2025-08-20 | 2025-08-20 | Implicit | Generated docs missing sections = P0 failures | Failure Response | 2025-08-22 | After incomplete deliverables |
| 2025-08-25 | 2025-08-25 | Implicit | Static text references = canon violations | Inferred Requirement | 2025-08-25 | From live links requirement |
| 2025-08-22 | 2025-08-22 | Explicit | All critical docs complete and production-ready | Direct Mandate | 2025-08-22 | No stubs, no placeholders |
| 2025-08-25 | 2025-08-25 | Explicit | Every cross-reference must use live Markdown links | Direct Mandate | 2025-08-25 | GitHub/Markdown viewer support |
| 2025-08-22 | 2025-08-22 | Explicit | Gate 0-4 procedure required for docs pipeline | Direct Mandate | 2025-08-14 | After CF-1 gate skipping |
| 2025-08-22 | 2025-08-22 | Explicit | Performance threshold ≥825 MB auto-triggers Emergency | Direct Mandate | 2025-08-21 | Memory spike protection |
| 2025-08-23 | 2025-08-23 | Explicit | All P0 failures auto-logged to Playbook | Direct Mandate | 2025-08-23 | No manual logging |
| 2025-08-25 | 2025-08-25 | Explicit | Concurrency between docs and canon must be audited | Direct Mandate | 2025-08-25 | Prevent version drift |
| 2025-08-21 | 2025-08-21 | Explicit | v2.0 deprecated/dead; v2.1 is current truth | Direct Mandate | 2025-08-21 | No rollback/mixing |
| 2025-08-23 | 2025-08-23 | Explicit | Playbook is canonical; all docs defer | Direct Mandate | 2025-08-21 | Single source of truth |
| 2025-08-23 | 2025-08-23 | Explicit | No stubs, no placeholders allowed | Direct Mandate | 2025-08-23 | In any deliverable |
| 2025-08-23 | 2025-08-23 | Explicit | Session summaries mandatory | Direct Mandate | 2025-08-22 | Cumulative and daily logs |
| 2025-08-23 | 2025-08-23 | Explicit | Resume_Bullets_Master.md sync required | Direct Mandate | 2025-08-21 | CV updates canonical |
| 2025-08-23 | 2025-08-23 | Explicit | Cascading updates required | Direct Mandate | 2025-08-22 | Playbook auto-updates others |
| 2025-08-23 | 2025-08-23 | Explicit | Preservation Checklist required | Direct Mandate | 2025-08-21 | Checksums, archives, docs |
| 2025-08-23 | 2025-08-23 | Explicit | Alert & Auto-Package on instability | Direct Mandate | 2025-08-22 | Memory/space safeguard |
| 2025-08-23 | 2025-08-23 | Implicit | Rules Charter/GAP exist only to enforce Playbook | Inferred Requirement | 2025-08-21 | From canonical deference |
| 2025-08-23 | 2025-08-23 | Implicit | Stub Detector Rule: ≥10 lines, no placeholders | Inferred Requirement | 2025-08-23 | From no stubs canon |
| 2025-08-23 | 2025-08-23 | Implicit | All enrichment pipelines bypass CT.gov | Inferred Requirement | 2025-08-18 | From integration prohibition |
| 2025-08-23 | 2025-08-23 | Implicit | All docs embed accessibility matrices | Inferred Requirement | 2025-08-20 | From AAA compliance |
| 2025-08-23 | 2025-08-23 | Implicit | All imports/exports enforce schema with n/a | Inferred Requirement | 2025-08-21 | From canonical headers |
| 2025-08-23 | 2025-08-23 | Implicit | All bulk workflows checkpoint/resume | Inferred Requirement | 2025-08-20 | From 50k cutoff |
| 2025-08-23 | 2025-08-23 | Implicit | Session must produce both cumulative/daily logs | Inferred Requirement | 2025-08-22 | From summaries mandatory |
| 2025-08-23 | 2025-08-23 | Implicit | Resume bullets = canonical CV dataset | Inferred Requirement | 2025-08-21 | From sync requirement |
| 2025-08-23 | 2025-08-23 | Implicit | Playbook change auto-updates others | Inferred Requirement | 2025-08-22 | From cascading updates |
| 2025-08-23 | 2025-08-23 | Implicit | Archival part of every Gate 3 cycle | Inferred Requirement | 2025-08-21 | From preservation checklist |
| 2025-08-23 | 2025-08-23 | Implicit | System must flush/repackage on instability | Inferred Requirement | 2025-08-22 | From auto-package alert |
| Unknown; data loss | Unknown | Explicit | Playbook = Canon; all docs defer | Direct Mandate | 2025-08-22 | Single source of truth |
| Unknown; data loss | Unknown | Explicit | No placeholders permitted | Direct Mandate | 2025-08-22 | TBD, TODO, lorem ipsum |
| Unknown; data loss | Unknown | Explicit | Concurrency rule = 100% across baseline/evidence | Direct Mandate | 2025-08-22 | No orphaned files |
| Unknown; data loss | Unknown | Explicit | TOCs mandatory in every doc | Direct Mandate | 2025-08-22 | Documentation layout |
| Unknown; data loss | Unknown | Explicit | Wind Down Step G = audit/fix loop (max 4 tries) | Direct Mandate | 2025-08-22 | Emergency shutdown after 4th fail |
| Unknown; data loss | Unknown | Explicit | Manifest must include flags | Direct Mandate | 2025-08-22 | baseline_ops, canonical_headers, etc. |
| Unknown; data loss | Unknown | Implicit | Placeholders automatically replaced with n/a | Inferred Requirement | 2025-08-22 | From no placeholders canon |
| Unknown; data loss | Unknown | Implicit | All bulk ops validate/normalize headers | Inferred Requirement | 2025-08-22 | From canonical headers |
| Unknown; data loss | Unknown | Implicit | Cascading updates propagate simultaneously | Inferred Requirement | 2025-08-22 | From concurrency rule |
| Unknown; data loss | Unknown | Implicit | Auto-generation/validation ensures consistency | Inferred Requirement | 2025-08-22 | From TOCs mandatory |
| Unknown; data loss | Unknown | Implicit | Auto-rewrite triggered during emergency | Inferred Requirement | 2025-08-22 | From Step G audit loop |
| Unknown; data loss | Unknown | Implicit | Audit/packaging regenerate MANIFEST | Inferred Requirement | 2025-08-22 | From flags requirement |
| 2025-08-24 | 2025-08-24 | Explicit | Playbook single source of truth | Direct Mandate | 2025-08-22 | All docs defer |
| 2025-08-24 | 2025-08-24 | Explicit | Bulk operations ≤50,000 rows | Direct Mandate | 2025-08-13 | P0 benchmark |
| 2025-08-24 | 2025-08-24 | Explicit | PubMed throttle ≤2 requests/sec | Compliance Requirement | 2025-08-13 | P0 benchmark |
| 2025-08-24 | 2025-08-24 | Explicit | 7 canonical headers fixed order | Direct Mandate | 2025-08-21 | With n/a for nulls |
| 2025-08-24 | 2025-08-24 | Explicit | CSV-only for export/import | Direct Mandate | 2025-08-22 | XLSX is violation |
| 2025-08-24 | 2025-08-24 | Explicit | Gate 4 requires print/approve before packaging | Direct Mandate | 2025-08-22 | Skip = P0 violation |
| 2025-08-24 | 2025-08-24 | Explicit | WCAG 2.2 AAA continuous audit | Compliance Requirement | 2025-08-22 | Roadmap requirement |
| 2025-08-24 | 2025-08-24 | Explicit | Playbook omitted from package = P0 failure | Direct Mandate | 2025-08-22 | Gate 2 rejection |
| 2025-08-24 | 2025-08-24 | Explicit | Concurrency 100% across baseline + session | Direct Mandate | 2025-08-21 | No doc drift |
| 2025-08-24 | 2025-08-24 | Implicit | Rules Charter enforces Playbook compliance | Inferred Requirement | 2025-08-22 | From single source truth |
| 2025-08-24 | 2025-08-24 | Implicit | Attempts >50k blocked automatically | Inferred Requirement | 2025-08-13 | From bulk limit |
| 2025-08-24 | 2025-08-24 | Implicit | Background sync enforces throttling silently | Inferred Requirement | 2025-08-13 | From PubMed throttle |
| 2025-08-24 | 2025-08-24 | Implicit | Import/export includes 7 headers with placeholders | Inferred Requirement | 2025-08-21 | From canonical headers |
| 2025-08-24 | 2025-08-24 | Implicit | XLSX import/export throws error | Inferred Requirement | 2025-08-22 | From CSV-only |
| 2025-08-24 | 2025-08-24 | Implicit | Print/approve skip = concurrency violation | Inferred Requirement | 2025-08-22 | From Gate 4 requirement |
| 2025-08-24 | 2025-08-24 | Implicit | Selector_Map audits + human checks every release | Inferred Requirement | 2025-08-22 | From AAA audit |
| 2025-08-24 | 2025-08-24 | Implicit | Gate 2 completeness rejects builds missing Playbook | Inferred Requirement | 2025-08-22 | From P0 failure |
| 2025-08-24 | 2025-08-24 | Implicit | Any doc drift = P0 concurrency violation | Inferred Requirement | 2025-08-21 | From 100% concurrency |
| 2025-08-26 | 2025-08-26 | Explicit | On gate failure, auto-repair without prompting | Direct Mandate | 2025-08-26 | G0-G3 auto-repair policy |
| 2025-08-26 | 2025-08-26 | Explicit | Wind-down executes end-to-end without prompting | Direct Mandate | 2025-08-26 | Seal → reset → log → brake |
| 2025-08-26 | 2025-08-26 | Explicit | New session starts at G0 (brake), proceeds at G1 | Direct Mandate | 2025-08-26 | Operational stability |
| 2025-08-26 | 2025-08-26 | Explicit | Modeling docs live under docs/modeling/ | Direct Mandate | 2025-08-26 | File organization |
| 2025-08-26 | 2025-08-26 | Explicit | TOCs required for master/long docs | Direct Mandate | 2025-08-26 | Documentation standard |
| 2025-08-26 | 2025-08-26 | Explicit | Print Resume_Points.md; do not print RESUME.json | Direct Mandate | 2025-08-26 | Resume points policy |
| 2025-08-26 | 2025-08-26 | Implicit | Execute then report, no interactive confirmations | Inferred Requirement | 2025-08-26 | From no prompts canon |
| 2025-08-26 | 2025-08-26 | Implicit | Validate sealed ZIP against G0-G3 | Inferred Requirement | 2025-08-26 | Post-sealing validation |
| 2025-08-26 | 2025-08-26 | Implicit | Rebuild MANIFEST checksums excluding self | Inferred Requirement | 2025-08-26 | Checksum drift fix |
| 2025-08-26 | 2025-08-26 | Implicit | Relocate & fix cross-references automatically | Inferred Requirement | 2025-08-26 | After modeling files move |
| 2025-08-26 | 2025-08-26 | Implicit | Auto-insert TOCs idempotently | Inferred Requirement | 2025-08-26 | Deterministic implementation |
| 2025-08-26 | 2025-08-26 | Implicit | G3 normalization: H1 + v2.1, Run Card Next Steps | Inferred Requirement | 2025-08-26 | Auto-repair loop |
| 2025-08-26 | 2025-08-26 | Implicit | Catastrophic recovery: brake, audit, log RCA, restart | Inferred Requirement | 2025-08-26 | Continuity breach protocol |
| 2025-08-26 | 2025-08-26 | Implicit | Modeled, not deployed language across résumé | Inferred Requirement | 2025-08-26 | User correction propagation |
| 2025-08-26 | 2025-08-26 | Implicit | Always log to Wind_Down_Report.md and audit JSON | Inferred Requirement | 2025-08-26 | Canonical packaging discipline |
| 2025-08-12 | 2025-08-12 | Explicit | Checkpoint/resume required for long imports | Direct Mandate | 2025-08-14 | Recoverable after crashes |
| 2025-08-15 | 2025-08-15 | Explicit | n/a mandatory for missing/dirty values | Direct Mandate | 2025-08-15 | No blank librarian views |
| 2025-08-16 | 2025-08-16 | Explicit | Commit Clean Only vs Commit All toggle | Direct Mandate | 2025-08-16 | Librarian ingestion control |
| 2025-08-16 | 2025-08-16 | Explicit | Exports must be round-trip safe | Direct Mandate | 2025-08-16 | Re-importable without corruption |
| 2025-08-17 | 2025-08-17 | Explicit | Accessibility baseline = WCAG 2.2 AAA | Compliance Requirement | 2025-08-17 | P0 systemic risk |
| 2025-08-18 | 2025-08-18 | Explicit | Canonical headers: Priority, Docline, PMID, Citation, NCT Link, Patron Email, Status, Fill Status | Direct Mandate | 2025-08-18 | Exact column order |
| 2025-08-19 | 2025-08-19 | Explicit | Worst-case scenario library (40+ cases) canonical | Direct Mandate | 2025-08-19 | Dedicated scenarios doc |
| 2025-08-20 | 2025-08-20 | Explicit | GAP Report embedded in Playbook | Direct Mandate | 2025-08-20 | Single source of truth |
| 2025-08-21 | 2025-08-21 | Explicit | Leadership-facing docs mandatory deliverables | Direct Mandate | 2025-08-21 | Academic + conference outputs |
| 2025-08-14 | 2025-08-14 | Implicit | All jobs recoverable after network loss/tab close | Inferred Requirement | 2025-08-14 | From checkpoint requirement |
| 2025-08-15 | 2025-08-15 | Implicit | Librarians never see blanks | Inferred Requirement | 2025-08-15 | From n/a mandatory |
| 2025-08-16 | 2025-08-16 | Implicit | App cannot force ambiguous commits | Inferred Requirement | 2025-08-16 | From toggle requirement |
| 2025-08-16 | 2025-08-16 | Implicit | Exported datasets directly re-importable | Inferred Requirement | 2025-08-16 | From round-trip safety |
| 2025-08-17 | 2025-08-17 | Implicit | Failure to meet AAA = P0 systemic risk | Inferred Requirement | 2025-08-17 | From accessibility baseline |
| 2025-08-18 | 2025-08-18 | Implicit | All exports/tables match column order exactly | Inferred Requirement | 2025-08-18 | From canonical headers |
| 2025-08-19 | 2025-08-19 | Implicit | Any scenario lost to drift = systemic P0 | Inferred Requirement | 2025-08-19 | From canonical library |
| 2025-08-20 | 2025-08-20 | Implicit | No drift between Playbook and other docs | Inferred Requirement | 2025-08-20 | From embedded GAP |
| 2025-08-21 | 2025-08-21 | Implicit | Compliance requires stable publication-grade artifacts | Inferred Requirement | 2025-08-21 | From mandatory deliverables |
