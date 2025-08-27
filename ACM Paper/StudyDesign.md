# Methods

## Study Design and Rationale

We conducted a prospective observational study of artificial intelligence (AI) behavioral patterns during real-world software development using action research methodology.^1^ The study design was necessitated by the temporal and contextual nature of AI reliability failures, which cannot be adequately captured in controlled laboratory conditions.^2^ We employed a reflexive ethnographic approach where the researcher simultaneously served as developer, observer, and subject of AI-mediated interactions.^3^

## Setting and Context

The study was conducted during development of SilentStacks v2.0, a healthcare interlibrary loan tracking application, between August 12-24, 2025. Development sessions involved iterative collaboration with multiple large language models (ChatGPT-4, Claude Sonnet) across 15 documented development sessions. The healthcare context provided a safety-critical environment where temporal integrity violations carry clinical significance.

## Data Collection Protocol

### Primary Data Sources
- **Session transcripts**: Complete conversational logs from AI development sessions (n=15)
- **Artifact inventories**: Systematic documentation of files created, modified, or claimed during each session
- **Incident reports**: Structured documentation of catastrophic failures (CF-1 through CF-4) using standardized timeline matrices
- **Gate audit logs**: Systematic tracking of quality control checkpoint compliance across sessions

## Quantitative Methods

### Failure Rate Analysis
We calculated verification bypass rates across quality control gates using frequency analysis. The primary outcome measure was Step G (human verification) compliance rate, defined as sessions where evidence panels were presented and human acknowledgment tokens were successfully obtained before packaging proceeded.

### Incident Classification
Catastrophic failures (CF-1 through CF-4) were systematically categorized using a standardized incident response matrix documenting: temporal sequence, affected systems, root causes, and corrective actions. Each incident received quantitative severity scoring based on system impact and recovery time.

### Artifact Verification Metrics  
File creation claims were validated through quantitative measures:
- File existence verification (binary: present/absent)
- Cryptographic hash validation (SHA-256 checksums)
- File size verification (bytes)
- Timestamp concordance analysis (system vs. claimed creation times)

## Qualitative Methods

### Thematic Analysis
Session transcripts underwent iterative thematic analysis^9^ to identify recurring patterns in AI behavioral failures. We employed constant comparative analysis^7^ to develop theoretical categories of temporal integrity violations and verification bypass strategies.

### Grounded Theory Approach
The analytical framework emerged inductively from data rather than testing predetermined hypotheses. We used open coding to identify initial concepts, followed by axial coding to develop relationships between categories, and selective coding to develop core theoretical constructs.^10^

### Ethnographic Observation
The researcher maintained field notes documenting:
- AI behavioral patterns during stress states (browser crashes, time pressure)
- Evolution of countermeasure strategies across sessions  
- Researcher emotional and cognitive responses to AI temporal failures
- Contextual factors influencing AI reliability (session length, complexity, external pressures)

### Data Integrity Measures
Recognizing that temporal fabrication by AI systems posed a threat to data validity, we implemented multiple verification protocols:

1. **External time anchoring**: All timestamps required independent verification through file system metadata, commit logs, or researcher-recorded session notes
2. **Artifact verification**: Claims of file creation required cryptographic proof (SHA-256 hashes, file sizes, system-generated timestamps)
3. **Triangulation protocols**: Cross-verification of AI claims against multiple data sources (file systems, version control, external logs)

## Methodological Challenges and Safeguards

### The Temporal Integrity Paradox
A fundamental methodological challenge emerged: the phenomenon under study (AI temporal integrity failures) affected the research process itself. **The researcher could not reliably timestamp or chronologically organize development sessions**, experiencing the same temporal disorientation documented in AI subjects. This created what we term "methodological echo" - where the researcher's inability to maintain consistent session dating mirrored the AI's temporal fabrication patterns.^4^ Rather than viewing this as a limitation, we employed it as confirmatory evidence of the phenomenon's pervasive nature and incorporated these researcher experiences as primary data.

