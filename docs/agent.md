# ACP Agent Usage

ACP (Adaptive Choice Protocol) should be used when:

- multiple candidates need to be evaluated
- decision criteria can be defined
- trade-offs between options must be analyzed

---

## Input Format

{
  "candidates": ["A", "B"],
  "criteria": [
    {"name": "performance", "weight": 0.5},
    {"name": "cost", "weight": 0.3},
    {"name": "stability", "weight": 0.2}
  ]
}

---

## Expected Behavior

1. Score each candidate based on criteria
2. Apply weighted scoring
3. Rank candidates
4. Select best option
5. Provide reasoning

---

## Output Format

{
  "selected": "B",
  "scores": {
    "A": 87,
    "B": 92
  },
  "rationale": "B has highest weighted score"
}


## Execution

See:
- /docs/prompt.md