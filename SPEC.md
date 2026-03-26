# ACP Specification v0.1

## Normative Language

The key words "MUST", "SHOULD", and "MAY" are defined as in RFC 2119.

---

## Selection Definition

A selection MUST satisfy:

1. Reuse
2. Downstream usage
3. Choice among alternatives

Otherwise:

selected MUST be false

---

## Schema

{
  "agent_id": "string",
  "execution_id": "string",
  "selected": true,
  "selector": "user | system | multi",
  "selection_type": "repeat | downstream | alternative",
  "timestamp": "ISO8601"
}
