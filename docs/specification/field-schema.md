# Field Schema

The canonical dataset `data/products.json` defines one record per SKU. This page documents every field: name, type, unit, and value range / semantics. The machine schema is embedded in the JSON under `_schema`; this page is the human-readable reference.

## Top-level structure

```
{
  "_meta":      { version, generated, brand, naming_rule, status, ... },
  "_schema":    { field definitions },
  "categories": [ 7 category records ],
  "products":   [ 22 SKU records ]
}
```

## Identification

| Field | Type | Unit | Description / range |
|---|---|---|---|
| `model` | string | — | Canonical SKU id, format `hy-{category_code}-{series}` (e.g. `hy-af-nano`). |
| `brand` | string | — | Always `hycarfilter`. |
| `category` | string enum | — | `af` / `cf` / `of` / `ff` / `wb` / `tf` / `led`. |
| `series` | string | — | Human-readable series name (e.g. `Nano`, `Spin-On`, `HEPA`). |
| `name_en` / `name_zh` | string | — | English / Chinese product name. |
| `status` | string enum | — | Data maturity: `seed` \| `draft` \| `final`. |

## Performance

| Field | Type | Unit | Description / range |
|---|---|---|---|
| `media` | string | — | Filter media type: `nano-fiber`, `cellulose`, `composite`, `activated carbon`, `HEPA composite`, `nylon mesh`, `natural rubber (…)`, `LED`. |
| `filtration_efficiency` | string \| null | — | Efficiency string, e.g. `>=99.5%`, `>=90% @ 20um`, `>=99.97% (H13)`; `null` for wiper / LED (not applicable). |

## Dimensions (`dimensions`)

All in millimetres; `null` = not applicable for that form factor.

| Field | Type | Unit | Description / range |
|---|---|---|---|
| `length_mm` | number \| null | mm | Panel / inline / blade / bar length. |
| `width_mm` | number \| null | mm | Panel / bar width. |
| `height_mm` | number \| null | mm | Panel height, or round-filter axial height. |
| `outer_diameter_mm` | number \| null | mm | Round / spin-on outer diameter. |
| `inner_diameter_mm` | number \| null | mm | Round / cartridge inner diameter. |
| `thread` | string \| null | — | Thread spec (oil / fuel): `3/4-16 UNF`, `1-12 UNF`, `M16x1.5`. |
| `gasket` | string \| null | — | Gasket / seal spec, e.g. `NBR`, `pan gasket included`. |

## Materials (`materials`)

| Field | Type | Unit | Description / range |
|---|---|---|---|
| `housing` | string | — | Housing / frame material. |
| `media_material` | string | — | Filter media material. |
| `endcap` | string | — | End cap material. |
| `seal` | string \| null | — | Sealing material; `null` if not applicable. |

## Fitment & cross-reference

| Field | Type | Unit | Description / range |
|---|---|---|---|
| `applicable_vehicles` | string[] | — | Vehicle types the SKU fits (e.g. `passenger cars`, `heavy trucks`). |
| `oe_numbers` | string[] | — | OE cross-reference numbers. **Seed placeholders** (unverified). |
| `cross_reference` | string[] | — | Competitor part numbers (MANN / Bosch / Fleetguard / …). **Indicative, unverified**. |

## Packing (`packing`)

| Field | Type | Unit | Description / range |
|---|---|---|---|
| `inner_box` | string | — | Inner packaging (polybag / color box / sleeve). |
| `outer_carton` | string | — | Outer carton spec (5-ply / double-wall export carton). |
| `carton_qty` | integer | units | Units per carton (装箱量). |
| `net_weight_kg` | number | kg | Net weight per unit. |

## Export & compliance

| Field | Type | Unit | Description / range |
|---|---|---|---|
| `moq` | integer | units | Minimum order quantity. |
| `lead_time_days` | integer | days | Production lead time. |
| `certifications` | string[] | — | Export / quality certs (ISO 9001, IATF 16949, CE, RoHS). |
| `target_markets` | string[] | — | Target export markets. |
| `hs_code` | string | — | China export HS code (10-digit). |

## Category records (`categories`)

| Field | Type | Description |
|---|---|---|
| `code` | string | Category code (matches `products[].category`). |
| `name_en` / `name_zh` | string | Category name. |
| `slug` | string | URL slug for the category page. |
| `hs_code` | string | Default HS code for the category. |
| `tagline` | string | Category definition line (from source inventory). |
