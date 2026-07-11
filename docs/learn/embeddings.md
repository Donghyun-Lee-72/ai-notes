# Embeddings

An embedding is a fixed-length vector representation of an object such as a
text passage, image, molecule, or user query. Embedding models are trained so
that a chosen similarity function reflects useful relationships in the target
task. The vector is not a universal semantic coordinate; its meaning depends on
the model, training objective, input format, and domain.

## Similarity and Retrieval

Cosine similarity, dot product, and Euclidean distance are common comparison
functions. Their scores are not interchangeable, and a threshold from one
model or corpus should not be reused without validation. For retrieval, encode
documents and queries in the format expected by the model, then rank candidate
vectors using the matching metric.

Bi-encoder retrieval computes query and document vectors separately, making
large-scale search efficient. A cross-encoder jointly reads a query-document
pair and can score relevance more precisely, but it is usually too expensive
for the entire collection. Many systems retrieve broadly with embeddings and
rerank a smaller candidate set.

## Design Choices

- embedding model and version;
- domain and language coverage;
- chunk boundaries and surrounding context;
- vector normalization and distance metric;
- metadata filters;
- index update and deletion behavior;
- dimension, storage, latency, and cost.

Use the same embedding model for items compared in one vector space unless an
explicit alignment method is used. Re-embedding after a model change should be
treated as an index migration.

## Evaluation

Evaluate retrieval with labeled queries and relevant items. Include exact-term
queries, paraphrases, rare entities, negation, and hard negatives that are
topically similar but do not answer the question. Inspect performance by domain
and language rather than relying only on an aggregate score.

## Further Reading

- [Sentence-BERT](https://arxiv.org/abs/1908.10084)
- [Dense Passage Retrieval](https://arxiv.org/abs/2004.04906)

## Related

- [Vector Databases](../tools/vector-databases.md)
- [Retrieval-Augmented Generation](../build/retrieval-augmented-generation.md)
