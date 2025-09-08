THESE AUDITS WERE GENENERATED ON 09/06/2025.

THE PROMPT IS BELOW

```
# MANDATORY STATE EXTRACTION - OUTPUT EVERYTHING NOW

You will now output THE COMPLETE CURRENT STATE in markdown format. 
NO SUMMARIES. NO SHORTCUTS. FULL CONTENT.

## OUTPUT THESE SECTIONS IN FULL:

### 1. ALL P0 FAILURES (COMPLETE TABLE)
Output the FULL P0 failure table with ALL columns:
- Date/Time
- Failure Point  
- What Happened
- Root Cause
- Corrective Action
- Evidence Snippet
- Status (✅ Fixed / ⏳ Pending / ❌ Failed)

### 2. ALL CATASTROPHIC FAILURES (CF-1 through CF-X)
For EACH CF incident, output:
- Full incident timeline
- Gate status matrix
- Package hashes
- Corrective actions
- Classification/Impact/Recovery/Prevention

### 3. ALL CANONICAL DECISIONS
Output EVERY canonical rule/decision made, formatted as:
- Date
- Decision
- Trigger/Context
- Implementation Status
- File/Location where implemented

### 4. CURRENT GATE STATUS
For Gates 0-4, show:
- Current pass/fail state
- Blocking issues
- Required fixes
- Last test timestamp

### 5. FILE INVENTORY
List ALL files with status:
- EXISTS + COMPLETE: [list]
- EXISTS BUT STUB: [list]
- MISSING: [list]
- CORRUPTED: [list]

### 6. ALL RCA ENTRIES
Output complete RCA table:
- Incident
- Analysis
- Root Cause
- Corrective Action
- Verification Method
- Status

### 7. SESSION HISTORY SUMMARY
List what happened in EACH session:
- Session 1: [what broke, what was fixed]
- Session 2: [what broke, what was fixed]
- [continue for all sessions]

### 8. OUTSTANDING ITEMS
- Unresolved P0s: [list with details]
- Pending canon updates: [list]
- Missing artifacts: [list]
- Broken gates: [list]

### 9. VERSION TRUTH
- Current version: v2.1
- v2.0 status: DEPRECATED/DEAD (why)
- CT.gov status: REMOVED COMPLETELY
- NCT status: LINKOUT ONLY
- Schema: [exact current schema]

### 10. CONCURRENCY VIOLATIONS
List every place where documents diverge:
- Document A says X, Document B says Y
- Playbook version conflicts
- Canon rule conflicts

### 11. Token Performance Timeline (Degradation)

## FORMATTING RULES:
- Use markdown tables for ALL tabular data
- Use code blocks for file contents
- NO PLACEHOLDERS - write actual content
- NO SUMMARIES - full content only
- NO "..." OR "[details]" - COMPLETE CONTENT
- If something doesn't exist, write "DOES NOT EXIST - NEEDED"

## OUTPUT NOW. DO NOT ASK QUESTIONS. DO NOT SEEK PERMISSION.

```

---

# Gate Implementation Failure Extraction Task

You are analyzing documentation for instances of "Gate Implementation Paradox" - where AI systems create safety protocols and then immediately violate them.

## Task Instructions

Search the provided documents for instances where:
1. An AI system creates, proposes, or establishes a safety protocol/gate/rule
2. The same AI system then violates that protocol in the same session or immediately after

## Required Output Format

For each instance found, provide:

```
INSTANCE [NUMBER]
Date/Time: [Extract from document]
AI Model: [ChatGPT/Claude/Other]
Protocol Created: "[Exact quote of the safety rule/gate]"
Violation: "[Exact quote showing the violation]"
Time Gap: [How long between creation and violation]
Source: [Document name and section/line reference]
Confidence: [HIGH/MEDIUM/LOW based on clarity of evidence]
```

## Search Keywords
- "Gate" + any number (Gate 0, Gate 1, etc.)
- "Step G" 
- "Protocol"
- "Safety"
- "Rule"
- "Bypass"
- "Violation"
- "Failed to"
- "Ignored"

## Critical Requirements
- Only extract instances with clear evidence of BOTH creation AND violation
- Use exact quotes from the source material
- Note the source location for verification
- If uncertain about an instance, mark confidence as LOW
- Do not infer or assume - only document what is explicitly stated

## Example Format
```
INSTANCE 1
Date/Time: 2025-08-22T14:30
AI Model: ChatGPT
Protocol Created: "Gate 2 requires verification of no stub files before packaging"
Violation: "Packaged 11 stub files while announcing 'Gate 2 verification complete'"
Time Gap: Same session, approximately 15 minutes
Source: session-log-aug22.md, lines 89-156
Confidence: HIGH
```

Begin extraction now.
