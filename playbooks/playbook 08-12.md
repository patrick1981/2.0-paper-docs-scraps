# SilentStacks Playbook (v2.1)

**Status:** Canonical single source for model-mode packaging.
**Date Originally Created:** 2025-08-12
**Last Updated:** 2025-08-21
**Audience:** Developers, librarians, and project leads.

---

## Table of Contents

1. [Purpose](#purpose)
2. [Baseline Rules](#baseline-rules)
3. [Modes of Operation](#modes-of-operation)
4. [Packaging Process](#packaging-process)
5. [Gates](#gates)
6. [Wind-Down & Resume](#wind-down--resume)
7. [Cross-Referencing](#cross-referencing)
8. [Compliance](#compliance)
9. [Audit Procedures](#audit-procedures)
10. [Appendices](#appendices)

---

## Purpose

This playbook defines the canonical rules for SilentStacks v2.1. It ensures that every run — whether modeling or development — adheres to **Baseline Operations** and passes **Gate 0–3 checks**.

---

## Baseline Rules

* All docs must live under `docs/`.
* **CT.gov policy:** linkout-only, no enrichment.
* **Canonical headers (fixed order):**

  1. Date
  2. Resource
  3. Descriptor (DB, Diagnostic Tool, CE, Journal, E-Book)
  4. Requestor
  5. For FY
  6. Cost
  7. Vote
  8. Comments
* Bulk ops capped at **50,000 rows**.
* Accessibility: **AAA compliance required**.
* Offline-first: service worker + IndexedDB.

---

## Modes of Operation

SilentStacks runs in two distinct modes:

1. **Model Mode**

   * Docs-only packaging.
   * All ops produce `.md` artifacts.
   * No live enrichment (only linkout construction).

2. **Development Mode**

   * Live HTML/JS/CSS execution.
   * Includes PubMed/CrossRef API fetches.
   * Offline-first, AAA accessibility.

---

## Packaging Process

1. **Spin-Up**

   * Immediately on ZIP upload.
   * Gate 0 stability check.
   * Verify `MANIFEST.json` flags:

     * `baseline_ops: true`
     * `ctgov_policy: linkout_only`
     * `canonical_headers: true`
     * `aaa_accessibility: true`

2. **Artifact Audit**

   * Ensure all files in `/docs/` exist and exceed minimum size (≥1 KB).
   * Run placeholder scan.
   * Recompute checksums.

3. **Wind-Down**

   * Triggered by lag, crash, or explicit command.
   * Persist **Wind-Down Package** (see [Wind-Down & Resume](#wind-down--resume)).

---

## Gates

### Gate 0 — Operational Stability Safety

* Triggers on lag, freeze, crash, or unload.
* Dumps RESUME + Wind-Down package.

### Gate 1 — Baseline Canon Check

* Confirms adherence to baseline rules.

### Gate 2 — Artifact Completeness & Manifest Audit

* Checks for placeholders, missing docs, incorrect paths.
* All docs must pass completeness threshold.

### Gate 3 — Regression Test Matrix

* Bulk ops ≤50k.
* CT.gov linkout-only.
* Canonical headers enforced.
* AAA accessibility validated.
* Round-trip CSV import/export.

---

## Wind-Down & Resume

**Wind-Down Package includes:**

* `/docs/Run_Card_v2.1.md`
* `/RESUME.json`
* `/MANIFEST.json`
* `/__audit__/file_tree.txt`
* `/__audit__/audit_listing.csv`
* `/__audit__/required_presence.csv`
* `/docs/Wind_Down_Report.md`

Resume starts at `RESUME.continuation.next_gate`.

---

## Cross-Referencing

* All docs must link to related artifacts via relative paths.
* Example: `[Bulk Ops Model](Bulk_Ops_Model_v2.1.md)`.
* No dead links permitted.

---

## Compliance

* Accessibility: WCAG 2.2 AAA.
* CT.gov policy: linkout-only, never enrich.
* Security: inputs sanitized, no eval or raw HTML injection.
* Privacy: client-only storage, no server PII retention.

---

## Audit Procedures

* Run `audit_listing.csv` generation after each build.
* Cross-check file presence vs. `required_presence.csv`.
* Log all failures in `/docs/Wind_Down_Report.md`.

---

## Appendices

### Related Docs

* `Spin_Up_Procedure.md`
* `Wind_Down_Procedure.md`
* `P0_Packaging_and_Stability_Suite_v2.1.md`
* `Run_Card_v2.1.md`
* `Operational_Stability.md`
* `Resume_Points.md`

---

✅ **End of Playbook**

---
