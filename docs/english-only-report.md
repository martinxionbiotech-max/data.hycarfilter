# English-Only Conversion Report — Hycarfilter Sub-Sites

> Produced: 2026-10-25 ｜ Author: technical content editor + front-end (Xiaozhu ✍️)
> Scope: `data.hycarfilter` · `tech.hycarfilter` · `market.hycarfilter` (MkDocs)

---

## 1. Summary

All three Hycarfilter sub-sites converted to English-only. Chinese content was removed (bilingual data files) or translated (Chinese prose pages). Verified zero CJK characters in `docs/` and in the rendered site content for all three repos.

## 2. Chinese cleanup — file counts (before → after)

| Repo | Files with Chinese (before) | Files with Chinese (after) |
|---|---|---|
| data.hycarfilter | 34 | 0 |
| tech.hycarfilter | 23 | 0 |
| market.hycarfilter | 21 | 0 |
| **Total** | **78** | **0** |

## 3. MkDocs language changes

| Repo | Before | After |
|---|---|---|
| data.hycarfilter | `en` | `en` (unchanged) |
| tech.hycarfilter | `zh` | `en` |
| market.hycarfilter | `zh` | `en` |

`site_name` was already English and was kept unchanged. `site_description` and all `nav` labels were translated from Chinese to English for tech/market.

## 4. Build-script change (data repo)

`scripts/build-db-pages.py` no longer renders the `name_zh` field:

- SKU index — category column dropped the `(name_zh)` Chinese-name suffix.
- Category pages — title dropped the `· name_zh` Chinese-name suffix.
- SKU detail pages — title dropped the `· name_zh` Chinese-name suffix; the `Name (ZH)` field row was removed (`Name (EN)` → `Name`); the category backlink dropped the Chinese name.

All 30 data-derived pages (SKU index + 7 category + 22 SKU detail) were regenerated from `data/products.json` via `python3 scripts/build-db-pages.py`. The canonical dataset `data/products.json` is unchanged (still byte-identical with the main site; `name_zh` remains in the data source but is no longer rendered).

## 5. Build results

| Repo | mkdocs build |
|---|---|
| data.hycarfilter | ✅ passed |
| tech.hycarfilter | ✅ passed |
| market.hycarfilter | ✅ passed |

Rendered HTML pages and the search index contain zero CJK; page and table structure remain intact.

## 6. Commits

| Repo | Commit | Message |
|---|---|---|
| data.hycarfilter | `9e6217f` | en-only: strip Chinese from data site |
| tech.hycarfilter | `2e0dd8a` | en-only: translate tech site to English |
| market.hycarfilter | `efce368` | en-only: translate market site to English |

All three pushed to `origin/main`.

## 7. Notes

- The MkDocs Material theme bundles third-party search-tokenizer assets (`lunr.zh.min.js`, `lunr.ja.min.js`, `tinyseg.js`) and a favicon under `site/assets/` that contain CJK as infrastructure — these are theme libraries, not authored content, and `site/` is gitignored.
- The editor persona name was romanized to `Xiaozhu` throughout.

## 8. Report path

`docs/english-only-report.md` (this document).
