# Prompt Engineering Log — Pipelining Hazards

---

## 1. Initial Prompt

The following condensed command was used to generate `v1.tex`:

```
Create quiz4-part1/slides/v1.tex. Topic: Pipelining Hazards in CPU Architecture.
Build deliberately weak — plain text only, no TikZ, no real-world analogy, no worked
example. Structure: 6 slides (title + 5 content slides + 1 references slide).
Requirements: \documentclass{beamer}, \usetheme{Madrid},
\usepackage{amsmath, amssymb, listings, xcolor}, \title{Understanding Pipelining Hazards},
frames using \begin{frame}{...}\end{frame}.
```

The five content slides covered: Introduction to CPU Pipelining, Data Hazards,
Structural Hazards, Control Hazards, and Hazard Mitigation Summary.

---

## 2. Design Choice

Pipelining Hazards was selected as the topic because it was identified in the student's
course history as the most difficult sub-topic within Computer Architecture — a subject
graded CB precisely because "pipelining/caching hard to visualize." This makes it an
ideal candidate for AI-assisted visual explanation. Beamer was chosen because it is the
de-facto standard for academic technical presentations in computer science: it supports
LaTeX math notation natively, integrates TikZ without friction, and produces
professional-quality PDFs suitable for Ninova upload. The Madrid theme was used for
the first three iterations because it is pre-installed in all standard TeX Live
distributions, avoiding any dependency risk during iterative development. The content
structure follows a deliberate **text → analogy → visual → polish** progression
across four versions, mirroring the pedagogical arc recommended in Patterson &
Hennessy's *Computer Organization and Design* (the course textbook): establish
vocabulary first, then build intuition, then provide a concrete model, then consolidate.
Five content areas were chosen to match the natural decomposition of the topic:
pipeline basics, data hazards (RAW/WAR/WAW), structural hazards, control hazards,
and mitigation strategies.

---

## 3. Iterative Refinement Process

Four iterations were performed: `v1.tex` → `v2.tex` → `v3.tex` → `v4_final.tex`.

---

### v1 → v2 (Iteration 1)

**Strategy:** "Explain the core concepts as if talking to a 10-year-old."

**Changes made:**
- Prepended a one-sentence real-world analogy before every technical concept on every
  slide (restaurant/assembly line for pipelining; relay race for RAW; pan-cleaning for
  WAR; report filing for WAW; loading dock for structural hazard; GPS wrong-lane for
  control hazard; factory supervisor for mitigation summary).
- Simplified jargon throughout by adding plain-English equivalents in parentheses
  (e.g., "stall" → "like holding a car at a red light for one cycle").
- Split the densest slide — Data Hazards, which had 6 bullets — into two frames:
  "Data Hazards — Types" and "Data Hazards — Detection & Mitigation".
- Changed `\medskip` to `\smallskip` in several places to accommodate the added
  analogy text without overflowing slides.
- File size grew from 5 370 bytes (115 lines) to 8 019 bytes (170 lines);
  slide count increased from **7 to 8**.

**Weakness addressed:** Dense technical jargon with no scaffolding made `v1.tex`
inaccessible to anyone without prior pipeline knowledge. Bullet points like "RAW (true
dependence): a consumer instruction attempts to read a register operand before the
producer instruction completes its WB stage" assumed fluency in micro-architecture
terminology. The analogies in v2 provide concrete mental hooks — the relay-race baton
for RAW, the loading-dock for structural conflicts, the GPS recalculation for branches
— that allow a reader to reason about the concepts before engaging the formal definitions.

---

### v2 → v3 (Iteration 2)

**Strategy:** "Add at least 2 TikZ diagrams and one concrete numerical worked example."

**Changes made:**
- Added `\usepackage{tikz}` and
  `\usetikzlibrary{positioning, arrows.meta, shapes}` to the preamble.
- Defined a global `\tikzset{}` block with six reusable styles:
  `stage` (large blue pipeline-stage box), `blk` (normal timing-grid cell, blue),
  `stl` (stall cell, red fill), `emp` (invisible spacer), `harr` (hardware arrow),
  `fwdarr` (green dashed forwarding arrow).
- **TikZ Diagram 1 — "The 5-Stage Pipeline" (new slide 3):** horizontal block
  diagram with five `stage`-styled nodes (IF → ID → EX → MEM → WB) connected by
  `{Stealth}` arrows, with grey label text below each node.
- **TikZ Diagram 2 — "Worked Example: RAW Hazard & Forwarding" (new slide 6):**
  two side-by-side timing grids: an 8-cycle grid (I1 + I2 with 2 red `stl` cells at
  cycles C4–C5) and a 6-cycle grid (I1 + I2 with a green dashed `fwdarr` from
  `i1ex.south` to `i2ex.north`); plus a `\begin{tabular}` step-by-step table
  comparing both cases across 8 columns.
- The tabular conclusion: **without forwarding → 2 stalls (8 cycles);
  with forwarding → 0 stalls (6 cycles) → 25% speedup**.
- PDF size grew from 103 KB to **136 KB** (embedded TikZ vector graphics).
  Slide count increased from **8 to 10**.

