# Tokenization

Tokenization converts input into discrete identifiers that a model can process.
Modern language models commonly use subword tokenizers: frequent strings can be
represented by one token, while rarer strings are split into smaller units.
A token may correspond to a word, part of a word, punctuation, whitespace, a
code fragment, or bytes.

## Why Token Boundaries Matter

The tokenizer is part of the model interface. The same text may produce very
different token counts across models, languages, formatting styles, and data
types. Context limits, usage accounting, and much of inference latency are
measured in tokens rather than characters or words.

Token boundaries can also affect behavior. Spelling, arithmetic, identifiers,
and unusual Unicode strings may be awkward when the relevant units are split
across several tokens. A model sees token identifiers and learned positions,
not a human word list.

## Common Approaches

- **Byte-pair encoding (BPE)** repeatedly merges frequent symbol pairs.
- **WordPiece** builds a subword vocabulary using a likelihood-based criterion.
- **Unigram models** choose a probable segmentation from a learned vocabulary.
- **Byte-level methods** ensure arbitrary text can be represented without an
  unknown-character fallback.

The exact implementation belongs to a particular model and should not be
assumed from the model family name alone.

## Engineering Implications

Count tokens with the tokenizer used by the deployed model. Budget separately
for instructions, user data, retrieved passages, tool observations, history,
and the maximum generated response. Test multilingual text, tables, code,
structured data, and long identifiers because their token density may differ
from ordinary English prose.

Truncation should be explicit. Silently cutting the end of a prompt can remove
the question or required schema; cutting the beginning can remove instructions.
Selection, compression, and retrieval are safer than indiscriminate truncation.

## Further Reading

- [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909)
- [SentencePiece](https://arxiv.org/abs/1808.06226)

## Related

- [Large Language Models](large-language-models.md)
- [Context Windows](context-windows.md)
