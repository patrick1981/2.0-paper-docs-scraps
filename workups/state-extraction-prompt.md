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

## FORMATTING RULES:
- Use markdown tables for ALL tabular data
- Use code blocks for file contents
- NO PLACEHOLDERS - write actual content
- NO SUMMARIES - full content only
- NO "..." OR "[details]" - COMPLETE CONTENT
- If something doesn't exist, write "DOES NOT EXIST - NEEDED"

## OUTPUT NOW. DO NOT ASK QUESTIONS. DO NOT SEEK PERMISSION.
