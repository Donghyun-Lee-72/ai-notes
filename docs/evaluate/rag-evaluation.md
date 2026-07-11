# RAG Evaluation

RAG evaluation asks two different questions: did the system retrieve the
evidence needed for the task, and did the generated answer use that evidence
correctly? Evaluating only the final response hides the layer that failed.

## Retrieval Evaluation

Create queries with judged relevant passages or documents. Common metrics
include:

- **Recall@k:** fraction of relevant items found in the first `k` results.
- **Precision@k:** fraction of the first `k` results that are relevant.
- **MRR:** reciprocal rank of the first relevant result, averaged over queries.
- **nDCG:** ranking quality when relevance has grades rather than a binary label.

Document-level recall can look good while the precise supporting passage is
missing. Evaluate at the granularity used for context assembly. Slice results
by query type, document type, recency, language, and answerability.

## Generation Evaluation

- **Correctness:** the answer is accurate for the task.
- **Faithfulness:** its claims follow from the supplied evidence.
- **Completeness:** it covers the important supported parts of the answer.
- **Citation precision:** cited evidence supports the associated claim.
- **Citation recall:** claims requiring support have appropriate citations.
- **Abstention:** the system recognizes insufficient or conflicting evidence.

Answer correctness and faithfulness are not identical. An answer may be true
from general knowledge yet unsupported by the retrieved context; it may also
faithfully repeat evidence that is outdated or wrong.

## Diagnostic Experiments

Run an oracle-context test by supplying known relevant evidence directly. If
generation still fails, retrieval is not the only bottleneck. Conversely, test
the retriever without generation. Add distractors, near-duplicates,
contradictory sources, unanswerable questions, and queries requiring several
pieces of evidence.

Evaluate the complete ingestion pipeline after parser, chunking, embedding, or
index changes. Use versioned datasets so improvements are reproducible rather
than impressions from a few demonstrations.

## Further Reading

- [BEIR](https://arxiv.org/abs/2104.08663)
- [RAGAS](https://arxiv.org/abs/2309.15217)
- [ARES](https://arxiv.org/abs/2311.09476)

## Related

- [Retrieval-Augmented Generation](../build/retrieval-augmented-generation.md)
- [Grounding and Hallucination](grounding-and-hallucination.md)
- [Vector Databases](../tools/vector-databases.md)
