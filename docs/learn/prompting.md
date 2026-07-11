# Prompting

Prompting specifies a task through instructions, context, examples, and an
expected response format. It is one layer of application design. Prompt wording
can improve behavior, but it cannot enforce permissions, guarantee facts, or
replace validation.

## A Practical Prompt Structure

1. State the task and intended audience.
2. Separate instructions from untrusted input and reference material.
3. Define constraints and what to do when information is missing.
4. Specify the output schema or evaluation criteria.
5. Include examples only when they clarify a real ambiguity.

Clear delimiters help distinguish data from instructions, but they do not make
untrusted content safe. Retrieved documents and tool output can contain prompt
injection. The application must restrict available actions and enforce policy
outside the model.

## Examples and Decomposition

Few-shot examples can communicate labels, style, and boundary cases. They also
consume context and can bias the model toward accidental patterns. Use a small,
representative set and evaluate whether examples improve held-out tasks.

Complex tasks may benefit from decomposition into retrieval, extraction,
validation, and synthesis steps. Do not require hidden reasoning transcripts as
a reliability mechanism; evaluate the observable answer and intermediate data
that the application genuinely needs.

## Prompt Evaluation

Version prompts like code. Compare changes on a fixed evaluation set, including
ambiguous, adversarial, and unanswerable inputs. Measure task quality, format
validity, refusal behavior, latency, and token use. Re-run evaluation when the
model or surrounding context changes.

## Related

- [Context Windows](context-windows.md)
- [Structured Output](../build/structured-output.md)
- [Grounding and Hallucination](../evaluate/grounding-and-hallucination.md)
