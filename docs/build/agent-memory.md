# Agent Memory

Agent memory is persisted information that can influence later decisions.
Conversation history is one possible input, but memory is better understood as
a system of storage, selection, updating, and forgetting.

## Memory Types

- **Working state:** information needed during the current run.
- **Episodic memory:** records of prior events or task outcomes.
- **Semantic memory:** consolidated facts or concepts.
- **Procedural memory:** reusable strategies, rules, or workflows.

These labels describe functions rather than mandatory databases. A single
system may implement them with structured records, documents, summaries, or a
search index.

## Memory Lifecycle

1. identify a candidate worth retaining;
2. validate its source and allowed retention scope;
3. store it with time, provenance, and confidence;
4. retrieve only when relevant;
5. resolve conflicts and superseded values;
6. expire or delete information according to policy.

Unfiltered automatic memory can preserve errors, sensitive information, or
prompt injection. Retrieval relevance is also not truth: a matching record may
be stale or belong to a different user or task.

## Evaluation

Test whether memory improves future task success without leaking information or
amplifying obsolete facts. Include contradictory updates, deletion requests,
similar users, long delays, and irrelevant but highly similar records. Measure
precision of retrieval as well as recall.

## Related

- [AI Agents](ai-agents.md)
- [Context Windows](../learn/context-windows.md)
- [Embeddings](../learn/embeddings.md)
