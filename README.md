# alnemari-m.github.io

- Feel free to borrow this template.
- Make sure to update all relevant fields in `_config.yml` and `_data`.

# License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.


## Articles (المقالات)

Non-academic articles live in `_articles/`, one markdown file per article, listed at `/articles.html`.

To add a new article, create `_articles/my-article.md` (use a `-ar` suffix for Arabic versions):

```yaml
---
title: "Article Title"          # or Arabic title
lang: en                        # en or ar (ar renders RTL with Arabic font)
date: 2026-08-27
description: "One-line summary shown on the listing card."
translation: /articles/my-article-ar/   # optional: link to the other-language version
---

Markdown body here...
```

Push to `main` and GitHub Pages rebuilds automatically.
