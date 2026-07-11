# AI Notes

AI Notes is a public, source-linked guide to language models, agents, retrieval,
and evaluation. The site is maintained by Donghyun Lee and published as a
static GitHub Pages site.

Only reviewed public-facing material belongs in this repository. Private notes,
project records, source archives, internal paths, and operational details are
excluded.

## Quality Gates

```bash
python3 scripts/public_scan.py .
mkdocs build --strict
```

Both checks run in GitHub Actions before deployment. A failed safety scan or
strict build blocks publication.

## License

Unless a page states otherwise, the written content is available under the
[Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/).

## Local Preview

```bash
python -m pip install mkdocs-material
mkdocs serve
```
