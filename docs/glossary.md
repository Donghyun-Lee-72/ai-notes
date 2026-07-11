# Glossary

## Agent

A system that pursues a goal through state, action selection, observations, and
stopping conditions. See [AI Agents](build/ai-agents.md).

## Attention

A mechanism that computes context-dependent combinations of value vectors using
weights derived from query-key similarity. See [Transformers](learn/transformers.md).

## Chunk

A retrievable unit created from a larger document. Chunk boundaries affect both
retrieval precision and the amount of surrounding context preserved.

## Context Window

The tokenized information a model can process for one generation, including
input and reserved output. See [Context Windows](learn/context-windows.md).

## Embedding

A vector representation optimized so a chosen similarity function reflects
useful relationships for a task. See [Embeddings](learn/embeddings.md).

## Grounding

Connecting generated claims to inspectable evidence or verified external state.
See [Grounding and Hallucination](evaluate/grounding-and-hallucination.md).

## Hallucination

Fluent output that is false, unsupported, or misleading in its use context.

## Large Language Model (LLM)

A neural model trained to estimate distributions over token sequences. See
[Large Language Models](learn/large-language-models.md).

## Prompt

The instructions, data, examples, and output requirements supplied to a model
for a generation. See [Prompting](learn/prompting.md).

## RAG

Retrieval-augmented generation: retrieving external evidence and including a
selected subset in the generation context. See
[Retrieval-Augmented Generation](build/retrieval-augmented-generation.md).

## Reranker

A model or scoring stage that reorders a limited candidate set produced by an
initial retriever. See [Reranking](build/reranking.md).

## Structured Output

Model output constrained to a machine-readable contract such as JSON Schema or
a typed record. See [Structured Output](build/structured-output.md).

## Token

A discrete identifier produced by a tokenizer and processed by a model. It may
represent a word, subword, symbol, whitespace, or bytes. See
[Tokenization](learn/tokenization.md).

## Tool Use

A controlled interface through which a model-backed application requests an
external function or service. See
[Tool Use and Function Calling](build/tool-use-and-function-calling.md).

## Vector Database

A database or search system that stores embeddings and supports nearest-
neighbor retrieval. See [Vector Databases](tools/vector-databases.md).
