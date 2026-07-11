# AI Agents

An AI agent is a system that pursues a goal by maintaining state, selecting
actions, observing results, and deciding whether to continue. An LLM may supply
part of the decision policy, but a model call by itself is not an agent.

## A Minimal Control Loop

1. Interpret the current goal and state.
2. Select an allowed action or produce a final response.
3. Validate and authorize the proposed action.
4. Execute it outside the model.
5. convert the result into an observation;
6. update state and test a stopping condition.

The application, not the model, owns permissions and execution. This separation
is essential because generated tool arguments can be incomplete, incorrect, or
unsafe.

## Agent, Workflow, and Hybrid System

A workflow follows transitions defined mostly in advance. An agent chooses some
transitions at runtime. Workflows are easier to test and audit; agents are more
adaptive when the necessary path cannot be enumerated beforehand. Reliable
applications often use a hybrid: deterministic routing and validation around a
bounded agentic loop.

Use the least autonomy needed for the task. If a fixed sequence can solve the
problem, an open-ended loop adds cost and failure modes without adding value.

## State and Memory

State is the information required for the current run: messages, completed
steps, tool observations, budgets, and pending decisions. Longer-lived memory
may store user preferences, learned facts, or past outcomes. Both need schemas,
retention rules, provenance, and conflict handling. Replaying an entire history
into the prompt is not a complete memory design.

## Failure Modes

- repeated or circular tool use;
- premature stopping or endless continuation;
- selecting the wrong tool or malformed arguments;
- treating an untrusted observation as an instruction;
- losing constraints during summarization;
- exceeding cost, latency, or action budgets;
- reporting success without verifying the external state.

Bound the number of steps, tool scope, elapsed time, and spend. Require explicit
confirmation for consequential actions. Design idempotent operations where
possible, and verify completion from observable state rather than model prose.

## Evaluation

Measure task success, action correctness, unnecessary steps, recovery after
tool failure, policy compliance, latency, and cost. Preserve step-level traces
for evaluation, but avoid exposing private reasoning or sensitive tool output.
Test adversarial observations and ambiguous stopping conditions, not only ideal
happy paths.

## Further Reading

- [ReAct](https://arxiv.org/abs/2210.03629)
- [Toolformer](https://arxiv.org/abs/2302.04761)

## Related

- [Tool Use and Function Calling](tool-use-and-function-calling.md)
- [Structured Output](structured-output.md)
- [LLM Evaluation](../evaluate/llm-evaluation.md)
