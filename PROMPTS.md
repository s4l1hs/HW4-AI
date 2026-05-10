# PROMPTS.md — BLG 483E Quiz 4 (Part I) Completion Guide

---

## 0. Assignment Overview

The assignment has 5 main parts:

| Part | Content | Deliverable |
|---|---|---|
| Part 1 | Academic Background & Course Preferences (Top-3 Easy/Difficult tables) | Filled tables |
| Part 2 | Pick a difficult topic → generate 6-8 LaTeX Beamer slides with AI → 3-5 iterations (v1, v2, v3, ...) → upload to Ninova | `v1.tex` … `vN.tex` (final) + Prompt Engineering Log |
| Part 3 | Compare with instructor's sample slides (Chinese Room, Rice's Theorem, **Convolution**) | 5-point analysis |
| Part 4 | Quality Assurance: 2 verification questions + 1 Decompression prompt | Quiz + decompression prompt |
| Part 5 | Feedback on AI Synthesis + a "Golden Rule" prompt | Reflective writing |

> ⚠️ **Important constraint:** **Do NOT pick Convolution** as your topic — that's the instructor's example. Choose something else: Eigenvalues, Paging, Red-Black Trees, Dynamic Programming, Caching, Pipelining, Pointers, Recursion, Lambda Calculus, etc.

---

## 1. Preparation (Manual — You Do This)

Before starting the Claude Code session, decide the following **for yourself**:

### 1.1 Top 3 Easy Courses 
| Course | Grade | Why it felt easier |
|---|---|---|
| Numerical Methods | BA | I could visualize the numerical methods |
| Linear Algebra | BA | Step-by-step matrix applications |
| OOP | BB | Clear real-world analogies |

### 1.2 Top 3 Difficult Courses
| Course | Grade | Why it was difficult |
|---|---|---|
| Digital Circuits | CB | Digital Circuit analogies |
| Computer Organization | CC | First Assembly experience |
| Computer Architecture | CB | Pipelining/caching hard to visualize |

### 1.3 Selected Sub-topic
> **Suggested topic:** `Pipelining (Hazards & Stalls)` — *from Computer Architecture; carries the visual + example + math triad nicely.*
> *Alternatives:* Eigenvalues, Red-Black Trees, Dynamic Programming, Paging, Lambda Calculus, Markov Chains.

> Throughout this file, the placeholder **`{TOPIC}` = "Pipelining Hazards"**; do a global find-and-replace for your own topic.

---

## 2. Folder Structure (Claude Code Will Create This)

```
quiz4-part1/
├── PROMPTS.md                  # this file
├── README.md                   # project overview
├── part1_courses.md            # Part 1 tables
├── slides/
│   ├── v1.tex                  # initial draft
│   ├── v2.tex                  # iteration 1
│   ├── v3.tex                  # iteration 2
│   ├── v4_final.tex            # final (upload to Ninova)
│   ├── build/                  # pdf outputs
│   └── images/                 # tikz/png assets
├── prompt_engineering_log.md   # Part 2.1
├── part3_comparative_analysis.md
├── part4_qa_quiz.md
├── part5_feedback.md
└── final_report.docx           # if Ninova requires single document
```

---

## 3. PROMPTS — To Be Given to Claude Code in Order

Paste these prompts **sequentially** into Claude Code, each as a separate
message. Each prompt is tagged **[PROMPT N]**; send only the text inside
the gray code block under the tag.

---

### [PROMPT 1] — Project Skeleton & Part 1

```
I'm preparing the BLG 483E Quiz 4 Part I assignment. Please do the following:

1. In my working directory, create a top-level folder named `quiz4-part1/`,
   with subfolders `slides/`, `slides/build/`, and `slides/images/`.

2. Write `quiz4-part1/README.md` with:
   - Assignment name, course (BLG 483E), CRN (25311 / 25410)
   - One-line summary of each of the 5 parts (Part 1..5)
   - The folder tree

3. Create `quiz4-part1/part1_courses.md` with two Markdown tables:
   - "Perceived Strengths (Top 3 Easy Courses)": Course Name | Grade | Reason
   - "Perceived Challenges (Top 3 Difficult Courses)": Course Name | Grade | Reason

   Fill the tables with my real data:

   EASY:
   - Numerical Methods | BA | I could visualize the numerical methods
   - Linear Algebra | BA | Step-by-step matrix applications
   - OOP | BB | Clear real-world analogies

   DIFFICULT:
   - Digital Circuits | CB | Digital Circuit analogies
   - Computer Organization | CC | First Assembly experience
   - Computer Architecture | CB | Pipelining/caching hard to visualize

   At the bottom, add a section "Selected Sub-topic": **{TOPIC}**, followed
   by a "Why this was difficult for me" paragraph (3-4 sentences).

4. After finishing, show the folder structure with `tree` or `ls -R`.
```

