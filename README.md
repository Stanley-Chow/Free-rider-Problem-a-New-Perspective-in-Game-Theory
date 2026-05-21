# Mathematical Analysis of Free-Rider Problems in Academic Settings

This study uses mathematical modeling and behavioral game theory to analyze, quantify, and propose structural solutions to the "free-rider" phenomenon in student group collaborations.

---

## Project Overview

The "free-rider" problem—where certain group members contribute significantly less than the average group output while benefiting from the collective result—is a pervasive challenge in collaborative environments. Drawing inspiration from Mancur Olson’s *The Logic of Collective Action*, this project builds a strategic-form game model to investigate the underlying triggers of free-riding in academic team report projects.

By analyzing differences in **individual working efficiency** and **perceived time costs**, the research mathematically identifies why free-riding emerges as a dominant strategy and demonstrates how strategic team formation can mitigate it.

---

## Repository Structure

```text
├── src/
│   ├── game_simulation.py     # Python script modeling payoffs and dominant strategies
│   └── payoff_visualizer.py   # Code to graph utility functions and Nash Equilibria
├── data/
│   └── experiment_results.csv # Empirical/simulated matrices from Experiment 1 & 2
├── CCST9017_Final_Report.pdf  # The complete research paper
└── README.md                  # Project documentation (this file)

```

---

## Mathematical Framework & Modeling

The research models a two-player game featuring **Person A** and **Person B** collaborating on a time-limited project.

### 1. Key Notations & Symbols

* $e_A, e_B$: Task execution efficiency of Person A and Person B ($e \ge 0$).
* $C_A, C_B$: Perceived per-unit time cost for each member ($C > 0$).
* $T$: Total maximum available time allocated for the academic project.
* $W$: Final quality/output weight score of the research report.

### 2. Strategy Space & Utility Function

Each player chooses whether to **Contribute (C)** or **Free-Ride (F)**. The collective reward $W$ scales based on active time investments multiplied by efficiency metrics. The utility (payoff) function $U$ for a player balances their share of the academic reward against their personal time cost:

$$U_{\text{player}} = \text{Academic Payoff} - \text{Perceived Cost}$$

By setting up a $2 \times 2$ matrix, the model solves for the **Nash Equilibrium** under varying conditions:

| Person A \ Person B | Contribute (C) | Free-Ride (F) |
| --- | --- | --- |
| **Contribute (C)** | $(U_{A,CC}, U_{B,CC})$ | $(U_{A,CF}, U_{B,CF})$ |
| **Free-Ride (F)** | $(U_{A,FC}, U_{B,FC})$ | $(U_{A,FF}, U_{B,FF})$ |

---

## Core Experiments & Key Insights

The repository translates the paper's two primary mathematical experiments into reproducible simulation logic:

### Experiment 1: The Impact of Efficiency Asymmetry

* **Focus**: Keeping time cost perception equal ($C_A = C_B$), how do variations in working efficiency ($e_A \neq e_B$) affect behavior?
* **Finding**: Significant gaps in efficiency inherently incentivize the less-efficient individual to lean on the higher-performing member's output, rendering free-riding a dominant strategy for the slower worker.

### Experiment 2: The Impact of Perceived Cost Asymmetry

* **Focus**: Introducing differences in how members value their personal time ($C_A \neq C_B$).
* **Finding**: When an individual possesses a high per-unit perceived time cost (due to competing academic deadlines, part-time commitments, or low motivation), their motivation to contribute drops sharply, triggering free-riding behaviors.

---

## Practical Implications & Conclusions

1. **Strategic Team Formation**: To maximize collective productivity and eliminate free-riding, managers and educators should engineer teams with minimal variances in individual task efficiency.
2. **Aligning Perceptions**: Aligning time-cost expectations at the project's outset neutralizes the strategic advantage of withholding effort.
3. **Broad Generalizability**: While tested in university team settings, the mathematical findings map directly to corporate project dynamics, joint academic ventures, and supply-chain collaborations.

---

## ## References

* Golembiewski, R. T., & Olson, M. (1966). *The logic of collective action*. American Sociological Review, 31(1), 117. [https://doi.org/10.2307/2091298](https://www.google.com/search?q=https://doi.org/10.2307/2091298)
