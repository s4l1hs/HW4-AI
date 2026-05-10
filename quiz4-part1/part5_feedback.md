# Part 5: Feedback on AI Synthesis

---

## 1. Hardest Elements to Get the AI to Generate Correctly

### TikZ Diagrams

The core difficulty is that TikZ requires **exact coordinate arithmetic** that the AI
cannot verify without a compile step. For the timing grids in `v3.tex` and
`v4_final.tex`, every cell position had to be computed manually (x = 0.30 + 0.60 × n
for column n) — a prompt that says "draw a pipeline timing diagram" without specifying
coordinates produces nodes that overlap, spill outside the slide boundary, or use
inconsistent spacing. The forwarding arrow in the "With Forwarding" diagram required
explicit angle parameters (`to[out=-80, in=80]`): without them, a generic curved-path
instruction generates either a nearly-invisible tight curve or an overshooting arc that
exits the frame. A third failure mode is **silent library omission**: the `{Stealth}`
arrowhead in `harr/.style` and `fwdarr/.style` produces no arrowhead and no error
if `\usetikzlibrary{arrows.meta}` is missing — making bugs invisible until the PDF is
opened.

### Mathematical Notation

The most persistent LaTeX issue was **colour-scoping inside tabular environments**.
The `\textcolor{red}{--}` syntax correctly scopes colour to a single cell, but AI-
generated code often substitutes `{\color{red}--}`, which leaks colour to every
subsequent cell in the same row until the group closes — producing a red row instead of
two red cells. A second source of errors was inline math symbols outside math mode:
`≈`, `→`, and `⇒` pasted as Unicode characters fail silently or produce garbled output
in `pdflatex`; the correct forms `$\approx$`, `$\to$`, and `$\Rightarrow$` must be
explicit. The 8-column `\begin{tabular}` in the worked example additionally required
`\setlength{\tabcolsep}{3.5pt}` to prevent overflow — a micro-layout adjustment that
no generic AI prompt anticipates, because the AI has no model of the slide's physical
width.

### Pedagogical Balance

Calibrating the analogy-to-definition ratio in each iteration was difficult because the
AI's default is to **front-load the formal definition and append the analogy**, whereas
effective pedagogy reverses that order (analogy first, definition second, as a label
for something already understood). In `v1.tex`, bullets like "RAW (true dependence):
a consumer instruction attempts to read a register operand before the producer
instruction completes its WB stage" require prior familiarity with six technical terms
before the concept becomes accessible. The Intuition blocks in `v4_final.tex` presented
the opposite risk: condensing six slides' worth of content into 1–2 sentences each,
the AI's tendency is to **paraphrase the bullet points** ("Forwarding allows results to
bypass the register file") rather than distil the underlying insight ("Forwarding trades
extra wires for time — the load-use case is the one penalty no wiring can eliminate").

---

## 2. Repeated AI Mistakes

**Verbose explanations in bullet points.**
In `v1.tex`, every bullet was 2–3 lines long: *"RAW (true dependence): a consumer
instruction attempts to read a register operand before the producer instruction
completes its WB stage."* A beamer bullet should fit on one line; this reads like a
textbook paragraph. A human lecturer would write: *"RAW: instruction B reads a register
before instruction A finishes writing it."* The verbosity forced `\medskip` between
items just to create visual breathing room, compressing usable slide area.

**Missing concrete examples in the first draft.**
`v1.tex` generated five content slides without a single instruction pair (e.g.,
`ADD R1, R2, R3` followed by `SUB R4, R1, R5`). Every hazard was described at the
abstract level — "a consumer instruction," "a producer instruction" — with no instance
that bound the concept to actual registers and values. The worked example (with I1, I2,
and cycle-by-cycle tracking) only appeared in `v3.tex` after an explicit prompt
demanding a `\begin{tabular}` numerical example.

**Wrong abstraction level for the target audience.**
The Hazard Mitigation Summary in `v1.tex` used graduate-seminar language: *"The hazard
detection unit asserts a stall signal, holding PC and IF/ID registers constant while
inserting a bubble (NOP) into the ID/EX register."* For an undergraduate audience
encountering pipelining for the first time, this sentence assumes knowledge of PC
registers, pipeline register names, and signal assertion — none of which were defined
earlier in the slide deck. The audience mismatch persisted until `v2.tex` explicitly
targeted a "10-year-old" comprehension level.

**Speculative package loading in the LaTeX preamble.**
`v1.tex` loaded `\usepackage{listings}` without any `\lstset{}` configuration or
`\begin{lstlisting}` environment anywhere in the document. The `listings` package was
listed in the assignment requirements but served no purpose in `v1.tex`; AI-generated
preambles routinely include packages pre-emptively "in case they are needed," creating
unnecessary compilation overhead and potential conflicts (the `listings` First Aid
warning visible in the `v3.tex` compile log was a direct consequence of this pattern).

**Structurally repetitive Intuition blocks.**
Three of the six `\begin{block}{Intuition}` blocks in `v4_final.tex` follow the same
two-clause sentence structure: *"X is the only Y; Z vanishes when W."* / *"X adds Y;
Z is the one penalty no Y can eliminate."* / *"X patches runtime hazards; Y eliminates
compile-time ones."* While structural parallelism aids memory, the near-identical
sentence frames make the blocks feel formulaic rather than tailored to each concept's
specific insight. The Structural Hazards block ("Every structural hazard has one root
cause: more demand than supply") avoids this pattern and is noticeably sharper for it.

---

## 3. Golden Rule Prompt

```prompt
You are an expert computer science tutor who has taught [TOPIC] to undergraduate
students for 10 years. Explain [TOPIC] in three escalating layers:

1. Intuition — no jargon: Describe the concept using a single real-world analogy
   in 2-3 sentences of prose. Do not use any technical term a 12-year-old would
   not already know. Do not use bullet points in this layer.
2. Formal definition: State the precise definition, introducing each new technical
   term in parentheses the first time it appears. Max 4 bullet points.
3. Worked example: Walk through ONE concrete numerical example step by step,
   showing every intermediate value explicitly. Conclude with a one-sentence rule
   of thumb that a student can apply in an exam without re-reading the definition.

Constraints:
- Total response: max 300 words across all three layers.
- Layer 3 must include at least one numerical value or formula substitution.
- Difficulty level: [BEGINNER / INTERMEDIATE / ADVANCED] — calibrate vocabulary,
  example complexity, and assumed prior knowledge accordingly.
- After Layer 3, generate exactly 2 self-test questions at the specified difficulty
  level. Do NOT provide the answers — the reader must attempt them independently.
```

This prompt is the "golden rule" because it encodes two well-validated pedagogical
principles simultaneously. The three-layer structure mirrors **Bruner's spiral
curriculum**: intuition first (enactive representation), formal definition second
(symbolic representation), and a worked example third (which forces the student to
verify that the symbol system predicts the concrete outcome) — ensuring that no layer
is learned in isolation from the others. The "no answers" directive on the self-test
questions enforces **active retrieval** rather than passive re-reading: a student who
must generate an answer, even incorrectly, retains the material significantly longer
than one who reads a provided answer, a finding replicated across decades of cognitive
science research under the label of the testing effect. The difficulty parameter makes
the prompt reusable across all stages of exam preparation — running it at BEGINNER
level two weeks before an exam and at ADVANCED level the night before produces two
complementary study sessions from a single template.
