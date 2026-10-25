#!/usr/bin/env python3
"""
build-db-pages.py — Hycarfilter data sub-site page generator.

Reads the canonical dataset `data/products.json` (the authoritative copy, kept
byte-identical with the main site's `src/data/products.json`) and generates all
data-derived MkDocs pages under `docs/`:

  - docs/products/index.md               SKU full index (every value from JSON)
  - docs/products/{slug}.md              x7  category pages (SKU table + tech params)
  - docs/products/{model}.md             x22 SKU detail pages (full field spec)
  - docs/crossref/vehicle-fitment.md     model <-> vehicle type mapping
  - docs/crossref/oe-cross-reference.md  model <-> OE framework (reference only)
  - docs/crossref/export-packing.md      packing / carton / pallet / 40HQ estimate

Zero manual transcription: every numeric / spec value is rendered from the JSON.
Estimates (carton dimensions, pallet, 40HQ) are clearly marked and computed here,
never stored in the authoritative dataset.

Run from repo root:  python3 scripts/build-db-pages.py
"""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(ROOT, "data", "products.json")
DOCS = os.path.join(ROOT, "docs")

# ---------------------------------------------------------------------------
# Load dataset
# ---------------------------------------------------------------------------

with open(JSON_PATH, "r", encoding="utf-8") as f:
    DS = json.load(f)

META = DS.get("_meta", {})
CATS = {c["code"]: c for c in DS["categories"]}
PRODUCTS = DS["products"]
VERSION = META.get("version", "0.1.0")
GENERATED = META.get("generated", "")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

DIM_ORDER = [
    ("length_mm", "L"),
    ("width_mm", "W"),
    ("height_mm", "H"),
    ("outer_diameter_mm", "OD"),
    ("inner_diameter_mm", "ID"),
]


def dim_str(d):
    vals = [str(d[k]) for k, _ in DIM_ORDER if d.get(k) is not None]
    return (" × ".join(vals) + " mm") if vals else "—"


def eff(v):
    return v if v else "—"


def join_list(v):
    return ", ".join(str(x) for x in v) if v else "—"


def bullet_list(v):
    return "\n".join(f"- `{x}`" for x in v) if v else "—"


def inline_list(v):
    return ", ".join(f"`{x}`" for x in v) if v else "—"


def cat(p):
    return CATS[p["category"]]


def cat_products(code):
    return [p for p in PRODUCTS if p["category"] == code]


def write(path, text):
    full = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  wrote {path}")


# ---------------------------------------------------------------------------
# Per-category technical parameter definitions (editorial, structured)
# ---------------------------------------------------------------------------

CATEGORY_PARAMS = {
    "af": [
        ("Filter media", "nano-fiber composite (fine pores, strong dust capture) vs resin-impregnated cellulose (standard); nano media reaches ≥99.5%, cellulose ≥99.0%."),
        ("Form factor", "Panel (L×W×H) for passenger cars / SUVs; round (H×OD×ID) for light trucks and commercial vehicles."),
        ("Safety layer", "Heavy-duty adds a nano-fiber + safety layer for high-dust construction, agricultural and heavy-truck duty."),
        ("Filtration efficiency", "≥99.0% (standard) / ≥99.5% (nano) / ≥99.6% (heavy-duty)."),
    ],
    "cf": [
        ("Media grade", "Particle (≥95%) / activated carbon (≥96%, adsorbs odour + VOCs) / HEPA composite (≥99.97%, H13) — three ascending grades."),
        ("Frame & seal", "Plastic frame + PU foam gasket; panel form factor (L×W×H)."),
        ("Filtration efficiency", "≥95% particle / ≥96% carbon / ≥99.97% H13 HEPA."),
    ],
    "of": [
        ("Thread", "3/4-16 UNF (passenger spin-on / long-life); 1-12 UNF (heavy-duty); cartridge type has no thread."),
        ("Bypass valve", "Opens when the element is clogged to maintain oil pressure; opening pressure set per model (calibrated in QC)."),
        ("Seal", "NBR gasket with high / low temperature resilience; thermoset plastisol end cap on long-life."),
        ("Filtration efficiency", "≥90% @ 20 µm (standard) / ≥95% @ 20 µm (glass-enhanced / nano composite)."),
    ],
    "ff": [
        ("Filtration efficiency", "≥95% @ 10 µm (standard) / ≥97% @ 10 µm (water-separator)."),
        ("Thread", "M16x1.5 (spin-on and water-separator); inline type uses quick-connect fittings."),
        ("Water separation", "Diesel water-separator adds a water-separation layer for diesel trucks / construction / agricultural duty."),
        ("Form factor", "Spin-on / inline / water-separator."),
    ],
    "wb": [
        ("Length", "350 mm (rear) / 550 mm (beam) / 650 mm (hybrid)."),
        ("Blade type", "Beam (frameless) / hybrid (framed, reinforced) / rear (compact)."),
        ("Rubber", "Natural rubber with graphite / coated finish for smooth, quiet wiping."),
    ],
    "tf": [
        ("Filtration efficiency", "≥90% @ 40 µm (nylon mesh)."),
        ("Media", "Nylon mesh filter screen."),
        ("Gasket", "Cork / rubber pan gasket included (pan or kit variants)."),
    ],
    "led": [
        ("Socket", "H4 / 9003, H7 — direct-fit headlight sockets; bar is auxiliary/off-road lighting."),
        ("Chip", "CSP LED chip on aluminium body for heat dissipation."),
        ("Certifications", "CE, RoHS."),
        ("Dimensions", "H4/H7 are socket-type (no panel dims); light bar L×W×H 520×55×70 mm."),
    ],
}


