# Retrieval-Augmented Generation

Retrieval-augmented generation (RAG) retrieves external evidence and places a
selected subset in the model context before generation. It is useful when an
answer should depend on a changing, specialized, or inspectable collection
rather than model parameters alone.

RAG does not make an answer correct automatically. It creates an evidence path
that can be measured and improved.

## Pipeline

1. **Ingest:** collect documents with ownership and update rules.
2. **Parse:** preserve useful structure such as headings, tables, and pages.
3. **Chunk:** create retrievable units with stable metadata.
4. **Index:** build lexical, vector, or hybrid search structures.
5. **Retrieve:** generate candidates for a query.
6. **Rerank and filter:** improve precision and enforce metadata constraints.
7. **Assemble context:** remove duplicates and fit the token budget.
8. **Generate:** answer from the selected evidence.
9. **Cite and verify:** connect claims to the passages that support them.

## Retrieval Choices

Lexical search is strong for exact names, identifiers, and rare terms. Dense
retrieval can match semantic similarity despite different wording. Hybrid
retrieval combines both, while rerankers score a smaller candidate set more
carefully. Metadata filters can enforce date, collection, access, or document
type constraints before evidence reaches the model.

Chunking is part of retrieval quality. Small chunks can lose context; large
chunks can dilute the relevant passage and consume the context window. Evaluate
chunk size, overlap, structural boundaries, and parent-document expansion on
the actual corpus.

## Grounding and Citations

A citation should support the nearby claim, not merely concern the same topic.
Store stable document and passage identifiers so a reader can inspect the exact
evidence. When the collection does not support an answer, the system should say
so rather than use prior model knowledge without disclosure.

## Failure Analysis

Separate at least four cases:

- the needed source was absent from the collection;
- indexing or retrieval failed to surface it;
- context assembly dropped or obscured it;
- generation ignored, distorted, or overextended the evidence.

This decomposition makes RAG evaluation actionable. A single end-to-end score
cannot identify which layer needs improvement.

## Further Reading

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Dense Passage Retrieval](https://arxiv.org/abs/2004.04906)
- [BEIR](https://arxiv.org/abs/2104.08663)

## Related

- [Embeddings](../learn/embeddings.md)
- [Vector Databases](../tools/vector-databases.md)
- [Grounding and Hallucination](../evaluate/grounding-and-hallucination.md)
- [RAG Evaluation](../evaluate/rag-evaluation.md)
