# Discrepancy Analysis: Prompt Extraction vs Pythonic Extraction

**Context:**  
Both extractions were run over the same SilentStacks session record.  
- **Prompt-based extraction** (manual/interpretive by ChatGPT) yielded **≈30 P0 failures**.  
- **Python-based extraction** (your JSON script) yielded **200+ P0 failures**.  

This document explains **why the counts diverge**.

---

## 1. Granularity of Extraction
- **Prompt extraction:** Groups related issues into **one P0**.  
  - Example: “Markdown wrapping missing” logged once, even if it happened 10+ times.  
- **Python extraction:** Treats **every occurrence** as its own P0.  
  - Same wrapper error appearing on three dates = three P0s.  

**Impact:** Python output much higher.

---

## 2. Triggering Logic
- **Prompt extraction:** Interpretive — only counts failures when clearly described in session narrative.  
- **Python extraction:** Rule-based — flags anything matching failure keywords (“missing,” “not wrapped,” “incomplete”).  

**Impact:** Script captures more subtle or repetitive failures.

---

## 3. Session Coverage
- **Prompt extraction:** Focused on ~20–25 visible sessions in record.  
- **Python extraction:** Parsed **all sub-entries** inside sessions (8–12 per session).  

**Impact:** Python produces >200 entries.

---

## 4. Treatment of Repeats
- **Prompt extraction:** Collapses repeats into **one canonical failure type**.  
  - “Markdown wrapper missing (recurring)” → logged once.  
- **Python extraction:** Logs repeats separately.  
  - Same wrapper issue on 08-20, 08-23, 08-25 = three distinct P0s.  

**Impact:** Higher counts in JSON.

---

## 5. Status Resolution
- **Prompt extraction:** Sometimes omits later repeats if marked ✅ Fixed.  
- **Python extraction:** Still logs repeats even if previously “fixed.”  

**Impact:** Inflation of count in JSON.

---

## 6. Summary Table

| Aspect                | Prompt Extraction | Python Extraction |
|------------------------|------------------|------------------|
| Granularity           | Consolidated “types” | Individual “instances” |
| Triggering Logic      | Interpretive | Rule-based |
| Session Coverage      | Top-level sessions | Sub-entries + all repeats |
| Treatment of Repeats  | Collapsed | Counted each time |
| Status Handling       | Deduplicated if fixed | Logs all regardless |

---

## ✅ Conclusion
- **Both extractions are correct**, but they measure **different things**:  
  - Prompt = **unique failure modes (taxonomy)**  
  - Python = **all recorded occurrences (logbook)**  
- Discrepancy (≈30 vs 200+) arises from **aggregation vs granularity**.

---

## 📌 Next Step (if desired)
To reconcile:
- Collapse JSON into **unique failure types** → should approach ~30.  
- Expand prompt extraction into **all occurrences** → should approach 200+.  
