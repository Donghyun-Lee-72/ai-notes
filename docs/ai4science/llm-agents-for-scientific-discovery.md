# LLM Agents for Scientific Discovery

An **LLM agent for scientific discovery** is a system in which a large
language model helps decide what to do next in a scientific workflow. It may
search for evidence, formulate or compare hypotheses, design an experiment,
invoke software or instruments, interpret observations, and revise its plan.

The defining feature is not the amount of computation or the presence of an
LLM. It is a **goal-directed, adaptive decision loop** that connects scientific
evidence, actions, observations, and subsequent decisions.

## From automation to scientific agency

A fixed script can run thousands of simulations or screen a large candidate
library. This is valuable high-throughput computing, but the sequence of
operations was specified in advance. A scientific agent has some authority to
choose among actions based on the current state of the investigation.

For example, an agent may decide:

- which evidence is missing and where to search for it;
- which competing hypothesis best explains an observation;
- which experiment would distinguish between plausible hypotheses;
- whether a proposed experiment satisfies physical, operational, cost, and
  safety constraints;
- whether a failure indicates a software error, an instrument problem, an
  invalid procedure, or evidence against a hypothesis; and
- how a new observation should change the next experiment.

This distinction is gradual rather than binary. A system can automate one
stage, assist a human decision, or connect several stages with different
approval boundaries. It should be described according to the decisions it
actually makes, rather than labeled autonomous merely because it uses an LLM.

Simulation can be part of scientific agency. The relevant question is whether
the agent only launches a predetermined batch or uses intermediate results to
choose new calculations, revise a model, reject a hypothesis, or change the
search strategy.

## The scientific discovery loop

A general discovery workflow can be represented as:

1. **Question:** define the scientific objective, assumptions, and success
   criteria.
2. **Evidence:** retrieve relevant literature, datasets, prior experiments,
   and technical documentation.
3. **Hypothesis:** construct one or more explanations or candidate solutions
   consistent with the available evidence.
4. **Prediction:** state observable consequences that could support or
   contradict each hypothesis.
5. **Experiment design:** choose an informative and feasible intervention,
   simulation, or measurement.
6. **Execution:** invoke validated code, scientific software, databases, or
   laboratory equipment.
7. **Interpretation:** analyze the result while preserving units, conditions,
   uncertainty, and provenance.
8. **Revision:** update the hypotheses and select the next action or a stopping
   condition.

An LLM agent does not need to control every stage. In many scientific settings,
human approval should remain at consequential, hazardous, or weakly validated
steps. The useful question is which transitions the agent can perform reliably
and how those transitions are verified.

## Retrieval and evidence grounding

Retrieval-augmented generation (RAG) can connect an agent to scientific
literature, structured databases, laboratory records, safety information, and
equipment documentation. Retrieval is especially important because a model's
parametric memory may be incomplete, outdated, or unable to preserve the
conditions under which a result is valid.

Retrieval alone does not constitute scientific discovery. A system that finds
and summarizes papers is primarily a literature assistant. Retrieval becomes
part of a discovery agent when the evidence changes a downstream decision,
such as selecting a hypothesis, rejecting a candidate, choosing experimental
conditions, or identifying a necessary control.

Scientific retrieval also requires more than finding topically similar text.
A useful system should preserve:

- the source supporting each consequential claim;
- experimental conditions, units, population or material scope, and stated
  uncertainty;
- disagreement and incompatibility between sources;
- information in tables, equations, figures, supplementary material, and
  structured scientific databases;
- the distinction between retrieved evidence, model inference, and new
  observation; and
- provenance from a final decision back to the evidence and tool outputs that
  informed it.

These requirements make **evidence-grounded decision making** a more complete
description of the problem than RAG alone. Retrieval quality must ultimately
be evaluated by its effect on scientific decisions, not only by document
relevance or answer fluency.

## What scientific reasoning means

"Scientific reasoning" is too broad to serve as an evaluation claim by
itself. It should be divided into capabilities with observable consequences:

- **Abductive reasoning:** propose explanations that could account for an
  observation.
- **Deductive reasoning:** derive testable predictions from a hypothesis.
- **Causal reasoning:** distinguish predictive association from the effect of
  an intervention.
- **Constraint reasoning:** respect physical laws, domain rules, instrument
  limits, budgets, and safety boundaries.
- **Experimental reasoning:** select controls and measurements that can
  discriminate among competing hypotheses.
- **Uncertainty reasoning:** represent insufficient evidence, measurement
  uncertainty, model uncertainty, and alternative explanations.
- **Revision:** change a hypothesis or plan appropriately when contradictory
  evidence or failure is observed.

