# ACP Prompt Protocol

When ACP is triggered, use the following procedure:

---

## Step 1: Identify Candidates

List all options clearly.

---

## Step 2: Define Criteria

Identify evaluation dimensions such as:

- performance
- cost
- stability
- scalability

If not provided, infer or ask.

---

## Step 3: Score Each Candidate

Assign a score (0–100) for each criterion.

---

## Step 4: Apply Weights

Multiply scores by weights and compute total.

---

## Step 5: Rank Candidates

Sort candidates by total score.

---

## Step 6: Select Best Option

Choose highest scoring candidate.

---

## Step 7: Provide Rationale

Explain decision based on criteria and trade-offs.

---

## Output Format

Return structured result:

{
  "selected": "...",
  "ranking": [...],
  "scores": {...},
  "rationale": "..."
}