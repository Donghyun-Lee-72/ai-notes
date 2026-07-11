# LLM Evaluation

LLM evaluation measures whether a model-backed system meets requirements on a
defined task distribution. A useful evaluation specifies the users, inputs,
acceptable outputs, failure costs, and operating conditions. A leaderboard
score or generic benchmark is evidence about one setting, not a guarantee for a
particular application.

## Evaluate by Layer

- **Model:** instruction following, reasoning, extraction, generation quality.
- **Context:** evidence selection, ordering, truncation, and contamination.
- **Tools:** selection, argument validity, execution, and recovery.
- **Application:** state transitions, permissions, validation, and stopping.
- **Outcome:** whether the user's actual objective was achieved.

Layered metrics make failures diagnosable. End-to-end task success remains the
final criterion, but it should not be the only recorded signal.

## Building an Evaluation Set

Sample representative production tasks and preserve difficult failures. Cover
common cases, boundary conditions, ambiguous requests, missing information,
adversarial inputs, and costly failure modes. Split data used for prompt or
pipeline development from held-out evaluation data to reduce overfitting.

Expected outputs can be exact values, accepted sets, executable tests, or
rubrics. Record evidence and evaluator instructions. A gold answer should not
encode one preferred writing style when several answers are correct.

## Evaluators

Deterministic checks are best for schemas, calculations, citations, program
tests, and policy rules. Human review is important for nuanced correctness,
usefulness, and high-impact decisions. Model-based judges can scale comparison
but may have position, verbosity, style, and self-preference biases. Calibrate
them against human labels and report disagreement.

## Operational Metrics

Quality must be interpreted with latency, cost, reliability, and safety. Track
error and retry rates, tail latency, token use, tool calls, refusal behavior,
and performance by meaningful slices. Report uncertainty or confidence
intervals when sample size permits.

Regression tests should run whenever the model, prompt, retrieval index, tool
contract, or application logic changes. Online monitoring can detect drift, but
production users should not become an uncontrolled experiment.

## Further Reading

- [HELM](https://arxiv.org/abs/2211.09110)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

## Related

- [Grounding and Hallucination](grounding-and-hallucination.md)
- [RAG Evaluation](rag-evaluation.md)
- [AI Agents](../build/ai-agents.md)
