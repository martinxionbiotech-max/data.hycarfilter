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

> 注：Phase 1 架构草案曾使用 `HF-` + 3 位序列（如 `HF-AF-001`），已由 `products.json` 的 `hy-{category_code}-{series}` 规范取代；以本页与数据集为准。

## Category codes

| Code | Category (EN) | Category (ZH) | Slug | HS Code |
|---|---|---|---|---|
| `af` | Air Filter | 空气滤清器 | `air-filter` | 8421310000 |
| `cf` | Cabin Filter | 空调滤清器 | `cabin-filter` | 8421310000 |
| `of` | Oil Filter | 机油滤清器 | `oil-filter` | 8421230000 |
| `ff` | Fuel Filter | 燃油滤清器 | `fuel-filter` | 8421230000 |
| `wb` | Wiper Blade | 雨刮器 | `wiper-blade` | 8512400000 |
| `tf` | Transmission Filter Screen | 变速箱滤网 | `transmission-filter-screen` | 8708409990 |
| `led` | LED Lights | LED 车灯 | `led-lights` | 8512209000 |

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
