# SilentStacks Dev Playbook — v2.1 (FULL — DELINEATED)
**Original creation date: 2025-08-23**

## 0. Purpose & Scope
SilentStacks is an offline-first, client-only ILL tracking and metadata enrichment tool for healthcare librarians. This Playbook is the canonical, end-to-end operational manual for development, testing, packaging, deployment, recovery, and wind-down procedures. It supersedes all prior notes where conflicts exist.

---

## 1. Canon (P0 Baseline)
- **CT.gov policy:** Linkout-only (no API calls). Generate `https://clinicaltrials.gov/study/{NCT}` links; do not fetch from `clinicaltrials.gov/api/*`.
- **Headers (exact order):** `Urgency | DOCLINE # | PMID | NLM Citation | NCT Link | Patron E-mail | Fill Status`  
  - Unknowns are `n/a`, never blank.
- **Bulk ops hard cap:** 50,000 rows.
- **Throttling:** ≤ 2 requests/sec across all external lookups.
- **Offline-first:** Service Worker + IndexedDB; no server-side components.
- **Accessibility:** WCAG 2.2 AAA where feasible; at minimum AA with AAA-oriented tokens and contrast.
- **Packaging integrity:** SHA-256 checksums, manifest flags:
  - `baseline_ops`, `ctgov_policy=linkout_only`, `canonical_headers`, `aaa_accessibility`.

---

## 2. Architecture
- **Client-only monolith** (one HTML or HTML+app.min.js) or **modular bundle** (`/modules` + build step).
- **Persistence:** IndexedDB for requests, settings, and queue; localStorage only for ephemeral UI state.
- **Network:** Fetch wrappers enforcing throttling and backoff; Retry-After honored.

---

## 3. Data Model & Validation
- **Request record (canonical fields):**
  - `urgency` (`Urgent|Normal|Low`)
  - `docline_id` (string; unique per request)
  - `pmid` (regex: `^[1-9]\d{0,7}$`)
  - `citation_nlm` (string; normalized)
  - `nct_link` (absolute URL `https://clinicaltrials.gov/study/NCT\d+`)
  - `patron_email` (RFC 5322 subset; institutional domains preferred)
  - `fill_status` (`Pending|Requested|Filled|Rejected|n/a`)
- **Normalization rules:**
  - DOI strings decoded and re-encoded; punctuation trimmed.
  - `n/a` for unknowns; never nulls.
  - Export CSV header order fixed to canonical.

---

## 4. Enrichment (P0)
- **PubMed (E-utilities) & Crossref** only; throttle ≤ 2/sec.
- **CT.gov:** **linkout-only** per canon. Derive NCT IDs from PubMed when available; never call CT.gov API in production.
- **Retry & caching:** Content-hash cache with max-age; respect ETag and Retry-After; exponential backoff.

---

## 5. UI/UX (AAA-forward)
- **Live regions:** `aria-live="polite"` for toasts and validation.
- **Skip links:** `#main` present and first focusable.
- **Keyboard:** All primary actions reachable by Tab; focus rings never suppressed.
- **Contrast tokens:** Dark on light and light on dark with ≥ 7:1 contrast on key text.

---

## 6. Gates (0 → 3)

### Gate 0 — Operational Stability Safety
**Triggers:** memory/space degradation, browser lag spikes, session reset symptoms.  
**Actions (must):**
1. Rehydrate Canonical Baseline Operations.
2. Run Upload Audit (file tree, required presence, placeholder scan).
3. If any failure → **STOP**; collect evidence; do not proceed.

### Gate 1 — Baseline Canon Check
- Verify:
  - CT.gov `linkout_only`.
  - Canonical headers present (UI + export).
  - Throttling configured ≤ 2/sec.
  - Offline-first enabled (SW + IDB wiring).

### Gate 2 — Artifact Completeness & Manifest Audit
- Required files present: `index.html` (or monolith), `app.min.js` (if modular), `style.css`, `service-worker.js`, authored PDFs (QuickStart, Upkeep, Developer Guide).
- Placeholder/stub scanner: block on `TODO|FIXME|LOREM|PLACEHOLDER`.
- Generate MANIFEST:
  - flags: `baseline_ops, ctgov_policy=linkout_only, canonical_headers, aaa_accessibility`
  - per-file SHA-256 checksums.

### Gate 3 — Regression Test Matrix
- **Load stability:** initial render < 2s on mid-tier hardware, cached mode < 1s.
- **Bulk ops:** import 50k CSV with no crash; memory steady-state acceptable; no main-thread stalls > 200ms.
- **Offline/online:** create → offline → modify → online; queued writes flushed; no data loss.
- **Validation:** regexes enforced; bad inputs toasts; exports in canonical order.

---

## 7. Spin-Up & Wind-Down

### Spin-Up
1. Gate 0 baseline.
2. Load dev dataset; enable verbose logs.
3. Verify SW/IDB wiring.
4. Run enrichment smoke with throttling.

### Wind-Down (Performance Degradation or Exit)
1. **ZIP artifacts** (mandatory) → `dist/` with manifest + checksums.
2. **Flush** queues & persist checkpoints.
3. Write incident note if any P0 encountered.
4. Release locks; clear ephemeral caches; keep IDB.

---

## 8. Incident Handling

### P0 Failure Record (template)
- Timestamp:
- Failure:
- Root Cause:
- Corrective Action:
- Evidence Snippet:
- Status: ✅/⏳/❌

**Catastrophic/Systemic (CF)**
- Full timeline, Gate matrix, package hashes, corrective actions, prevention.

---

## 9. Packaging

**Docs bundle must include authored PDFs:**
- QuickStart
- Upkeep
- Developer Guide

**ZIP contents (minimal):**
