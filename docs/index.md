# AI Notes

AI Notes is a public guide to the concepts and engineering patterns behind
language-model applications. The goal is not to collect every new framework or
model release. It is to build a durable map of the ideas that remain useful
across implementations: tokens and attention, context and retrieval, tools and
state, validation and evaluation.

## Choose a Learning Path

### Understand the model layer

Start with [Large Language Models](learn/large-language-models.md), then read
[Tokenization](learn/tokenization.md), [Transformers](learn/transformers.md),
and [Context Windows](learn/context-windows.md). These pages explain what the
model consumes, how it mixes information, and why application-level context
management matters.

### Build a grounded application

Read [Embeddings](learn/embeddings.md),
[Retrieval-Augmented Generation](build/retrieval-augmented-generation.md), and
[Vector Databases](tools/vector-databases.md). Follow with
[RAG Evaluation](evaluate/rag-evaluation.md) before choosing an indexing or
retrieval stack.

### Build a controlled agent

Begin with [AI Agents](build/ai-agents.md), then connect
[Tool Use and Function Calling](build/tool-use-and-function-calling.md) with
[Structured Output](build/structured-output.md). The key theme is that an LLM
may propose actions, but application code owns validation, authorization,
execution, and stopping.

### Measure reliability

[Grounding and Hallucination](evaluate/grounding-and-hallucination.md) explains
the evidence problem. [LLM Evaluation](evaluate/llm-evaluation.md) introduces a
layered evaluation strategy, while [RAG Evaluation](evaluate/rag-evaluation.md)
separates retrieval failures from generation failures.

## How to Read These Notes

Each page aims to answer five questions:

1. What is the concept?
2. How does it work?
3. Which design choices matter?
4. How does it fail?
5. How should it be evaluated?

Use the [Glossary](glossary.md) for quick definitions and
[References](references.md) for primary papers and official documentation.