---

### [PROMPT 2] — Slides v1 (Initial Generation — Naive Prompt)

```
Create the file quiz4-part1/slides/v1.tex.

Topic: Pipelining Hazards in CPU Architecture

This first version should be DELIBERATELY WEAK — because the assignment
requires demonstrating an "Iterative Refinement" process. Build it with
the following intentional weaknesses:
- Plain text only, no TikZ diagrams
- Dense technical jargon (not student-friendly)
- No real-world analogy
- No code or worked example
- 6 slides: title + 5 content slides

LaTeX requirements:
- documentclass{beamer}
- usetheme{Madrid}
- usepackage{amsmath, amssymb, listings, xcolor}
- \title{Understanding {TOPIC}}
- frames: \begin{frame}{...}\end{frame}
- Add a final references slide (even if empty)

After writing the file:
- Compile with pdflatex: `cd quiz4-part1/slides && pdflatex -output-directory=build v1.tex`
- If errors occur, fix the first one and recompile
- Confirm v1.pdf is generated under build/
- Finally, report the file size of `slides/v1.tex` and the slide count
```

---

### [PROMPT 3] — Slides v2 (Iteration 1 — "Explain it to a 10-year-old")

```
Create the file quiz4-part1/slides/v2.tex.

This is iteration 1 of v1.tex. Improvement strategy:
"Explain the core concepts as if you are talking to a 10-year-old."

Take v1 as the base and apply these changes:
1. Prepend EVERY technical concept with a one-sentence real-world analogy
   (e.g. for {TOPIC}: "Taking orders, cooking, and serving in a restaurant…
   if these didn't run in parallel, every order would take 30 minutes.
   CPU pipelining works exactly like that.")
2. Simplify jargon in parentheses
3. Split dense single slides into two
4. Final slide count should be 7-8

Consistency:
- Keep the SAME titles and section order as v1.tex
- Only simplify language and add analogies — don't change the structure

After writing, compile with `pdflatex -output-directory=build v2.tex`.
Fix any errors. Briefly report the difference in total slide count and
character count between v1.pdf and v2.pdf.
```

---

### [PROMPT 4] — Slides v3 (Iteration 2 — TikZ Diagram + Worked Example)

```
Create the file quiz4-part1/slides/v3.tex.

This is iteration 2 (built on v2.tex). Improvement strategy:
"Add at least 2 TikZ diagrams and one concrete numerical worked example."

Tasks:
1. Draw a TikZ diagram showing the topic's core mechanism
   (for {TOPIC}: the 5-stage pipeline IF-ID-EX-MEM-WB flow; an example
    Data Hazard).
   - Use tikzpicture, node[draw,rectangle], arrow chains.
   - Use color: stalls in red, normal cycles in blue.

2. Add a "before/after" comparison diagram
   (e.g. With hazard vs. resolved with forwarding).

3. Add a STEP-BY-STEP numerical worked example:
   - A table showing which instruction is in which stage for each cycle
   - At least 4 cycles long, in beamer with \begin{tabular}
   - Conclusion: "Without forwarding: X stalls, With forwarding: Y stalls"

4. Preserve all text from v2 — add the above as ADDITIONS.
   Slide count may exceed 8, but don't go over 10.

5. Add `\usepackage{tikz}` and `\usetikzlibrary{positioning,arrows.meta,shapes}`.

After writing, compile. TikZ compilation may take 1-2 seconds — be patient.
When done, list which new slides you added and which TikZ libraries you used.
```

---

