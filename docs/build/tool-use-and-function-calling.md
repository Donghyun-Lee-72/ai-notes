# Tool Use and Function Calling

Tool use lets an LLM-backed application request an external capability such as
search, calculation, code execution, or a database query. Function calling is
an interface in which the model selects a named operation and proposes typed
arguments. The host application decides whether to execute it.

## Trust Boundary

Model output is untrusted input. A safe execution path is:

1. expose only tools needed for the current task;
2. parse the proposed call against a schema;
3. validate values and enforce authorization in code;
4. request user confirmation when consequences require it;
5. execute with the narrowest available permissions;
6. return a concise, typed observation;
7. verify external state before reporting completion.

Prompt instructions are not an authorization system. A tool description can
help the model choose correctly, but access control must be enforced outside the
model.

## Tool Contract Design

A tool needs a precise name, purpose, input schema, output shape, error model,
and side-effect description. Prefer separate read and write operations. Make
retries safe through idempotency keys or state checks when possible. Large raw
results should be filtered or summarized by trusted application logic before
returning to the context.

## Failure Modes

- wrong tool selection;
- missing, invented, or type-correct but invalid arguments;
- prompt injection contained in retrieved tool output;
- duplicate writes after a timeout and retry;
- stale observations;
- a successful API response that does not achieve the user goal.

Evaluate both selection and execution. Include unavailable tools, permission
denials, ambiguous requests, malformed responses, and partial failures in the
test set.

## Further Reading

- [Toolformer](https://arxiv.org/abs/2302.04761)
- [ReAct](https://arxiv.org/abs/2210.03629)

## Related

- [AI Agents](ai-agents.md)
- [Structured Output](structured-output.md)
- [Pydantic](../tools/pydantic.md)