**Pedagogical gap closed:** `v2.tex` explained hazards through analogies and words
alone but provided no visual model of concurrent stage execution. A student could
understand that a stall "freezes the front of the pipeline" without being able to see
*which cycle that freeze occurs in* or *how many cycles are wasted*. The TikZ timing
grids make the cycle-by-cycle progression concrete and countable: the reader can point
to the two red `--` cells and immediately see the 2-cycle cost. The worked example
tabular provides the numerical precision needed to verify one's own calculations.

---

### v3 → v4_final (Iteration 3)

**Strategy:** "Final pedagogical polish — add learning objectives, navigation, intuition
blocks, real-world context, edge cases, and a self-test."

**Changes made:**
- Switched Beamer theme from **Madrid** to **Metropolis**
  (`\usetheme{metropolis}`, `\metroset{sectionpage=none, subsectionpage=none,
  progressbar=frametitle}`), giving a cleaner sans-serif layout with a thin
  per-slide progress bar.
- Added an author note via `\institute`: "Generated with AI assistance, refined
  over 4 iterations."
- **New slide 2 — "Learning Objectives":** three `\enumerate` goals using
  Bloom's taxonomy verbs: *Identify* (hazard classes + analogies), *Apply*
  (forwarding/stall calculation), *Compare* (mitigation strategies).
- **New slide 3 — "Outline":** `\tableofcontents` populated by five `\section{}`
  commands — *What is Pipelining?*, *Data Hazards*, *Structural & Control Hazards*,
  *Mitigation Techniques*, *Summary* — compiled twice for cross-reference resolution.
- Added **6 `\begin{block}{Intuition}…\end{block}`** blocks at the end of all six
  theoretical slides (Introduction, Data Types, Data Detection, Structural,
  Control, Mitigation Summary), each distilling the core insight in 1–2 sentences.
- **New slide 13 — "Real-World Context":** three bullets connecting theory to
  practice — modern x86 (Tomasulo/register renaming, >98% branch prediction accuracy),
  ARM Cortex-A53 (in-order) vs. A76 (out-of-order), and GPU SIMT warp-switching as
  an alternative latency-hiding strategy.
- **New slide 14 — "Summary & Common Pitfalls" (final):** 3 summary bullets,
  2 misconceptions (*"forwarding solves all data hazards"* and *"deeper pipelines
  are always faster"* — with the Pentium 4 Prescott 31-stage counter-example),
  and a `\begin{alertblock}{Test Yourself}` presenting an unresolved load-use
  puzzle across three instructions.
- PDF size grew from 136 KB to **153 KB**. Slide count increased from **10 to 14**.

**Final polish added:** The deck now has a complete pedagogical arc. Learning
Objectives frame the session upfront; the ToC provides navigational structure;
Intuition blocks give the "why it matters" insight after each formal definition;
Real-World Context answers the "so what?" question; and the Summary/Pitfalls slide
consolidates key facts while actively challenging the reader. The Metropolis theme
gives the final version a visual identity distinct from the draft versions.

---

## 4. Before vs After

**Initial output (`v1.tex`) weaknesses:**
- **No visual representation:** pipeline stages, timing diagrams, and hazard effects
  were described entirely in text. The concurrent execution of multiple instructions
  across stages — the defining property of pipelining — was impossible to grasp
  without a diagram.
- **Dense technical jargon with no scaffolding:** terms like "IPC ≈ 1",
  "EX/MEM and MEM/WB pipeline registers", "BTFN (backward-taken, forward-not-taken)"
  appeared without explanation or analogy, making the slides inaccessible to students
  encountering these concepts for the first time.
- **No pedagogical architecture:** no learning objectives, no outline, no summary,
  no self-test. The slides were a flat enumeration of facts with no structure to guide
  what a student should take away, check, or remember.

**Final version (`v4_final.tex`) strengths:**
- **Full visual layer:** two TikZ diagrams (the IF→ID→EX→MEM→WB pipeline block
  diagram and the before/after timing grids with a green forwarding arrow) make
  hazard mechanics immediately visible; the `\begin{tabular}` table provides
  numerical verification.
- **Three-layer pedagogical architecture:** Learning Objectives → structured content
  with Intuition blocks → Summary & Common Pitfalls creates a complete lesson with a
  clear entry, body, and consolidation phase.
- **Industrial grounding:** the Real-World Context slide connects textbook theory to
  modern x86 out-of-order execution, ARM Cortex micro-architectures, and GPU SIMT
  warp-switching — answering "why does this matter?" with concrete industrial examples.

**Comparison table:**

| Dimension | v1 | v4\_final |
|---|---|---|
| Slide count | 7 | 14 |
| TikZ diagrams | 0 | 2 |
| Worked example | none | RAW hazard timing grids + `\begin{tabular}` table |
| Analogy | none | 6 (restaurant, relay race, traffic officer, loading dock, GPS, factory supervisor) |
| Learning Objectives | none | yes (`\begin{enumerate}`, 3 Bloom's-verb goals) |
| Intuition blocks | 0 | 6 (`\begin{block}{Intuition}`) |
| Sections / ToC | none | 5 `\section{}` commands + `\tableofcontents` |
| Beamer theme | Madrid | Metropolis (`progressbar=frametitle`) |
| Real-World Context | none | x86, ARM Cortex-A53/A76, GPU SIMT |
| Common pitfalls | none | 2 misconceptions + Pentium 4 counter-example |
| Self-test | none | `\begin{alertblock}{Test Yourself}` |
| PDF size | 99 KB | 153 KB |
