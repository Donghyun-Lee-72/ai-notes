# Workflows and Agents

An LLM workflow follows an application-defined sequence of steps. An agent
allows a model or another policy to choose some steps at runtime. The boundary
is a spectrum: most reliable systems combine deterministic structure with
bounded adaptive decisions.

## Prefer a Workflow When

- the required steps and order are known;
- each transition can be validated directly;
- reproducibility and auditability dominate flexibility;
- the operation has meaningful side effects;
- predictable latency and cost are important.

Common patterns include sequential pipelines, routing among fixed branches,
parallel map-reduce, and evaluator-optimizer loops with a strict retry limit.

## Prefer Bounded Agency When

- relevant information must be discovered iteratively;
- the next useful tool depends on an observation;
- the task path cannot be enumerated economically;
- recovery requires selecting among several alternatives.

Agency should still have an action allowlist, budgets, a stopping rule, and
observable success criteria. "Continue until done" is not a sufficient control
policy.

## Hybrid Design

A practical hybrid uses a deterministic outer workflow to authorize inputs,
set budgets, and verify results. An agent operates only within one bounded step,
then returns typed output to the workflow. This reduces the state space that
must be evaluated while preserving adaptation where it matters.

## Related

- [AI Agents](ai-agents.md)
- [Tool Use and Function Calling](tool-use-and-function-calling.md)
- [Structured Output](structured-output.md)
