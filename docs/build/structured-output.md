# Structured Output

Structured output asks a model to produce data that conforms to a machine-
readable contract, commonly JSON Schema, typed records, or function-call
arguments. It replaces fragile prose parsing with an explicit interface, but it
does not guarantee that the values are true or safe.

## Three Validation Layers

1. **Syntactic validation** checks whether the result can be parsed.
2. **Schema validation** checks required fields, types, ranges, and enums.
3. **Semantic validation** checks domain rules, evidence, and authorization.

A record can pass the first two layers while containing a fabricated citation
or an impossible quantity. Domain checks remain application responsibilities.

## Design Principles

- Use the smallest schema that represents the decision.
- Distinguish missing, unknown, and not applicable values.
- Constrain categories with enums when the set is genuinely closed.
- Add descriptions for fields whose meaning is ambiguous.
- Keep user-facing explanations separate from machine-action fields.
- Version schemas when downstream consumers depend on them.

When validation fails, retry with the error and the original evidence only when
the operation is safe and bounded. Do not silently coerce a value whose meaning
changes. Preserve validation errors for evaluation.

## Example with Pydantic

```python
from typing import Literal
from pydantic import BaseModel, Field

class EvidenceClaim(BaseModel):
    claim: str = Field(min_length=1)
    evidence_id: str = Field(min_length=1)
    confidence: Literal["low", "medium", "high"]
```

The schema checks shape and allowed labels. Application code must still verify
that `evidence_id` exists and that the cited passage supports `claim`.

## Related

- [Pydantic](../tools/pydantic.md)
- [Tool Use and Function Calling](tool-use-and-function-calling.md)
- [Grounding and Hallucination](../evaluate/grounding-and-hallucination.md)
