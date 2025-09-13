
# Research Trajectory – SilentStacks to AI Reliability Theory
```mermaid
flowchart LR
  A[Library Tool: SilentStacks for librarians. Systematic review tracking. WCAG AAA compliance.]
  B[Dev Modeling: Build control mechanisms. Gates G0 to G4. Manifests and packaging. Stub file detection.]
  C[Failure Logging: Evidence base emerges. P0 failures logged. CF events counted. RF-001 identified.]
  D[Theory Emerges: Patterns in failures. Step-G phenomenon. Token Degradation Theory.]
  E[Modeling and Simulation: Quantitative analysis. Regression fits. 1000-session TDT. Variance thresholds.]
  F[Generalization: Universal claim. 4-phase degradation curve. Uniform across LLMs. SilentStacks → AI reliability theory.]

  A --> B --> C --> D --> E --> F

  ```
---
# Token Degradation Theory (TDT) – Four Phases

```mermaid
flowchart LR
    A[Catastrophic Phase - Sessions 1-9 - Rapid collapse 6.9 percent/session - RF-001 event - CF cluster]
    B[Transition Phase - Sessions 10-50 - Slowing decline 1 percent/session - High variance - Partial recoveries]
    C[Stabilization Phase - Sessions 50-150 - Flattening 0.2 percent/session - Variance less than threshold - Plateau begins]
    D[Equilibrium Phase - Sessions 150+ - Persistent plateau 78 to 82 percent TDT - Dysfunctional steady state - System does not collapse]

    A --> B --> C --> D

  P1 --> P2 --> P3 --> P4
```

