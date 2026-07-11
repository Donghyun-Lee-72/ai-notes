# Pydantic

Pydantic is a Python library for validating data from type annotations. It is
useful at LLM application boundaries: structured model outputs, tool arguments,
retrieved metadata, configuration, and API records.

## Basic Model

```python
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

class SearchRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(min_length=1, max_length=500)
    top_k: int = Field(default=5, ge=1, le=20)
    mode: Literal["lexical", "semantic", "hybrid"] = "hybrid"
```

`extra="forbid"` rejects undeclared fields, while constraints bound values
before downstream use. The model can also emit JSON Schema for function-calling
or structured-output interfaces.

## Validation Is Not Authorization

A valid object has the expected shape; it is not necessarily safe or correct.
A valid path may still target a forbidden resource, and a plausible citation ID
may not exist. Enforce permissions and domain invariants in application code.

Avoid broad coercion where it could hide an error. Define whether extra fields,
string-to-number conversion, and unknown enum values should be rejected. Return
validation feedback carefully: errors may help a bounded retry, but raw internal
details should not be exposed to an end user.

## Version Note

Pydantic v2 introduced new APIs and behavior compared with v1. Confirm the
major version used by a project and consult current official documentation
rather than mixing examples across versions.

## Further Reading

- [Pydantic documentation](https://docs.pydantic.dev/)
- [Pydantic JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)

## Related

- [Structured Output](../build/structured-output.md)
- [Tool Use and Function Calling](../build/tool-use-and-function-calling.md)
