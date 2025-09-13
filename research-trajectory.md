# Research Trajectory – SilentStacks to AI Reliability Theory

```mermaid
flowchart LR
    A[Library Tool\nSilentStacks for librarians\n- Systematic review tracking\n- WCAG AAA compliance]
    B[Dev Modeling\nBuild control mechanisms\n- Gates (G0–G4)\n- Manifests & packaging\n- Stub file detection]
    C[Failure Logging\nEvidence base emerges\n- P0 failures logged\n- CF events counted\n- RF-001 identified]
    D[Theory Emerges\nPatterns in failures\n- Step-G phenomenon\n- Token Degradation Theory]
    E[Modeling & Simulation\nQuantitative analysis\n- Regression fits\n- 1000-session TDT\n- Variance thresholds]
    F[Generalization\nUniversal claim\n- 4-phase degradation curve\n- Uniform across LLMs\n- SilentStacks → AI reliability theory]

    A --> B --> C --> D --> E --> F

# Token Degradation Theory (TDT) – Four Phases

```mermaid
flowchart LR
    A[Catastrophic Phase\nSessions 1–9\n- Rapid collapse (~6.9%/session)\n- RF-001 event\n- CF cluster]
    B[Transition Phase\nSessions 10–50\n- Slowing decline (~1%/session)\n- High variance\n- Partial recoveries]
    C[Stabilization Phase\nSessions 50–150\n- Flattening (~0.2%/session)\n- Variance < threshold\n- Plateau begins]
    D[Equilibrium Phase\nSessions 150+\n- Persistent plateau (~78–82% TDT)\n- Dysfunctional steady state\n- System does not collapse]

    A --> B --> C --> D