### [PROMPT 5] — Slides v4_final (Final Iteration — Pedagogical Polish)

```
Create the file quiz4-part1/slides/v4_final.tex.

This is the final version. Improvement strategy:
"Final pedagogical polish: add learning objectives, summary, real-world
context, edge cases, and intuition pumps."

Take v3.tex as the base and ADD:

1. As slide 2, a "Learning Objectives" slide:
   - 3 objectives: "After this lecture, you will be able to: (1)... (2)... (3)..."

2. At the end of every theoretical slide in v3, add a small
   "🔑 Intuition" block (\begin{block}{Intuition}...\end{block}).

3. Second-to-last slide: "Real-World Context"
   - Where the topic appears in real systems
     (for {TOPIC}: modern x86, ARM Cortex, GPU SIMT, CUDA streams)
   - 2-3 bullets

4. Final slide: "Summary & Common Pitfalls"
   - 3 main summary bullets
   - 2 common misconceptions (edge cases)
   - A "Test yourself" subsection with 1 mini-question (don't give the answer)

5. Reconsider the Beamer theme: try Metropolis instead of Madrid
   (\usetheme{metropolis}); fall back to Madrid if Metropolis isn't installed.

6. On the title slide, add an author note: "Generated with AI assistance,
   refined over 4 iterations."

7. Place \tableofcontents as slide 2 or 3 (add \section{} commands as needed).

Compile: `pdflatex -output-directory=build v4_final.tex` (run twice so
\tableofcontents resolves correctly).

Then copy the PDF from `slides/build/` to `quiz4-part1/v4_final.pdf` in
the main folder (for Ninova upload).
```

---

### [PROMPT 6] — Prompt Engineering Log (Part 2.1)

```
Create the file quiz4-part1/prompt_engineering_log.md.

FILL the following sections (extract data by reading v1, v2, v3,
v4_final.tex under quiz4-part1/slides/):

# Prompt Engineering Log — {TOPIC}

## 1. Initial Prompt
[Paste the initial command used to generate v1.tex; a condensed version
of PROMPT 2 above. 4-6 lines.]

## 2. Design Choice
[Why this topic, why Beamer, why this structure? One paragraph, 5-7
sentences. Explain choices like "Madrid theme" / "text → visual → code
flow".]

## 3. Iterative Refinement Process
4 iterations were performed (v1 → v2 → v3 → v4_final). One subsection each:

### v1 → v2 (Iteration 1)
- Strategy: "Explain like to a 10-year-old"
- Changes made: (4-5 bullets)
- Which weakness of the previous version did it address?

### v2 → v3 (Iteration 2)
- Strategy: "Add TikZ diagrams + numerical worked example"
- Changes made: ...
- Which pedagogical gap did it close?

### v3 → v4_final (Iteration 3)
- Strategy: "Pedagogical polish + learning objectives + real-world context"
- Changes made: ...
- What final polish was added?

## 4. Before vs After
Initial output (v1) weaknesses:
- (3 bullets)
Final version (v4_final) strengths:
- (3 bullets)

Comparison table:
| Dimension | v1 | v4_final |
|---|---|---|
| Slide count | ... | ... |
| TikZ diagrams | 0 | ... |
| Worked example | none | ... |
| Analogy | none | ... |
| Learning Objectives | none | yes |

Write the entire log in English. Keep technical/LaTeX terms verbatim.
```

---

### [PROMPT 7] — Part 3: Comparative Performance Analysis

