# Hycarfilter Data

**Canonical product database** for hycarfilter — Qinghe County Hongying Auto Parts Co., Ltd. (清河县宏盈汽车零部件有限公司; since 2013, Qinghe County, Xingtai, Hebei).

> **Positioning**: the foundational data layer that is searched, machine-read and cited. This sub-site carries only **structured data / specifications / cross-references**, with zero marketing. Marketing copy and purchasing-decision content live on the main site `hycarfilter.com`; this sub-site is only cited by it and does not duplicate it.

> **Commercial catalog &amp; inquiry** — [View all products &amp; request a quote on hycarfilter.com →](https://hycarfilter.com/products/)

## Coverage

| Dimension | Value |
|---|---|
| Categories | **7** (air filter / cabin filter / oil filter / fuel filter / wiper blade / transmission filter screen / LED lights) |
| SKUs | **22** (seed dataset, 2–4 representative models per category) |
| Data version | `0.1.0` (`data/products.json` `_meta.version`) |
| Naming rule | `hy-{category_code}-{series}` (e.g. `hy-af-nano`) |
| Field coverage | Identification / dimensions / materials / performance / fitment / OE cross-reference / packing / export (MOQ · lead time · certifications · target markets · HS Code) |

## Data notes

1. **Single source of truth (canonical)**: the single source of truth for every model / parameter / specification lives in this repo's `data/products.json`. The main site and the tech/market sub-sites reference the same file, so **each value is defined in exactly one place** across sites.
2. **Zero manual transcription**: every data page in this sub-site (SKU index, category pages, SKU detail pages, cross-reference tables) is rendered by `scripts/build-db-pages.py` from the JSON — no value is transcribed by hand.
3. **Reference-only marking**: OE cross-reference numbers and competitor part numbers are currently `status: seed` placeholder / indicative values, **not verified**; the cross-reference page clearly marks this reference-only nature.
4. **Estimate marking**: pallet / 40HQ loading quantities are script **estimates**, and carton dimensions are per-category assumptions inside the script — they **do not enter the authoritative dataset**; packing / carton quantity / net weight are authoritative values.
5. **Data maturity**: the `status` field marks `seed | draft | final`; currently all values are `seed`, to be progressively completed and verified through Phase 4+.

## Quick links

- [SKU full index](products/index.md) — 22-model master table (model / category / dimensions / efficiency / filter media / HS Code)
- [Category pages](products/air-filter.md) — 7 category spec tables + category technical parameter definitions
- [Vehicle fitment mapping](crossref/vehicle-fitment.md) — model ↔ applicable vehicle types (forward / reverse index)
- [OE cross-reference framework](crossref/oe-cross-reference.md) — model ↔ OE number (reference-only)
- [Export packing data](crossref/export-packing.md) — packing / carton quantity / pallet / 40HQ estimates
- [Field schema](specification/field-schema.md) · [Naming rules](specification/naming-rules.md) · [Changelog](specification/changelog.md)
