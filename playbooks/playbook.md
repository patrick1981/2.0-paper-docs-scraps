---

# 📘 SilentStacks Master Playbook (v2.0 Canon)

**Last updated:** 2025-08-23
**Maintainer:** Project Lead (solo librarian-informatics role)
**Canonical Version:** v2.0 (CT.gov/NCT fully removed; PubMed + CrossRef only)

---

## 0. Purpose

SilentStacks is an **offline-first, browser-based ILL tracking and metadata enrichment tool** for healthcare librarians. It supports **PMID** (PubMed) and **DOI** (CrossRef) enrichment, bulk operations, and exports in a strict canonical format.

---

## 1. Canonical Rules

1. **CSV-only** — no `.xlsx` usage anywhere (enforced at Gate 1).

2. **CORS-safe fetches only** — GET + `Accept`, `credentials:'omit'`.

   * CrossRef contact info must be passed via `?mailto=` query parameter.
   * Forbidden headers (e.g. `User-Agent`) are never set client-side.

3. **PubMed + CrossRef only** — CT.gov/NCT integration permanently removed.

4. **Canonical export schema (10 fields):**

   ```
   PMID | DOI | Title | Authors | Journal | Year | Volume | Issue | Pages | URL | Confidence
   ```

5. **Docs must carry live TOCs + cross-links** — no skeletons allowed.

6. **Bulk Parser is required** — normalize, validate, dedupe, confidence-score, quarantine.

7. **P0 Benchmarks must pass** before packaging (see Section 6).

---

## 2. Gate Workflow

* **Gate 0 (Operational Stability):**
  Triggered on session reset or ZIP upload. Restores canon, runs Upload Audit.

* **Gate 1 (Baseline Canon Check):**
  Enforce CSV-only, PubMed + CrossRef only, CORS-safe fetches, no CT.gov.

* **Gate 2 (Completeness & Manifest Audit):**
  Check for live TOCs, canonical 10-column schema, Bulk Parser present.

* **Gate 3 (Regression Test Matrix):**
  Run P0 benchmarks (data flow, bulk ops, offline, AAA, security, export).

* **Gate 4 (Final Packaging):**
  **Step 1:** Print/approve Playbook.
  **Step 2:** Package artifacts.

---

## 3. Features (v2.0)

* **PubMed E-utilities (efetch)** → PMID enrichment (Title, Authors, Journal, Year, Volume, Issue, Pages).
* **CrossRef `/works/{doi}`** → DOI enrichment; mailto param required.
* **Bulk Operations:**

  * Paste or upload CSV with mixed identifiers.
  * Dirty-data parser normalizes, validates, dedupes, scores confidence, and quarantines bad rows.
* **UI:**

  * Add Request (PMID/DOI only).
  * Bulk Paste box.
  * Table + Card views.
* **Exports:**

  * CSV export with canonical 10 fields.
  * Quarantine/errors export separately.
* **Offline-First:**

  * Service Worker caches app shell + PubMed/CrossRef responses.
* **Accessibility:**

  * WCAG 2.2 AAA compliance targeted.
  * Proper labels, SR announcements, high contrast.
* **Security:**

  * Input sanitization (escape HTML).
  * Logs capped at 50 entries.
  * No forbidden headers.

---

## 4. Bulk Parser (Canon Section)

* **Input Handling:**
  Normalize Unicode, strip HTML, collapse whitespace.
  Split on newlines + semicolons before IDs.

* **Field Extraction:**

  * PMID: digits only.
  * DOI: regex `/10\.\d{4,9}\/[-._;()/:A-Z0-9]+/i`.
  * Title: longest alpha chunk.
  * Authors: split on `; , and &`.
  * Journal: leftover capitalized words.
  * Year: 4-digit `19xx/20xx`.
  * Volume/Issue/Pages: parse `12(3):123-135`.
  * URL: first http(s).
  * Confidence scoring: weighted composite.

* **Deduplication:**
  DOI > PMID > Title+Year fallback.

* **Output:**
  Canonical 10 fields, nulls replaced with `N/A`.