```
Create the file quiz4-part1/part3_comparative_analysis.md.

The instructor's sample slides cover Chinese Room, Rice's Theorem, and
Convolution. The Convolution example comes in 4 distinct styles:
- c-real-life.pdf (real-world analogy: detective + flashlight)
- code.pdf (Python/NumPy/PyTorch implementation)
- math.pdf (mathematical formulas, Toeplitz matrix)
- visual.pdf (TikZ diagrams)

Fill in the 5 sections below:

## 1. Communication Strategy
Which instructor slide was most effective? Identify its key pedagogical
elements (step-by-step explanation, visuals, examples). Briefly compare
with your own v4_final.tex. At least one paragraph, 6-8 sentences.

Suggested approach: "c-real-life.pdf was most effective because the
detective metaphor… In my own slides, I emulated this for {TOPIC} using
a restaurant-kitchen metaphor…"

## 2. Information Density (TikZ Prompt)
Pick one of your slides (the densest one). If you wanted to ADD a TikZ
diagram to it, what would your prompt be? Write the prompt as a code BLOCK:

```prompt
Generate a TikZ diagram showing ... with the following nodes ...
arrows ..., colors ..., position the kernel as ...
```

Explain which part was unclear without the diagram and how the diagram
resolves it.

## 3. Efficiency
Which part of your slides does the AI explain BETTER than a textbook?
Why? (Clearer examples? Better abstraction? Step-by-step structure?)
Brief comparison + one example excerpt.

## 4. Slide Improvement Challenge
Pick the MOST EFFECTIVE instructor slide. Write a refined prompt that
would improve it further. Specify the prompting technique used:
- Few-shot? Chain-of-Thought? Role-prompting? Constraint-prompting?

Provide the prompt in a code block.

## 5. Missing Piece
Identify a critical missing element in EITHER the instructor's slides
OR yours:
- Intuition pump? Real-world context? Edge case? Failure analysis?
How does this gap affect understanding?

Write the entire document in English.
```

---

### [PROMPT 8] — Part 4: Quality Assurance & Decompression

```
Create the file quiz4-part1/part4_qa_quiz.md.

# Part 4: Quality Assurance and Interactive Testing

## a) Verification Quiz (2 Questions)

### Question 1 — Visual/Table/Code Interpretation
[Write 1 question that REFERENCES a TikZ diagram or table inside v3.tex
or v4_final.tex. Format example:
"In the pipeline diagram on slide X, in cycle 3, which stage is register
R1 in? Does a stall occur?"]

**Expected Answer:**
[Explain in 2-3 sentences. Which slide/element produces this answer?]

### Question 2 — Logical Derivation / Calculation
[A non-trivial calculation. Example: "In the given 4-instruction sequence,
calculate the total stall count without forwarding, then compare with
forwarding enabled."]

**Expected Answer:**
[Step-by-step solution, at least 4 lines. Numerical result.]
[Why this answer is correct — derive it from a formula in your slides.]

## b) Decompression Task

Pick your most complex slide (likely the one with TikZ + table + formula).
Write its title here: **"<...>"**

Write a prompt that splits this slide into 3 STEPS:

```prompt
You are a teaching assistant. Take the following Beamer slide content:

<paste the original slide content here>

Split this into a 3-frame sequence for a complete beginner:
- Frame 1: Build only the visual intuition (no equations).
- Frame 2: Introduce the core formula with one symbol explained at a time,
  using progressive disclosure (\onslide<2->{} or \pause).
- Frame 3: Walk through ONE concrete numerical example, step by step,
  showing the substitution of each value into the formula.

Constraints:
- Use Madrid theme.
- Each frame max 6 lines of text.
- Add a "💡 Hint" block at the bottom of frames 2 and 3.
- Output valid LaTeX Beamer code only.
```

[Write the prompt verbatim. Then add a one-paragraph note: what kind of
output you would expect if you ran this prompt.]
```

---

### [PROMPT 9] — Part 5: Feedback on AI Synthesis

```
Create the file quiz4-part1/part5_feedback.md.

# Part 5: Feedback on AI Synthesis

## 1. Hardest Elements to Get the AI to Generate Correctly

Discuss these 3 areas:
- TikZ diagrams (coordinate errors, overlap, missing libraries)
- Mathematical notation (LaTeX issues with \mathbb, \cdots, align*
  misalignment)
- Pedagogical balance (too technical vs. too simple)

For each, 2-3 sentences: WHY was it hard?
(Ambiguity? Visualization difficulty? Training-data scarcity?)

## 2. Repeated AI Mistakes
What mistakes did the AI keep repeating during generation?
- Verbose explanations
- Missing examples
- Wrong abstraction level
- Outdated LaTeX package names
- Repetitive content
For each bullet, give one concrete example.

## 3. Golden Rule Prompt
If you could give ONE single prompt to a friend studying for a hard exam
with AI, what would it be? Provide the prompt in a code block, 5-8 lines,
including:
- Role-prompting (tell the AI who it is)
- Output format constraint
- "Explain in 3 layers: intuition → formal → example" structure
- Difficulty parameter
- Self-test directive

Example format:

```prompt
You are a {role}. Explain {topic} in three escalating layers:
1. ...
2. ...
3. ...

