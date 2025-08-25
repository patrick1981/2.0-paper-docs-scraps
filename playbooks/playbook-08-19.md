# 📘 SilentStacks Playbook v2.1

**Created:** 2025-08-19
**Status:** Draft – under active refactor
**Maintainer:** Solo + AI-assisted

---

## 1. Client-Side Data Architecture & Limits (P0)

* **All client-side.** IndexedDB for requests & bulk jobs; localStorage for settings/state.
* **Hard Cutoff:** Max **50,000 rows** per bulk job. Larger → reject.
* **Rate Limits:** PubMed throttled ≤ 2/sec. Worst case: 50k run ≈ 7 hrs.
* **Checkpointing:** Progress indicator with resume capability.
* **Dirty Data Handling:**

  * Invalid rows highlighted.
  * *Commit Clean Only* vs *Commit All* toggle.
  * Export dirty-only set for cleaning + re-import.
* **Accessibility:** AAA baseline. Light, Dark, and High Contrast themes are P0.

---

## 2. Add Request (Single Entry)

* Input: PMID, DOI, or NCT → metadata fetch (PubMed/CrossRef/CT.gov).
* Deduplication & cross-checks across IDs.
* Manual fill for missing fields; librarian tagging.
* Save → auto-commit to table + card view.
* **UI Contract:** v1.2 preserved (tabs, IDs, roles).

---

## 3. Bulk Operations

* **Sources:** Clipboard paste, CSV/XLS upload, raw text.
* Normalize tokens → route by type.
* **Edge Cases:** Mixed valid/invalid IDs, titles-only, Excel junk, email dumps.
* **Commit Paths:**

  * Auto-commit obvious matches.
  * Librarian confirmation for uncertain matches.
  * Clean vs All toggle.

---

## 4. Worst-Case Scenarios

* **Singleton Garbage:** Fail gracefully, suggest manual search.
* **Bulk Flood:** 500k rows → reject at 50k cutoff.
* **Network Loss:** Resume from checkpoint.
* **Mixed Dirty Data:** Dirty flagged, export enabled.
* **Machine Hog:** Long jobs mitigated by checkpoint + pause/resume.

---

## 5. Accessibility & Theming

* WCAG 2.2 AAA baseline.
* Theme switching: light/dark/high-contrast.
* ARIA labels, skip links, live regions, keyboard navigation enforced.

---

## 6. Exports & Interop

* Strict NLM citation format enforced.
* Export clean-only vs full set.
* Dirty rows always `"n/a"`.
* Round-trip safe: exports re-importable.

---

## 7. Security & Storage

* Input sanitization (escape HTML/scripts).
* API URLs encoded, injection-proof.
* IndexedDB for requests (scalable).
* LocalStorage for settings only.
* Error log capped at 50 entries.

---

## 8. Baseline Declaration

* v1.2 UI remains contract (IDs/classes/roles).
* **CT.gov API disabled** — NCT linkouts only.
* Modularized repo structure authoritative.

---

## 9. P0 Requirements

* Bulk ops (PMID/DOI/NCT) with throttling & checkpoint.
* Canonical headers (Fill Status last):

  ```
  Urgency | Docline # | PMID | Citation | NCT Link | Patron e-mail | Fill Status
  ```
* `"n/a"` enforced for all missing fields.
* Dirty-only export path mandatory.

---

## 10. Security Conformance Matrix

| Risk                 | Control                                 | Status    |
| -------------------- | --------------------------------------- | --------- |
| XSS                  | Escape HTML/attributes; sanitize inputs | ✅ Met     |
| API Injection        | Regex validation; URL-encode params     | ✅ Met     |
| CORS Misuse          | CT.gov API calls disabled; linkout only | ✅ Met     |
| Data Leakage         | Exports normalized; `"n/a"` enforced    | ✅ Met     |
| Storage Safety       | IndexedDB cleanup of malformed blobs    | ⚠ Pending |
| Dependency Integrity | Pin libraries; SRI hashes for CDN       | ⚠ Pending |

---

## 11. WCAG 2.2 AAA Conformance Matrix

| Criterion               | Level | Status    |
| ----------------------- | ----- | --------- |
| Contrast (Enhanced)     | AAA   | ✅ Met     |
| Visual Presentation     | AAA   | ⚠ Pending |
| Images of Text          | AAA   | ✅ Met     |
| Keyboard (No Exception) | AAA   | ✅ Met     |
| No Timing               | AAA   | ✅ Met     |
| Three Flashes           | AAA   | ✅ Met     |
| Location                | AAA   | ⚠ Pending |
| Link Purpose            | AAA   | ✅ Met     |
| Section Headings        | AAA   | ✅ Met     |
| Focus Not Obscured      | AAA   | ⚠ Pending |
| Focus Appearance        | AAA   | ✅ Met     |
| Accessible Auth         | AAA   | N/A       |
| Identify Purpose        | AAA   | ✅ Met     |
| Consistent Help         | A/AA  | ⚠ Pending |
| Media Alternatives      | AAA   | N/A       |

---

## 12. Worst-Case Scenarios (Explicit Matrix)

* **Dirty bulk paste** → Mixed IDs parsed, dirty flagged, `"n/a"` enforced.
* **Extreme bulk** → >50k rejected.
* **Network loss / tab close** → Checkpoint + resume.
* **Export/import loop** → Round-trip safe, dirty preserved.
* **Title-only dump w/ typos** → Fuzzy match, low-confidence flagged.
* **CSV junk** → Regex fallback, dirty preserved.

---

## 13. Acceptance Checklist

* ✅ P0 scope validated (bulk ops, headers, linkouts).
* ✅ Security tests (XSS, injection, CORS).
* ✅ AAA checks (contrast, keyboard, headings, links).
* ⚠ Pending: preferences panel, breadcrumbs, sticky focus, Help affordance.
* ✅ Worst-case scenarios simulated.
* ✅ Docs cross-linked, timestamps present.

---

**Bottom Line:**
SilentStacks v2.1 Playbook defines the operational contract: client-side only, bulk ops hardened, accessibility AAA baseline enforced, dirty-data and worst-case handling explicit. Demo-stable; production pending final accessibility + storage audits.

---

👉 Do you want me to also **save this out as a `.md` file** like we did with the v1.2 docs so you can slot it directly into GitHub?
