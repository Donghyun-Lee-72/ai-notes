# Reranking

Reranking applies a more precise scoring method to a small set of candidates
returned by an initial retriever. It is common in search and RAG because a fast
first stage can maximize recall while a slower second stage improves ordering.

## Common Methods

- a cross-encoder that jointly reads the query and each candidate;
- a late-interaction model that compares token-level representations;
- a learned-to-rank model using semantic and metadata features;
- a model prompt that compares a very small candidate set.

Reranking cannot recover evidence absent from the candidate set. First-stage
recall therefore sets an upper bound on downstream performance.

## Design Questions

Choose the candidate count, scoring model, latency budget, batching strategy,
and final context size together. Preserve document diversity when several
sources are required. Deduplicate overlapping chunks so the context is not
filled by near-identical passages from one document.

## Evaluation

Compare ranking metrics before and after reranking, then measure end-to-end
answer quality. Include hard negatives that share vocabulary or topic but do
not support the answer. Record latency and cost because a small quality gain may
not justify a large operational penalty.

## Related

- [Retrieval-Augmented Generation](retrieval-augmented-generation.md)
- [Embeddings](../learn/embeddings.md)
- [RAG Evaluation](../evaluate/rag-evaluation.md)