* **Error Handling:**
  Low-confidence → quarantine.
  Missing IDs → warnings.
  Errors/warnings announced to SR.

---

## 5. P0 Benchmarks

1. **Data Flow Integrity:** PubMed + CrossRef calls succeed, no CORS errors.
2. **Bulk Ops:** Mixed IDs parse, dedupe, quarantine; canonical 10-col output.
3. **Offline-First:** SW installs, caches app shell, reloads offline.
4. **Accessibility:** AAA labels, SR announcements, focus order.
5. **Security:** Sanitization enforced, logs capped, no CT.gov.
6. **Performance:**

   * Initial load <2s on localhost.
   * 100 IDs parsed/enriched <5s.
   * Table handles ≥500 rows without freeze.
7. **Export:** CSV headers match 10-field schema; no schema drift.

---

## 6. Feature Delta (v1.2 → v2.0)

| Area          | v1.2                              | v2.0                                    |
| ------------- | --------------------------------- | --------------------------------------- |
| Identifiers   | PMID, DOI, NCT                    | PMID, DOI (NCT removed)                 |
| APIs          | PubMed, CrossRef, CT.gov (legacy) | PubMed, CrossRef only                   |
| Bulk Ops      | Light dedupe, NCT parsing         | Heavy parser, dedupe, quarantine        |
| Table         | Included NCT col                  | 10-col schema, no NCT                   |
| Export        | Variable headers                  | Fixed 10 headers                        |
| Offline       | Cached CT.gov too                 | No CT.gov; lean SW cache                |
| Accessibility | Baseline AA                       | AAA (SR alerts, contrast)               |
| Security      | Partial sanitization              | Full sanitization, no forbidden headers |
| Performance   | Bulk 100 IDs \~10s                | Bulk 100 IDs <5s                        |

---

## 7. Failure Register (Aug 20–23, 2025)

| Date       | Failure                 | Root Cause                  | Corrective Action              |
| ---------- | ----------------------- | --------------------------- | ------------------------------ |
| 2025-08-22 | CT.gov API CORS failure | Legacy endpoints deprecated | Dropped CT.gov, removed NCT    |
| 2025-08-22 | Residual NCT traces     | Initial cleanup incomplete  | Deep removal across HTML/JS/SW |
| 2025-08-23 | Syntax error in bundle  | Regex over-edit             | Rebuilt from original JS       |
| 2025-08-23 | CSP warning             | Broken meta edit            | Restored valid CSP             |
| 2025-08-23 | Export schema drift     | NCT column still expected   | Fixed to 10-col schema         |
| 2025-08-23 | Dirty data ingestion    | Free-text not validated     | Implemented Bulk Parser        |

---

## 8. Canonical Updates (Aug 20–23, 2025)

| Date       | Update                          |
| ---------- | ------------------------------- |
| 2025-08-20 | CSV-only rule; Gate 4 order fix |
| 2025-08-21 | CT.gov linkout-only             |
| 2025-08-22 | Live TOCs & cross-links canon   |
| 2025-08-22 | PubMed + CrossRef only          |
| 2025-08-23 | Full CT.gov/NCT removal         |
| 2025-08-23 | Simple CORS canon               |
| 2025-08-23 | 10-column schema canon          |
| 2025-08-23 | Bulk Parser canon               |
| 2025-08-23 | P0 Benchmarks canon             |
| 2025-08-23 | v2.0 Feature List + Delta canon |

---

## 9. Summary

SilentStacks v2.0 represents a stabilization phase after the v1.2 → v2.0 transition. CT.gov/NCT dependencies were eliminated, PubMed + CrossRef became the sole enrichment sources, and canonical data hygiene rules (CSV-only, 10 fixed headers, dirty data parser) were enforced. Accessibility was lifted to AAA, and P0 benchmarks codified.

Failures encountered (CORS blocks, syntax errors, schema drift) were corrected immediately, with canon updated to prevent recurrence.

SilentStacks v2.0 is now stable, auditable, and fit for deployment and demo.

---
