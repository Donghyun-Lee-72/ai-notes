# Vector Databases

A vector database or vector-capable search engine stores embeddings and
supports nearest-neighbor search. It commonly also stores identifiers and
metadata used to filter, update, delete, and trace retrieved items.

## What the Index Does

Exact search compares a query with every vector. Approximate nearest-neighbor
(ANN) indexes trade some recall for lower latency and memory use at scale.
Algorithms such as HNSW and inverted-file methods expose tuning parameters that
affect build time, query speed, memory, and retrieval recall.

The database does not determine whether an embedding is meaningful or a chunk
answers the question. Embedding quality, chunking, metadata, query formulation,
and reranking remain separate design choices.

## Operational Requirements

- stable external IDs and source provenance;
- model and index version metadata;
- consistent update and deletion semantics;
- access control before and after retrieval;
- backups or a reproducible rebuild process;
- monitoring for index lag and failed ingestion;
- lexical or hybrid search when exact terms matter.

Filtering after retrieval can produce too few usable results. When supported,
apply required authorization and collection filters within the search query.
Never rely on the model to ignore a retrieved item the user was not allowed to
see.

## Selecting a System

Start from corpus size, update rate, filtering needs, latency target, deployment
constraints, and measured retrieval quality. A simple in-process or relational
database extension may be enough for a small application. A specialized
distributed service is justified by operational requirements, not by RAG alone.

## Evaluation

Measure end-to-end retrieval quality and system performance separately. ANN
recall compares approximate results with exact nearest neighbors; task recall
compares results with human relevance judgments. Both can matter, but they
answer different questions.

## Related

- [Embeddings](../learn/embeddings.md)
- [Retrieval-Augmented Generation](../build/retrieval-augmented-generation.md)
- [RAG Evaluation](../evaluate/rag-evaluation.md)