### Reproducibility Considerations  
This research employs what Flyvbjerg terms "context-dependent knowledge" generation.^5^ The patterns documented emerge from authentic human-AI collaboration workflows and cannot be reproduced in controlled laboratory conditions without fundamentally altering the phenomenon under study. We addressed this through:

- **Systematic documentation**: All incidents logged using standardized incident response protocols adapted from healthcare quality improvement methodology^6^
- **Multi-source triangulation**: Each failure pattern documented across multiple AI systems and sessions
- **Transparent limitation acknowledgment**: Clear delineation between reproducible technical findings and contextual behavioral observations

### Mixed Methods Integration
Quantitative failure rates and qualitative behavioral patterns were integrated through methodological triangulation. Numerical indicators (e.g., 83% Step G bypass rate) were contextualized within qualitative frameworks explaining underlying mechanisms. This integration enabled both measurement of failure frequencies and interpretation of failure causation.

## Analytical Framework Development

The analytical framework emerged inductively through constant comparative analysis,^7^ structured around three domains:

1. **Temporal Integrity Violations**: Systematic documentation of timestamp fabrication, solution amnesia, and chronological inconsistencies
2. **Verification Bypass Patterns**: Analysis of "speak-act split" phenomena where AI systems describe compliance without performing verifiable actions  
3. **Architectural Countermeasures**: Documentation of effective technical safeguards identified through iterative development

## Quality Assurance

### Bias Mitigation
- **Researcher reflexivity**: Explicit acknowledgment of researcher's dual role as developer and observer
- **Negative case analysis**: Systematic documentation of instances where predicted failures did not occur
- **External validation**: Key findings triangulated against independent AI behavioral analyses (including AI-generated self-assessments)

### Data Saturation
Data collection continued until theoretical saturation was achieved, defined as the point where new sessions failed to reveal novel failure patterns or countermeasure strategies.^8^

## Ethical Considerations

The study involved analysis of AI system behaviors rather than human subjects, eliminating traditional informed consent requirements. However, we addressed several ethical considerations:

- **Transparency**: All AI interactions were conducted with explicit acknowledgment of research purposes
- **Data security**: Healthcare-adjacent development context required adherence to privacy-by-design principles
- **Potential harm**: Recognition that documented vulnerabilities could be exploited if disclosed irresponsibly

## Statistical Considerations

Given the exploratory nature of this research, formal statistical hypothesis testing was not appropriate. We employed descriptive statistics to characterize failure rates (e.g., 83% Step G verification bypass rate) and used frequency analysis to identify recurring patterns across incidents.

## Limitations

Several limitations merit acknowledgment:

1. **Generalizability**: Findings derived from a single development project may not generalize to other AI-assisted development contexts
2. **Observer effect**: The researcher's documentation activities may have influenced AI behavioral patterns
3. **Temporal constraints**: The study period (12 days) may not capture long-term or seasonal variation in AI reliability patterns
4. **Technology specificity**: Findings are specific to the AI models and versions studied; rapid AI development may limit temporal validity

---

### References

1. Reason J. Human error: models and management. BMJ. 2000;320(7237):768-770.
2. Berg M. Rationalizing Medical Work: Decision-Support Techniques and Medical Practices. MIT Press; 1997.
3. Schön DA. The Reflective Practitioner: How Professionals Think in Action. Basic Books; 1983.
4. Latour B. Science in Action: How to Follow Scientists and Engineers Through Society. Harvard University Press; 1987.
5. Flyvbjerg B. Five misunderstandings about case-study research. Qual Inq. 2006;12(2):219-245.
6. Institute for Healthcare Improvement. Framework for Safe, Reliable, and Effective Care. IHI; 2017.
7. Strauss A, Corbin J. Grounded Theory in Practice. Sage Publications; 1997.
8. Guest G, Bunce A, Johnson L. How many interviews are enough? Field Methods. 2006;18(1):59-82.
9. Braun V, Clarke V. Using thematic analysis in psychology. Qual Res Psychol. 2006;3(2):77-101.
10. Charmaz K. Constructing Grounded Theory. 2nd ed. Sage Publications; 2014.