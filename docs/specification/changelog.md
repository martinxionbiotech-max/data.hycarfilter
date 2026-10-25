# Changelog

Version and update log for the canonical dataset and this sub-site.

## Versioning

- Dataset version is the single source of truth: `data/products.json` `_meta.version`.
- Format: `major.minor.patch` (semver). Bump `patch` for value corrections, `minor` for added SKUs/fields, `major` for schema-breaking changes.

## Log

### 0.1.0 — 2026-10-25

- **Initial seed dataset**: 7 categories, 22 SKUs.
- Schema established (identification / dimensions / materials / performance / fitment / packing / export).
- Naming rule `hy-{category_code}-{series}`.
- All product data carries `status: seed` — schema + placeholder values; OE / competitor cross-references are **unverified reference placeholders**.
- Sub-site scaffolded: MkDocs Material + `scripts/build-db-pages.py` generator + cross-reference pages.

### Next

- Replace seed OE numbers / competitor part numbers with verified catalogue data (Phase 4+).
- Add `draft` → `final` status promotion as values are confirmed.
- Per-SKU carton dimensions promoted from script estimates to dataset fields once measured.
