# Large Language Models

A large language model (LLM) is a neural network trained to estimate
probability distributions over token sequences. Given a context, an
autoregressive LLM repeatedly predicts a distribution for the next token,
selects or samples one, appends it to the context, and continues until a
stopping condition is reached.

This simple interface supports many behaviors because training exposes the
model to recurring structures in language, code, and other serialized data.
The model does not retrieve a stored sentence in the ordinary case; it computes
new token probabilities from learned parameters and the current context.

## From Training to an Application

Pretraining usually optimizes next-token prediction over a large corpus.
Instruction tuning and preference optimization can make the resulting model
more useful in conversations and task-following. At inference time, decoding
settings such as temperature and top-p affect how a token is chosen from the
predicted distribution.

An LLM application includes more than the model:

- a tokenizer and context-management policy;
- instructions, examples, and retrieved evidence;
- tools and permissions;
- parsers and validators;
- state, retries, and stopping conditions;
- evaluation, monitoring, latency, and cost controls.

Changing any of these layers can change system quality even when the model is
unchanged.

## Capabilities and Limits

LLMs are useful for transformation, extraction, classification, explanation,
code generation, and synthesis. Their output is probabilistic rather than a
guaranteed execution trace or database lookup. Fluent text may contain a false
claim, an invalid citation, or an action that violates application constraints.

Important limitations include sensitivity to context, finite context windows,
uneven knowledge, unreliable arithmetic or exact recall, and weak calibration.
The practical response is not only better prompting. Reliable systems combine
generation with retrieval, tools, deterministic checks, typed interfaces, and
task-specific evaluation.

## Design Questions

Before selecting a model, define the required quality, latency, cost, context
size, modalities, data-handling constraints, and tool capabilities. Evaluate
the complete application on representative tasks. A larger model can improve
reasoning while still failing because retrieval, tool execution, or validation
is poorly designed.

## Further Reading

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)

## Related

- [Tokenization](tokenization.md)
- [Transformers](transformers.md)
- [Context Windows](context-windows.md)
- [LLM Evaluation](../evaluate/llm-evaluation.md)
