# Part 1: Academic Background & Course Preferences

## Perceived Strengths (Top 3 Easy Courses)

| Course Name | Grade | Reason |
|-------------|-------|--------|
| Numerical Methods | BA | I could visualize the numerical methods |
| Linear Algebra | BA | Step-by-step matrix applications |
| OOP | BB | Clear real-world analogies |

---

## Perceived Challenges (Top 3 Difficult Courses)

| Course Name | Grade | Reason |
|-------------|-------|--------|
| Digital Circuits | CB | Digital Circuit analogies |
| Computer Organization | CC | First Assembly experience |
| Computer Architecture | CB | Pipelining/caching hard to visualize |

---

## Selected Sub-topic: **Pipelining Hazards**

### Why this was difficult for me

Pipelining Hazards was one of the most challenging topics I encountered in Computer Architecture because the problem is fundamentally invisible — unlike a wrong formula result, a data hazard silently corrupts execution, making it hard to develop intuition without careful cycle-by-cycle tracing. The five-stage pipeline (IF-ID-EX-MEM-WB) made sense in isolation, but reasoning about multiple instructions overlapping in different stages simultaneously stretched my mental model well beyond what I was used to in sequential programming. Structural hazards, data hazards (RAW, WAW, WAR), and control hazards each required a different mitigation strategy — stalls, forwarding, or branch prediction — and keeping all three straight while also calculating stall counts felt like juggling too many moving parts at once. What finally helped was drawing out the pipeline as a time-step grid on paper, which is exactly the kind of visual scaffold I needed but that the course lacked.
