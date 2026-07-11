# LangChain and LangGraph

LangChain is an open-source ecosystem for composing model calls, prompts,
retrievers, tools, and output processing. LangGraph provides graph-based
orchestration for stateful workflows and agents. Their APIs evolve quickly, so
examples should be checked against the current official documentation.

## Different Roles

LangChain offers integrations and reusable components. LangGraph represents a
process as nodes, state, and transitions, including conditional and cyclic
flows. A graph makes control flow explicit, but it does not automatically make
an agent safe or reliable.

## Design Guidance

- keep domain data models independent of framework-specific objects;
- define state fields and reducers deliberately;
- separate pure computation from side-effecting tools;
- bound loops and retries;
- make checkpoints and resume semantics explicit;
- test nodes and transitions without requiring a live model when possible;
- retain application-level authorization around tool execution.

Framework abstractions are useful when they reduce repeated integration work or
make state transitions easier to inspect. A small direct implementation can be
clearer for a short fixed pipeline. Select a framework after defining the
control flow, not as a substitute for defining it.

## Evaluation and Observability

Trace node inputs, typed outputs, tool results, errors, and final outcomes while
redacting sensitive data. Evaluate the graph with simulated failures and
deterministic test doubles. A successful node execution is not necessarily a
successful user outcome.

## Further Reading

- [LangChain documentation](https://python.langchain.com/docs/)
- [LangGraph documentation](https://langchain-ai.github.io/langgraph/)

## Related

- [AI Agents](../build/ai-agents.md)
- [Workflows and Agents](../build/workflows-and-agents.md)
- [Retrieval-Augmented Generation](../build/retrieval-augmented-generation.md)