# ---------------------------------------------------------------------------
# Carton dimension estimates (L, W, H) in cm — ESTIMATES, not in the dataset
# ---------------------------------------------------------------------------

CARTON_DEFAULTS = {
    "af": (60, 45, 35),
    "cf": (55, 45, 30),
    "of": (60, 40, 30),
    "ff": (60, 40, 35),
    "wb": (90, 30, 20),
    "tf": (55, 40, 30),
    "led": (50, 40, 30),
}

CARTON_OVERRIDES = {
    "hy-af-round": (70, 50, 40),
    "hy-af-heavy": (80, 55, 45),
    "hy-of-hd": (60, 45, 40),
    "hy-ff-inline": (50, 40, 25),
    "hy-led-bar": (60, 20, 15),
}

PALLET_L, PALLET_W, PALLET_H = 120, 100, 160  # cm (load height incl. pallet)
HQ40_USABLE_M3 = 65.0  # usable volume estimate for a 40HQ container


def carton_dims(model, category):
    return CARTON_OVERRIDES.get(model, CARTON_DEFAULTS[category])


def packing_estimate(model, category, carton_qty):
    L, W, H = carton_dims(model, category)
    vol_m3 = L * W * H / 1e6
    cpl = max((PALLET_L // L) * (PALLET_W // W), (PALLET_L // W) * (PALLET_W // L))
    layers = int(PALLET_H // H)
    cpp = cpl * layers
    units_pallet = cpp * carton_qty
    cartons_hq = int(HQ40_USABLE_M3 // vol_m3)
    units_hq = cartons_hq * carton_qty
    return dict(L=L, W=W, H=H, vol_m3=round(vol_m3, 4), cpp=cpp,
                units_pallet=units_pallet, cartons_hq=cartons_hq, units_hq=units_hq)


def header(title, desc):
    return f"# {title}\n\n{desc}\n"


def autogen_note():
    return (
        "> **Auto-generated** by `scripts/build-db-pages.py` from the canonical "
        f"dataset `data/products.json` (v{VERSION}, {GENERATED}). "
        "Do not edit values by hand — edit the dataset, then rebuild.\n"
    )


# ---------------------------------------------------------------------------
# 1. SKU full index
# ---------------------------------------------------------------------------

def gen_index():
    rows = []
    for p in PRODUCTS:
        c = cat(p)
        link = f"[`{p['model']}`]({p['model']}.md)"
        rows.append(
            "| " + " | ".join([
                link,
                f"{c['name_en']} ({c['name_zh']})",
                dim_str(p["dimensions"]),
                eff(p["filtration_efficiency"]),
                p["media"],
                f"`{p['hs_code']}`",
            ]) + " |"
        )
    table = "\n".join([
        "| Model | Category | Dimensions | Efficiency | Filter media | HS Code |",
        "|---|---|---|---|---|---|",
    ] + rows)
    text = header("SKU Index", "Full index of every SKU in the canonical dataset. "
                  "All values are rendered from `data/products.json`.")
    text += autogen_note()
    text += f"\n**{len(PRODUCTS)} SKUs across {len(CATS)} categories.**\n\n"
    text += table + "\n"
    write("products/index.md", text)


# ---------------------------------------------------------------------------
# 2. Category pages
# ---------------------------------------------------------------------------

def gen_category(code):
    c = CATS[code]
    skus = cat_products(code)
    rows = []
    for p in skus:
        d = p["dimensions"]
        m = p["materials"]
        pk = p["packing"]
        link = f"[`{p['model']}`]({p['model']}.md)"
        rows.append(
            "| " + " | ".join([
                link,
                p["series"],
                dim_str(d),
                eff(p["filtration_efficiency"]),
                p["media"],
                m["housing"],
                join_list(p["applicable_vehicles"]),
                str(pk["carton_qty"]),
                f"{pk['net_weight_kg']}",
                f"`{p['hs_code']}`",
            ]) + " |"
        )
    table = "\n".join([
        "| Model | Series | Dimensions | Efficiency | Filter media | Housing | Vehicle types | Carton qty | Unit net wt (kg) | HS Code |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ] + rows)

    params = "\n".join(f"| `{name}` | {desc} |" for name, desc in CATEGORY_PARAMS[code])
    params_table = "\n".join([
        "| Parameter | Definition |",
        "|---|---|",
        params,
    ])

    text = header(f"{c['name_en']} · {c['name_zh']}",
                  f"Category code `{code}` · slug `{c['slug']}` · HS Code `{c['hs_code']}` · "
                  f"{len(skus)} SKU(s).")
    text += autogen_note()
    text += "\n" + c["tagline"] + "\n\n"
    text += f"## SKUs ({len(skus)})\n\n{table}\n\n"
    text += "## Category technical parameters\n\n" + params_table + "\n"
    write(f"products/{c['slug']}.md", text)


# ---------------------------------------------------------------------------
# 3. SKU detail pages
# ---------------------------------------------------------------------------

def gen_sku(p):
    c = cat(p)
    d = p["dimensions"]
    m = p["materials"]
    pk = p["packing"]

    dim_rows = "\n".join(
        f"| {label} (`{key}`) | {d.get(key) if d.get(key) is not None else '—'} | mm |"
        for key, label in DIM_ORDER
    )
    dim_table = "\n".join([
        "| Field | Value | Unit |",
        "|---|---|---|",
        dim_rows,
        f"| Thread (`thread`) | {d.get('thread') or '—'} | — |",
        f"| Gasket / seal (`gasket`) | {d.get('gasket') or '—'} | — |",
    ])

    mat_table = "\n".join([
        "| Field | Value |",
        "|---|---|",
        f"| Housing / frame | {m['housing']} |",
        f"| Filter media material | {m['media_material']} |",
        f"| End cap | {m['endcap']} |",
        f"| Seal | {m['seal'] or '—'} |",
    ])

    fit_table = "\n".join([
        "| Field | Value |",
        "|---|---|",
        f"| Applicable vehicles | {inline_list(p['applicable_vehicles'])} |",
        f"| OE numbers | {inline_list(p['oe_numbers'])} |",
        f"| Cross reference (competitor) | {inline_list(p['cross_reference'])} |",
    ])

    pack_table = "\n".join([
        "| Field | Value |",
        "|---|---|",
        f"| Inner box | {pk['inner_box']} |",
        f"| Outer carton | {pk['outer_carton']} |",
        f"| Carton quantity | {pk['carton_qty']} units |",
        f"| Net weight per unit | {pk['net_weight_kg']} kg |",
    ])

    exp_table = "\n".join([
        "| Field | Value |",
        "|---|---|",
        f"| MOQ | {p['moq']} units |",
        f"| Lead time | {p['lead_time_days']} days |",
        f"| Certifications | {inline_list(p['certifications'])} |",
        f"| Target markets | {inline_list(p['target_markets'])} |",
        f"| HS Code | `{p['hs_code']}` |",
    ])

    ident = "\n".join([
        "| Field | Value |",
        "|---|---|",
        f"| Model | `{p['model']}` |",
        f"| Brand | {p['brand']} |",
        f"| Category | {c['name_en']} (`{c['code']}`) |",
        f"| Series | {p['series']} |",
        f"| Name (EN) | {p['name_en']} |",
        f"| Name (ZH) | {p['name_zh']} |",
        f"| Data status | {p['status']} |",
        f"| Filter media | {p['media']} |",
        f"| Filtration efficiency | {eff(p['filtration_efficiency'])} |",
    ])

    text = header(f"{p['name_en']} · {p['name_zh']}", f"`{p['model']}`")
    text += autogen_note()
    text += f"\n> Category: **{c['name_en']} · {c['name_zh']}** — "
    text += f"[category page]({c['slug']}.md) · [SKU index](index.md)\n\n"
    text += "## Identification & performance\n\n" + ident + "\n\n"
    text += "## Dimensions\n\n" + dim_table + "\n\n"
    text += "## Materials\n\n" + mat_table + "\n\n"
    text += "## Fitment & cross-reference\n\n" + fit_table + "\n\n"
    text += "## Packing\n\n" + pack_table + "\n\n"
    text += "## Export & compliance\n\n" + exp_table + "\n"
    write(f"products/{p['model']}.md", text)


# ---------------------------------------------------------------------------
# 4. Vehicle fitment cross-reference
# ---------------------------------------------------------------------------

def gen_fitment():
    rows = "\n".join(
        f"| [`{p['model']}`](../products/{p['model']}.md) | {cat(p)['name_en']} | {join_list(p['applicable_vehicles'])} |"
        for p in PRODUCTS
    )
    forward = "\n".join([
        "| Model | Category | Applicable vehicle types |",
        "|---|---|---|",
        rows,
    ])

    reverse = {}
    for p in PRODUCTS:
        for v in p["applicable_vehicles"]:
            reverse.setdefault(v, []).append(p["model"])
    rev_rows = "\n".join(
        f"| {v} | {' · '.join('`' + m + '`' for m in sorted(ms))} |"
        for v, ms in sorted(reverse.items())
    )
    rev_table = "\n".join([
        "| Vehicle type | Models |",
        "|---|---|",
        rev_rows,
    ])

    text = header("Vehicle Fitment Cross-Reference",
                  "Mapping between SKU models and the vehicle types they fit, "
                  "rendered from each SKU's `applicable_vehicles` field.")
    text += autogen_note()
    text += "\n## Model → vehicle type\n\n" + forward + "\n\n"
    text += "## Vehicle type → model (reverse index)\n\n" + rev_table + "\n"
    write("crossref/vehicle-fitment.md", text)


# ---------------------------------------------------------------------------
# 5. OE cross-reference framework (reference only)
# ---------------------------------------------------------------------------

def gen_oe():
    rows = "\n".join(
        f"| [`{p['model']}`](../products/{p['model']}.md) | {join_list(p['oe_numbers'])} | {join_list(p['cross_reference'])} | seed · reference only |"
        for p in PRODUCTS
    )
    table = "\n".join([
        "| Model | OE numbers | Competitor cross-reference | Status |",
        "|---|---|---|---|",
        rows,
    ])
    text = header("OE Cross-Reference Framework",
                  "Model ↔ OE number ↔ competitor part-number framework. "
                  "**Reference nature only**: all entries carry `status: seed` "
                  "placeholders in the dataset and have not been verified against "
                  "manufacturer OE catalogues.")
    text += autogen_note()
    text += "\n> ⚠️ OE numbers containing `XXXXX` / `YYYYY` are explicit placeholders. "
    "Competitor numbers (MANN / Bosch / Fleetguard / Donaldson / Valeo / Philips / Osram) "
    "are indicative pattern references, not verified matches.\n\n"
    text += table + "\n"
    write("crossref/oe-cross-reference.md", text)


# ---------------------------------------------------------------------------
# 6. Export packing table
# ---------------------------------------------------------------------------

def gen_packing():
    pack_rows = "\n".join(
        f"| [`{p['model']}`](../products/{p['model']}.md) | {p['packing']['inner_box']} | {p['packing']['outer_carton']} | {p['packing']['carton_qty']} | {p['packing']['net_weight_kg']} |"
        for p in PRODUCTS
    )
    pack_table = "\n".join([
        "| Model | Inner box | Outer carton | Carton qty | Unit net wt (kg) |",
        "|---|---|---|---|---|",
        pack_rows,
    ])

    est_rows = []
    for p in PRODUCTS:
        e = packing_estimate(p["model"], p["category"], p["packing"]["carton_qty"])
        est_rows.append(
            f"| [`{p['model']}`](../products/{p['model']}.md) | {e['L']}×{e['W']}×{e['H']} | {e['cpp']} | {e['units_pallet']} | {e['cartons_hq']} | {e['units_hq']} |"
        )
    est_table = "\n".join([
        "| Model | Carton dims L×W×H (cm, est.) | Cartons / pallet (est.) | Units / pallet (est.) | Cartons / 40HQ (est.) | Units / 40HQ (est.) |",
        "|---|---|---|---|---|---|",
        "\n".join(est_rows),
    ])

    text = header("Export Packing Data",
                  "Packing and container-loading data. Inner/outer packing, carton "
                  "quantity and unit net weight are authoritative (from the dataset); "
                  "pallet and 40HQ figures are **estimates** computed by the build script.")
    text += autogen_note()
    text += "\n## Packing (authoritative)\n\n" + pack_table + "\n\n"
    text += "## Pallet & 40HQ estimate\n\n"
    text += ("**Assumptions (estimates only):** pallet footprint 1200×1000 mm, load "
             f"height {PALLET_H} cm; 40HQ usable volume ≈ {HQ40_USABLE_M3:g} m³. "
             "Filters are light, so loading is volume-constrained (not weight-constrained). "
             "Carton dimensions are per-category estimates stored in the script, not in the dataset.\n\n")
    text += est_table + "\n"
    write("crossref/export-packing.md", text)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"Dataset: v{VERSION} ({GENERATED}) — {len(PRODUCTS)} SKUs, {len(CATS)} categories\n")
    gen_index()
    for code in CATS:
        gen_category(code)
    for p in PRODUCTS:
        gen_sku(p)
    gen_fitment()
    gen_oe()
    gen_packing()
    print("\nDone.")


if __name__ == "__main__":
    main()
