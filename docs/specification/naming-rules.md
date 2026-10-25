# Naming Rules

## Canonical model naming

Every SKU id follows a single rule defined in `data/products.json` `_meta.naming_rule`:

```
hy-{category_code}-{series}
```

- `hy` — brand prefix (hycarfilter).
- `{category_code}` — two-letter category code (see table below).
- `{series}` — lowercase series / form-factor token (kebab-style).

Examples: `hy-af-nano`, `hy-of-spinon`, `hy-cf-hepa`, `hy-led-h4`, `hy-ff-water`.

> Note: The Phase 1 architecture draft used a `HF-` + 3-digit sequence (e.g. `HF-AF-001`), which has been superseded by the `hy-{category_code}-{series}` convention in `products.json`; this page and the dataset are authoritative.

## Category codes

| Code | Category (EN) | Slug | HS Code |
|---|---|---|---|
| `af` | Air Filter | `air-filter` | 8421310000 |
| `cf` | Cabin Filter | `cabin-filter` | 8421310000 |
| `of` | Oil Filter | `oil-filter` | 8421230000 |
| `ff` | Fuel Filter | `fuel-filter` | 8421230000 |
| `wb` | Wiper Blade | `wiper-blade` | 8512400000 |
| `tf` | Transmission Filter Screen | `transmission-filter-screen` | 8708409990 |
| `led` | LED Lights | `led-lights` | 8512209000 |

## Series tokens (current)

| Category | Series tokens |
|---|---|
| `af` | `nano`, `panel`, `round`, `heavy` |
| `cf` | `particle`, `carbon`, `hepa` |
| `of` | `spinon`, `cartridge`, `hd`, `longlife` |
| `ff` | `spinon`, `inline`, `water` |
| `wb` | `beam`, `hybrid`, `rear` |
| `tf` | `pan`, `kit` |
| `led` | `h4`, `h7`, `bar` |

## URL / file conventions

- Category page: `docs/products/{slug}.md` → `/products/{slug}/`.
- SKU detail page: `docs/products/{model}.md` → `/products/{model}/`.
- Cross-reference: `docs/crossref/*.md`.
- Data specification: `docs/specification/*.md`.
