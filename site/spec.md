# ACP Selection Specification

## 1. Objective

Define a repeatable selection mechanism for evaluating candidates under uncertainty.

---

## 2. Selection Dimensions

| Dimension     | Description |
|--------------|------------|
| Performance   | Output quality / efficiency |
| Cost          | Resource consumption |
| Stability     | Variance across scenarios |
| Scalability   | Ability to grow |

---

## 3. Scoring Model

Each candidate is scored using weighted evaluation:

Score =  (weight_i × metric_i)

---

## 4. Decision Rule

- Select top-scoring candidate
- If variance > threshold  trigger re-evaluation
- If no candidate meets baseline  abandon

---

## 5. Output

Selection must produce:

- Selected candidate
- Score breakdown
- Decision rationale