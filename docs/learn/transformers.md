# Transformers

A Transformer is a neural-network architecture built around attention and
position-wise transformations. Unlike a recurrent network that must process a
sequence step by step, a Transformer can compute representations for many
positions in parallel during training.

## Self-Attention

For each token representation, learned projections produce a query, key, and
value. Similarity between a query and keys determines attention weights; the
weighted combination of values becomes context-dependent information for that
position. In scaled dot-product attention:

\[
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}(QK^T/\sqrt{d_k})V
\]

Multi-head attention repeats this operation with different learned projections,
allowing different heads to represent different interaction patterns. Residual
connections, normalization, and feed-forward layers complete a Transformer
block.

## Position and Causality

Attention alone does not encode sequence order, so Transformers add positional
information. Autoregressive decoders also use a causal mask: a position may
attend to earlier positions but not future output tokens. During generation,
the model produces one new token at a time, commonly caching earlier key and
value tensors to avoid recomputing the whole prefix.

## Architectural Families

- **Encoder-only** models build representations of an observed sequence.
- **Decoder-only** models generate sequences autoregressively and dominate
  general-purpose LLM deployments.
- **Encoder-decoder** models encode an input and generate a conditioned output.

These categories describe information flow, not a guarantee about capability.
Training data, objectives, scale, alignment, and inference methods also matter.

## Limitations

Standard attention has quadratic time and memory cost in sequence length during
full-sequence computation. Long-context systems use combinations of optimized
kernels, sparse or local attention, recurrence, compression, and retrieval.
Attention weights should not automatically be interpreted as faithful human
explanations of a model's reasoning.

## Further Reading

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)

## Related

- [Large Language Models](large-language-models.md)
- [Context Windows](context-windows.md)
- [Tokenization](tokenization.md)
