# Context Windows

The context window is the amount of tokenized information a model can process
for one generation. It includes system and user instructions, conversation
history, retrieved documents, tool results, multimodal representations, and the
tokens produced as output. Provider conventions differ, so documentation must
be checked to determine whether a published limit combines input and output.

## Capacity Is Not Effective Use

A long supported context does not guarantee that every detail will influence
the answer equally. Evidence can be redundant, contradictory, or buried among
distractors. Position and formatting can affect whether the model uses a fact.
The "lost in the middle" finding illustrates that access to long context and
reliable use of long context are different properties.

## Context Engineering

Context engineering is the application-level process of deciding what the
model should see and how it should be represented. A practical policy may:

1. preserve high-priority instructions and the current user request;
2. retrieve evidence relevant to the present step;
3. summarize older interaction state while retaining exact critical facts;
4. compress verbose tool output into typed observations;
5. remove duplicate or stale content;
6. reserve enough space for the expected response.

Summaries are lossy and should not replace exact identifiers, numeric values,
citations, or constraints when those details matter. Durable application state
belongs in explicit storage, not only in a growing prompt.

## Evaluation

Test context strategies with realistic lengths and distractors. Measure answer
quality as relevant evidence moves to different positions. Include conflicting
sources, missing evidence, and prompts near the token limit. Record truncation
and selected evidence so failures can be reproduced.

## Further Reading

- [Lost in the Middle](https://arxiv.org/abs/2307.03172)

## Related

- [Tokenization](tokenization.md)
- [Prompting](prompting.md)
- [Retrieval-Augmented Generation](../build/retrieval-augmented-generation.md)
