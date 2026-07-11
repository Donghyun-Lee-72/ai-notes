# Grounding and Hallucination

Grounding connects generated claims to an authoritative context: supplied
documents, verified tool results, a database, or another inspectable source.
Hallucination is a broad label for fluent output that is false, unsupported, or
misleading in the setting where it is used.

## Distinguish the Failure

- **Factual error:** a claim conflicts with reality.
- **Unsupported claim:** the claim may be true, but the supplied evidence does
  not establish it.
- **Citation error:** a cited source exists but does not support the claim.
- **Attribution error:** content is assigned to the wrong source or speaker.
- **Overclaim:** the wording is stronger than the evidence permits.

These categories require different fixes. Retrieval may help with missing
knowledge, while validation or calibrated language may help with overclaiming.

## Grounded Generation Pattern

1. define the sources the answer is allowed to use;
2. retrieve evidence with stable identifiers;
3. ask for claims linked to specific evidence;
4. verify that each citation entails or supports the claim;
5. expose uncertainty, contradiction, and missing evidence;
6. abstain or narrow the answer when support is insufficient.

The presence of citations is not evidence of grounding. Citation correctness
must be checked at claim level. Instructions such as "do not hallucinate" are
helpful signals but are not enforcement mechanisms.

## Evaluation

Annotate atomic claims and the evidence that supports them. Measure citation
precision and coverage, test unanswerable questions, and include conflicting or
outdated sources. Deterministic verification is preferable when a claim can be
checked through code, a database constraint, or a trusted calculation.

## Further Reading

- [TruthfulQA](https://arxiv.org/abs/2109.07958)
- [FActScore](https://arxiv.org/abs/2305.14251)

## Related

- [Retrieval-Augmented Generation](../build/retrieval-augmented-generation.md)
- [LLM Evaluation](llm-evaluation.md)
- [RAG Evaluation](rag-evaluation.md)