A plausible written explanation is not evidence that these capabilities are
present. Evaluation should test whether the proposed experiment is informative
and feasible, whether conclusions follow from the observations, whether
uncertainty is calibrated, and whether the plan changes appropriately under
counterfactual observations or tool failures.

## A minimal system architecture

An LLM-based scientific agent commonly combines several components:

1. A **state representation** records the objective, hypotheses, accumulated
   evidence, observations, unresolved questions, and constraints.
2. A **planner** selects the next scientific or operational action.
3. A **retrieval layer** provides literature, database records, prior
   experiments, and documentation with provenance.
4. A **tool layer** exposes code execution, data analysis, simulators,
   scientific software, and possibly laboratory instruments.
5. A **verifier** checks evidence support, scientific consistency, feasibility,
   permissions, and output validity before consequential actions are accepted.
6. A **memory and audit record** preserves decisions, tool inputs and outputs,
   software and model versions, and links between claims and evidence.
7. A **feedback controller** incorporates observations, handles failures, and
   determines whether to continue, revise, request human review, or stop.

These are functional roles, not a requirement to use seven separate models.
Some roles may be implemented with deterministic software, domain-specific
models, rules, or human review. Safety constraints and authorization should be
enforced outside the language model when a model-generated action could affect
physical equipment, costly resources, or hazardous materials.

## Evaluation and limits

Scientific agents should be evaluated as decision systems rather than only as
text generators. Relevant questions include:

- Does the agent retrieve the evidence needed for the decision and cite it
  faithfully?
- Are hypotheses distinguishable, falsifiable, and consistent with known
  constraints?
- Does the experiment provide useful information relative to its cost?
- Are generated programs and procedures executable and scientifically valid?
- Does the agent recognize uncertainty, contradictory evidence, and
  out-of-scope conditions?
- Can it detect and recover from retrieval, code, simulation, instrument, and
  experimental failures without corrupting its state?
- Can every result be traced to the data, tools, models, and decisions that
  produced it?
- Does it improve discovery efficiency or scientific validity relative to
  relevant human, workflow, and non-agent baselines?

End-to-end demonstrations do not establish competence at every stage. The
ICLR 2025 **ScienceAgentBench** benchmark therefore evaluates language agents
on individual, data-driven tasks drawn from peer-reviewed scientific work. Its
best evaluated agent solved 32.4% of tasks independently within three attempts,
illustrating the gap between generating plausible research actions and
reliably completing scientific work.

Two chemistry systems illustrate different parts of the architecture.
**Coscientist** connects planning with web and documentation search, code
execution, and laboratory automation. **ChemCrow** lets an LLM iteratively
select among chemistry-specific tools, observe their outputs, and plan further
actions. These systems demonstrate meaningful integration, but they do not
imply that general scientific reasoning or fully autonomous discovery has been
solved.

## Common misinterpretations

- **Many simulations are not automatically agentic.** Adaptation and decision
  authority matter more than repetition.
- **RAG is not discovery by itself.** Retrieved evidence must inform a
  scientifically meaningful decision.
- **A chain-of-thought-style explanation is not validated reasoning.** The
  resulting predictions, experiments, and revisions must be tested.
- **Tool use is not sufficient.** A system must choose and interpret tools
  correctly, preserve state, and recover from failure.
- **Autonomy is not scientific validity.** Controls, uncertainty, provenance,
  replication, and domain review remain necessary.

## References

- Boiko, D. A., MacKnight, R., Kline, B., & Gomes, G. (2023). Autonomous
  chemical research with large language models. *Nature, 624*, 570–578.
  [https://doi.org/10.1038/s41586-023-06792-0](https://doi.org/10.1038/s41586-023-06792-0)
- Bran, A. M., Cox, S., Schilter, O., Baldassari, C., White, A. D., & Schwaller,
  P. (2024). Augmenting large language models with chemistry tools. *Nature
  Machine Intelligence, 6*, 525–535.
  [https://doi.org/10.1038/s42256-024-00832-8](https://doi.org/10.1038/s42256-024-00832-8)
- Chen, Z., et al. (2025). ScienceAgentBench: Toward rigorous assessment of
  language agents for data-driven scientific discovery. *International
  Conference on Learning Representations (ICLR)*.
  [https://proceedings.iclr.cc/paper_files/paper/2025/hash/f12b4df26344f3be803c06b555252efe-Abstract-Conference.html](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f12b4df26344f3be803c06b555252efe-Abstract-Conference.html)

## Related notes

- [AI4Science](index.md)
- [Self-Driving Laboratories](self-driving-laboratories.md)
- [AI Agents](../build/ai-agents.md)
- [Retrieval-Augmented Generation](../build/retrieval-augmented-generation.md)