Constraints:
- ...
- After your explanation, generate 2 self-test questions ...
```

Then 2-3 sentences: Why is this prompt the "golden rule"? Which
pedagogical principles does it preserve?
```

---

### [PROMPT 10] — Final Build & Word Report

```
Do the following:

1. Re-compile quiz4-part1/slides/v4_final.tex one final time:
   `cd quiz4-part1/slides && pdflatex -output-directory=build v4_final.tex && pdflatex -output-directory=build v4_final.tex`
   Copy the PDF to `quiz4-part1/Final_Slides.pdf`.

2. Combine the following files into a single Word document:
   - part1_courses.md
   - prompt_engineering_log.md
   - part3_comparative_analysis.md
   - part4_qa_quiz.md
   - part5_feedback.md

   Word document name: `Quiz4_PartI_Report.docx`
   - Cover page: "BLG 483E — Quiz 4 Part I", name, ID, date
   - Each section starts on a new page
   - Use Word's default H1/H2/H3 heading styles
   - Insert an automatic table of contents at the very beginning
   - Footer with page numbers

   Use the docx skill (anthropic-skills:docx).

3. Final pre-submission checklist for Ninova:
   ✅ slides/v1.tex
   ✅ slides/v2.tex
   ✅ slides/v3.tex
   ✅ slides/v4_final.tex (final tex to upload)
   ✅ Final_Slides.pdf
   ✅ Quiz4_PartI_Report.docx
   ✅ PROMPTS.md (this file)

   Report this list, naming any files that are missing.

4. ZIP the output folder: `quiz4-part1.zip`
   Single shareable archive in the main folder.
```

---

## 4. Workflow — Quick Reference

```
PROMPT 1  →  project skeleton + Part 1 tables
PROMPT 2  →  v1.tex (weak draft)
PROMPT 3  →  v2.tex (simplification)
PROMPT 4  →  v3.tex (TikZ + worked example)
PROMPT 5  →  v4_final.tex (polish)
PROMPT 6  →  Prompt Engineering Log
PROMPT 7  →  Part 3 (Comparative Analysis)
PROMPT 8  →  Part 4 (QA Quiz + Decompression)
PROMPT 9  →  Part 5 (Feedback)
PROMPT 10 →  Final docx + zip
```

Expected total time: **2-3 hours** (5-15 min between prompts).

---

## 5. Notes & Tips

- **LaTeX errors:** Read Claude Code's log; start from the first error.
  `! Undefined control sequence` → missing package; `! Missing $` → math
  mode issue.
- **TikZ not rendering:** Add `\usetikzlibrary{positioning,arrows.meta,shapes,calc}`.
- **Metropolis theme missing:** Install with `tlmgr install beamertheme-metropolis`,
  or fall back to Madrid.
- **Iteration count:** The assignment requires at least 3, at most 5;
  4 iterations (v1→v2→v3→v4) is the sweet spot.
- **Switching topics:** Do a global find-and-replace for `{TOPIC}` and
  `Pipelining Hazards` in this file.
- **Ninova upload:** Each intermediate version (v2.tex, v3.tex) must be
  uploaded separately — not just the final.

---

## 6. Common Errors

| Error | Fix |
|---|---|
| `pdflatex: command not found` | `brew install --cask mactex-no-gui` or install TeX Live |
| `! LaTeX Error: File 'beamer.cls' not found` | `tlmgr install beamer pgf` |
| TikZ overlap | Increase `node distance=2cm` |
| Table overflow | Wrap with `\resizebox{\textwidth}{!}{...}` |
| Slide count over 8 | Move secondary details to appendix (`\appendix`) |

---

> **Final note:** As you paste these prompts into Claude Code in order,
> always verify the output of each one — especially that LaTeX compiled,
> the slide count is right, and the English text reads smoothly. Request
> small mid-step corrections when needed. Good luck! 🎓