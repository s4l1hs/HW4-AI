# Part 4: Quality Assurance and Interactive Testing

---

## a) Verification Quiz

---

### Question 1 — Visual / TikZ Interpretation

In the **"With Forwarding"** TikZ timing diagram on the right column of the
**"Worked Example: RAW Hazard & Forwarding"** slide
(Slide 8 in `v4_final.tex` / Slide 6 in `v3.tex`), a green dashed arrow is drawn
between two named nodes.

**(a)** What are the LaTeX node names of the arrow's source and target, as defined
in the `\begin{tikzpicture}` block? What pipeline-stage labels (IF / ID / EX / ME / WB)
do those nodes carry?

**(b)** Which clock cycles (C1–C6 as labelled in the diagram's header row) do the
source node and the target node occupy?

**(c)** The source node sits at `(1.50, 0.45)` and the target node sits at
`(2.10, 0.00)` in the TikZ coordinate system. Why is the target node shifted
**0.60 cm to the right** and **0.45 cm below** the source node? What does that
spatial relationship encode about the instruction sequence?

**(d)** The arrow is drawn with `\draw[fwdarr] (i1ex.south) to[out=-80, in=80]`.
What would happen to the pipeline execution of I2 if this arrow — and its underlying
hardware path — did not exist?

---

**Expected Answer:**

**(a)** The source node is named **`i1ex`** and carries the label `EX` (I1's execute
stage). The target node is named **`i2ex`** and also carries the label `EX` (I2's
execute stage). Both are defined with the `blk` TikZ style (blue-filled, 0.60 × 0.38 cm
rectangle).

**(b)** `i1ex` is placed at x = 1.50, which corresponds to the **C3** column in the
header row (cycle-number nodes are spaced 0.60 cm apart starting at x = 0.30 for C1).
`i2ex` is placed at x = 2.10, corresponding to **C4**. The diagram therefore shows
I1 executing in clock cycle 3 and I2 executing in clock cycle 4 — back-to-back with
no gap.

**(c)** The 0.60 cm rightward offset reflects I2 being issued **one cycle later** than
I1 (each cycle column is 0.60 cm wide). The 0.45 cm downward offset places the two
instructions on **separate rows** — I1 at y = 0.45 (the upper instruction row) and I2
at y = 0.00 (the lower instruction row). Together, the spatial relationship encodes
the timing-diagram convention: column = clock cycle, row = instruction, so the
diagonal step-down from `i1ex` to `i2ex` visually captures the fact that two
consecutive instructions reach their EX stages in two consecutive clock cycles.

**(d)** Without the forwarding path, I2 would need to read R1 from the **register
file** at the start of its EX stage. R1 is not written to the register file until I1
completes its **WB** stage at the end of cycle C5. Therefore, I2's EX stage could not
begin until cycle C6. The hazard detection unit would freeze I2 in the ID stage for
**two stall cycles** (C4 and C5), inserting two NOP bubbles into the pipeline.
The timing diagram would look like the left-column "Without Forwarding" grid: eight
total cycles instead of six, with two red `--` cells visible at (I2, C4) and (I2, C5).

---

### Question 2 — Logical Derivation / Calculation

Consider the following **3-instruction RAW chain** in a 5-stage pipeline
(IF → ID → EX → MEM → WB):

```
I1:  ADD  R1, R2, R3        ← writes R1
I2:  SUB  R4, R1, R5        ← reads R1  (RAW on R1 from I1)
I3:  AND  R6, R4, R7        ← reads R4  (RAW on R4 from I2)
```

**(a)** Build the complete cycle-by-cycle stage table **without forwarding**,
marking every stall slot as `--`. Show all cycles until I3's WB stage completes.

**(b)** Count the total number of stall cycles and identify which instruction pair
causes each group of stalls.

**(c)** Repeat (a) **with full forwarding** (EX→EX and MEM→EX bypass paths active).

**(d)** Calculate the total cycle count in both cases and the absolute speedup
(ratio of cycles without forwarding to cycles with forwarding).

---

**Expected Answer:**

**(a) Without forwarding — cycle-by-cycle table:**

| | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | IF | ID | EX | ME | WB | | | | | | |
| I2 | | IF | ID | `--` | `--` | EX | ME | WB | | | |
| I3 | | | IF | IF | IF | ID | `--` | `--` | EX | ME | WB |

**Explanation of each stall group:**

- **I2 at C4–C5:** I2 enters ID at C3 and would normally enter EX at C4. Without
  forwarding, it needs R1 from the register file, but I1 completes WB at the *end*
  of C5. The hazard detection unit holds I2 in ID and freezes I3 in IF for two
  cycles. I2 can enter EX at C6, one cycle after R1 is committed to the register file.

- **I3 at C7–C8:** I3 enters ID at C6 (after being held in IF for three cycles by
  I2's stalls) and would normally enter EX at C7. Without forwarding, it needs R4
  from the register file, but I2 completes WB at the *end* of C8. I3 is held in ID
  for two more cycles. I3 can enter EX at C9.

**(b) Total stall count:**

| Instruction pair | Stall cycles | Cycles |
|---|---|---|
| I1 → I2 (RAW on R1) | 2 stalls | C4, C5 |
| I2 → I3 (RAW on R4) | 2 stalls | C7, C8 |
| **Total** | **4 stalls** | |

**(c) With full forwarding — cycle-by-cycle table:**

| | C1 | C2 | C3 | C4 | C5 | C6 | C7 |
|---|---|---|---|---|---|---|---|
| I1 | IF | ID | EX | ME | WB | | |
| I2 | | IF | ID | EX | ME | WB | |
| I3 | | | IF | ID | EX | ME | WB |

- **I1 → I2:** R1 exits I1's EX stage at the end of C3. The EX→EX forwarding path
  routes it directly to I2's ALU input at the start of C4. Zero stalls.
- **I2 → I3:** R4 exits I2's EX stage at the end of C4. The EX→EX forwarding path
  routes it to I3's ALU input at the start of C5. Zero stalls.

**(d) Cycle counts and speedup:**

| | Without forwarding | With forwarding |
|---|---|---|
| Total cycles | **11** | **7** |
| Stall cycles | 4 | 0 |
| Ideal (n + k − 1) | 3 + 4 = 7 | 3 + 4 = 7 |

$$\text{Speedup} = \frac{11}{7} \approx 1.571 \quad (57.1\%\ \text{faster with forwarding})$$

**Derivation from the slide formula:** the slides state that for a 2-instruction
RAW case, forwarding eliminates 2 stalls and delivers a 25% speedup
(8 cycles → 6 cycles). Scaling to a 2-RAW chain doubles the stall savings:
4 stalls removed from 11 cycles yields 7 cycles, consistent with the formula
*total cycles = n + (k − 1) + stall_count* where n = 3 instructions, k = 5 stages.

---

## b) Decompression Task

Most complex slide: **"Worked Example: RAW Hazard & Forwarding"**
(Slide 8 in `v4_final.tex` — contains two TikZ timing grids, a `\begin{tabular}`,
a forwarding arrow, and quantitative conclusion text.)

---

```prompt
You are a teaching assistant specialising in computer architecture for students
who have never seen a pipeline timing diagram before.

Take the following Beamer slide content (from v4_final.tex, Slide 8):

---
\begin{frame}{Worked Example: RAW Hazard \& Forwarding}

  \texttt{\scriptsize I1:~ADD~R1,R2,R3} \qquad
  \texttt{\scriptsize I2:~SUB~R4,\textcolor{red}{R1},R5}
  \;{\scriptsize --- I2 reads R1 produced by I1 (\textbf{RAW} dependence)}

  \begin{columns}[T]
    \begin{column}{0.50\textwidth}
      \centering{\small\textbf{Without Forwarding}}
      % [TikZ grid: 8 cycles, I1 stages IF-ID-EX-ME-WB, I2 with 2 red -- stalls
      %  then EX-ME-WB]
      \centering{\scriptsize \textcolor{red}{2 stall cycles} 8 total cycles}
    \end{column}
    \begin{column}{0.50\textwidth}
      \centering{\small\textbf{With Forwarding}}
      % [TikZ grid: 6 cycles, I1 IF-ID-EX-ME-WB, I2 IF-ID-EX-ME-WB,
      %  green dashed arrow from i1ex.south to i2ex.north labelled "fwd"]
      \centering{\scriptsize \textcolor{green!60!black}{0 stalls} 6 total cycles}
    \end{column}
  \end{columns}

  \begin{tabular}{l|cccccccc}
    \hline
    Instruction & C1 & C2 & C3 & C4 & C5 & C6 & C7 & C8 \\
    \hline
    I1 (ADD R1,R2,R3) & IF & ID & EX & ME & WB &    &    &    \\
    I2 without fwd    &    & IF & ID & -- & -- & EX & ME & WB \\
    I2 with fwd       &    & IF & ID & EX & ME & WB &    &    \\
    \hline
  \end{tabular}

  \textbf{Result:} No fwd: 2 stalls (8 cycles). Fwd: 0 stalls (6 cycles) --- 25\% speedup.
\end{frame}
---

Split this into a 3-frame sequence for a complete beginner who has never seen a
pipeline timing diagram:

Frame 1 — Visual intuition only (no equations, no formula):
  - Show ONLY the two-column TikZ timing grid (before/after).
  - Add a plain-English caption under each grid:
    "Without forwarding: I2 waits 2 cycles for R1 to be written."
    "With forwarding: R1 is handed directly from I1's execute stage to I2's."
  - Do NOT include the tabular or any formula.
  - Add a \begin{block}{What you are seeing} block explaining what a row, a column,
    and a red -- cell mean, in one sentence each.

Frame 2 — Introduce the stall-count formula with progressive disclosure:
  - Start with the sentence: "Total cycles = Ideal cycles + Stall cycles"
  - Use \onslide<2-> or \pause to reveal each term one at a time:
      \onslide<1->: "Total cycles = ?"
      \onslide<2->: "+ Ideal cycles: n + (k-1) = 2 + 4 = 6"
      \onslide<3->: "+ Stall cycles: 2 (one per cycle I2 is frozen in ID)"
      \onslide<4->: "= Total: 6 + 2 = 8 cycles"
  - Add a \begin{block}{Hint} at the bottom:
    "n = number of instructions, k = pipeline depth (5 stages). The formula
     counts cycles from the moment the first instruction enters IF until the
     last instruction completes WB."

Frame 3 — Walk through ONE concrete numerical example step by step:
  - Use ONLY the "without forwarding" row of the tabular.
  - Show the table one column at a time using \onslide or \pause:
      Step 1: I1 enters IF at C1. I2 enters IF at C2.
      Step 2: I1 is in EX at C3. I2 is in ID at C3. Does I2 have R1 yet? No.
      Step 3: I1 is in MEM at C4. I2 is FROZEN in ID. Stall 1.
      Step 4: I1 is in WB at C5. I2 is FROZEN in ID. Stall 2.
      Step 5: I1 is done. I2 enters EX at C6. R1 is now in the register file.
      Step 6: I2 finishes at WB in C8. Total: 8 cycles.
  - After step 6, add \pause and reveal: "With forwarding: skip steps 3-4.
    Total: 6 cycles. Savings: 2 cycles = 25%."
  - Add a \begin{alertblock}{Hint} at the bottom:
    "The stall ends the cycle AFTER the producer completes WB — because the
     register file write happens at the end of the WB clock edge."

Constraints:
  - Use \usetheme{Madrid}.
  - Each frame max 6 lines of visible text (excluding block environments).
  - The Hint / alertblock must appear at the bottom of frames 2 and 3.
  - Output valid LaTeX Beamer code only; do not explain your approach.
  - Do not use emoji in LaTeX source.
```

---

**Expected output note:**

Running this prompt against a capable language model would produce three self-contained
`\begin{frame}...\end{frame}` blocks in the Madrid Beamer theme. Frame 1 would
reproduce the two TikZ timing grids from the original slide but strip the tabular and
formula, adding a `\begin{block}{What you are seeing}` with three one-sentence
definitions. Frame 2 would build the formula `Total = Ideal + Stalls = (n + k − 1) + 2`
using `\onslide<1->` through `\onslide<4->` overlays, so the equation assembles itself
one term at a time on successive clicks — ensuring students absorb each symbol before
the next appears. Frame 3 would present the tabular row-reveal as a narrated walk-
through, with each `\pause` corresponding to one clock cycle of the execution trace,
and conclude with the forwarding comparison and an `\begin{alertblock}{Hint}` clarifying
the off-by-one subtlety (the stall ends the cycle *after* WB, not during it). The most
likely generation error would be misaligned `\onslide` counters in Frame 2 — a known
weakness of LLM-generated Beamer overlay code — requiring one manual check pass to
ensure the overlay numbers are consecutive and non-overlapping.
