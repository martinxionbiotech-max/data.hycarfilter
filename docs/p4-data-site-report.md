# Hycarfilter Phase 4 Delivery Report: data.hycarfilter product-database sub-site

> Produced: 2026-10-25 ｜ Author: data-product designer + export-filter industry editor (Xiaozhu ✍️)
> Repo: `data.hycarfilter` (MkDocs · product-database core) ｜ Basis: `docs/hycarfilter-p1-inventory-architecture.md` §2.2 + main-site `src/data/products.json`

---

## 1. Delivery overview

The MkDocs Material data sub-site is live, positioned as "the foundational data layer that is searched, machine-read and cited", with **zero marketing** and zero duplication of the main site's marketing copy. The canonical product dataset has been moved into this repo as the single source of truth.

## 2. MkDocs page count (37 content pages + 1 404)

| Section | Pages | Notes |
|---|---|---|
| Home | 1 | Database positioning / coverage / data notes (no marketing copy) |
| SKU full index | 1 | 22-model master table: model/category/dimensions/efficiency/filter media/HS Code |
| Category pages | 7 | Per-category full SKU spec table + category technical parameter definitions |
| SKU detail pages | 22 | Complete field spec (identification/dimensions/materials/performance/fitment/packing/export) |
| Cross-reference | 3 | Vehicle fitment mapping / OE cross-reference framework / export packing data |
| Data specification | 3 | Field schema / naming rules / changelog |
| **Total** | **37** | |

## 3. Build script notes

`scripts/build-db-pages.py` (Python 3, no third-party dependencies) reads `data/products.json` and generates all data pages in one pass:

- `docs/products/index.md` — SKU full index
- `docs/products/{slug}.md` ×7 — category pages (SKU table + category technical parameter definitions)
- `docs/products/{model}.md` ×22 — SKU detail pages (full field spec)
- `docs/crossref/vehicle-fitment.md` — model ↔ vehicle type (forward + reverse index)
- `docs/crossref/oe-cross-reference.md` — model ↔ OE cross-reference framework (marked reference-only)
- `docs/crossref/export-packing.md` — packing / carton quantity (authoritative) + pallet / 40HQ (script estimates)

**Estimation logic**: pallet 1200×1000 mm / load height 160 cm; 40HQ usable volume ≈ 65 m³; carton dimensions are per-category assumptions inside the script (some models override), and **do not enter the authoritative dataset** — packing / carton quantity / net weight are authoritative values, while pallet / 40HQ figures are estimates and are clearly marked with assumptions on the page.

## 4. Consistency mechanism

1. **Single source of truth**: `data/products.json` is the single source of truth for the main site + the three sub-sites; every value is defined in exactly one place.
2. **Identical authoritative copy**: this repo's `data/products.json` is byte-identical with the main site's `src/data/products.json` (verified by `diff` — **IDENTICAL**, 0 differences).
3. **Zero manual transcription**: all data pages are rendered by the script; no value is transcribed by hand.
4. **Sync flow** (written into README): main site changes data → copy `products.json` into this repo → `python3 scripts/build-db-pages.py` → `mkdocs build` → commit & push (`p4-data-*` marker).

## 5. build / commit / push

- **build**: `mkdocs build` ✅ 37 content pages (+ 404), 1.12s, Material theme.
- **commit**: `449a9ba` `p4-data: scaffold canonical product database (MkDocs Material)`.
- **push**: origin/main (new branch `main` pushed).
- **sync**: main site and data site `products.json` — 0 differences.

## 6. Compact summary

**MkDocs pages**: 37 content pages = home 1 · SKU index 1 · categories 7 · SKU detail pages 22 · cross-reference 3 (vehicle fitment / OE cross-reference / export packing) · data specification 3 (field schema / naming rules / changelog).

**Build script**: `scripts/build-db-pages.py` generates all data pages (index / category / SKU / cross-reference) from `data/products.json` in one pass, with zero manual transcription; pallet / 40HQ figures are script estimates, clearly marked with assumptions, and do not pollute the authoritative data.

**Consistency mechanism**: `data/products.json` is the single source of truth + byte-identical with the main site (diff 0 differences) + script-regenerated pages guarantee identical values across the two repos; README documents the sync flow (change data → copy → rebuild → commit).

**build**: mkdocs build, 37 pages all green. **commit**: `p4-data: scaffold canonical product database`. **push**: origin/main. **sync**: 0/0.

**Report path**: `docs/p4-data-site-report.md` (this document).
