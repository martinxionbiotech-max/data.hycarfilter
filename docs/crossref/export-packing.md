# Export Packing Data

Packing and container-loading data. Inner/outer packing, carton quantity and unit net weight are authoritative (from the dataset); pallet and 40HQ figures are **estimates** computed by the build script.
> **Auto-generated** by `scripts/build-db-pages.py` from the canonical dataset `data/products.json` (v0.1.0, 2026-10-25). Do not edit values by hand — edit the dataset, then rebuild.

## Packing (authoritative)

| Model | Inner box | Outer carton | Carton qty | Unit net wt (kg) |
|---|---|---|---|---|
| [`hy-af-nano`](../products/hy-af-nano.md) | polybag + color box | 5-ply export carton | 20 | 0.42 |
| [`hy-af-panel`](../products/hy-af-panel.md) | polybag + color box | 5-ply export carton | 20 | 0.38 |
| [`hy-af-round`](../products/hy-af-round.md) | polybag + color box | 5-ply export carton | 10 | 1.1 |
| [`hy-af-heavy`](../products/hy-af-heavy.md) | polybag + carton | double-wall export carton | 6 | 2.4 |
| [`hy-cf-particle`](../products/hy-cf-particle.md) | polybag + color box | 5-ply export carton | 25 | 0.22 |
| [`hy-cf-carbon`](../products/hy-cf-carbon.md) | polybag + color box | 5-ply export carton | 25 | 0.26 |
| [`hy-cf-hepa`](../products/hy-cf-hepa.md) | polybag + color box | 5-ply export carton | 25 | 0.3 |
| [`hy-of-spinon`](../products/hy-of-spinon.md) | polybag + color box | 5-ply export carton | 30 | 0.35 |
| [`hy-of-cartridge`](../products/hy-of-cartridge.md) | polybag + color box | 5-ply export carton | 30 | 0.2 |
| [`hy-of-hd`](../products/hy-of-hd.md) | polybag + carton | double-wall export carton | 12 | 1.3 |
| [`hy-of-longlife`](../products/hy-of-longlife.md) | polybag + color box | 5-ply export carton | 30 | 0.38 |
| [`hy-ff-spinon`](../products/hy-ff-spinon.md) | polybag + color box | 5-ply export carton | 20 | 0.5 |
| [`hy-ff-inline`](../products/hy-ff-inline.md) | polybag + color box | 5-ply export carton | 50 | 0.12 |
| [`hy-ff-water`](../products/hy-ff-water.md) | polybag + carton | double-wall export carton | 12 | 0.9 |
| [`hy-wb-beam`](../products/hy-wb-beam.md) | polybag + sleeve | 5-ply export carton | 50 | 0.18 |
| [`hy-wb-hybrid`](../products/hy-wb-hybrid.md) | polybag + sleeve | 5-ply export carton | 50 | 0.22 |
| [`hy-wb-rear`](../products/hy-wb-rear.md) | polybag + sleeve | 5-ply export carton | 50 | 0.12 |
| [`hy-tf-pan`](../products/hy-tf-pan.md) | polybag + color box | 5-ply export carton | 20 | 0.3 |
| [`hy-tf-kit`](../products/hy-tf-kit.md) | polybag + color box | 5-ply export carton | 20 | 0.35 |
| [`hy-led-h4`](../products/hy-led-h4.md) | polybag + color box | 5-ply export carton | 20 | 0.25 |
| [`hy-led-h7`](../products/hy-led-h7.md) | polybag + color box | 5-ply export carton | 20 | 0.25 |
| [`hy-led-bar`](../products/hy-led-bar.md) | polybag + color box | 5-ply export carton | 10 | 2.8 |

## Pallet & 40HQ estimate

**Assumptions (estimates only):** pallet footprint 1200×1000 mm, load height 160 cm; 40HQ usable volume ≈ 65 m³. Filters are light, so loading is volume-constrained (not weight-constrained). Carton dimensions are per-category estimates stored in the script, not in the dataset.

| Model | Carton dims L×W×H (cm, est.) | Cartons / pallet (est.) | Units / pallet (est.) | Cartons / 40HQ (est.) | Units / 40HQ (est.) |
|---|---|---|---|---|---|
| [`hy-af-nano`](../products/hy-af-nano.md) | 60×45×35 | 16 | 320 | 687 | 13740 |
| [`hy-af-panel`](../products/hy-af-panel.md) | 60×45×35 | 16 | 320 | 687 | 13740 |
| [`hy-af-round`](../products/hy-af-round.md) | 70×50×40 | 8 | 80 | 464 | 4640 |
| [`hy-af-heavy`](../products/hy-af-heavy.md) | 80×55×45 | 6 | 36 | 328 | 1968 |
| [`hy-cf-particle`](../products/hy-cf-particle.md) | 55×45×30 | 20 | 500 | 875 | 21875 |
| [`hy-cf-carbon`](../products/hy-cf-carbon.md) | 55×45×30 | 20 | 500 | 875 | 21875 |
| [`hy-cf-hepa`](../products/hy-cf-hepa.md) | 55×45×30 | 20 | 500 | 875 | 21875 |
| [`hy-of-spinon`](../products/hy-of-spinon.md) | 60×40×30 | 20 | 600 | 902 | 27060 |
| [`hy-of-cartridge`](../products/hy-of-cartridge.md) | 60×40×30 | 20 | 600 | 902 | 27060 |
| [`hy-of-hd`](../products/hy-of-hd.md) | 60×45×40 | 16 | 192 | 601 | 7212 |
| [`hy-of-longlife`](../products/hy-of-longlife.md) | 60×40×30 | 20 | 600 | 902 | 27060 |
| [`hy-ff-spinon`](../products/hy-ff-spinon.md) | 60×40×35 | 16 | 320 | 773 | 15460 |
| [`hy-ff-inline`](../products/hy-ff-inline.md) | 50×40×25 | 36 | 1800 | 1299 | 64950 |
| [`hy-ff-water`](../products/hy-ff-water.md) | 60×40×35 | 16 | 192 | 773 | 9276 |
| [`hy-wb-beam`](../products/hy-wb-beam.md) | 90×30×20 | 32 | 1600 | 1203 | 60150 |
| [`hy-wb-hybrid`](../products/hy-wb-hybrid.md) | 90×30×20 | 32 | 1600 | 1203 | 60150 |
| [`hy-wb-rear`](../products/hy-wb-rear.md) | 90×30×20 | 32 | 1600 | 1203 | 60150 |
| [`hy-tf-pan`](../products/hy-tf-pan.md) | 55×40×30 | 20 | 400 | 984 | 19680 |
| [`hy-tf-kit`](../products/hy-tf-kit.md) | 55×40×30 | 20 | 400 | 984 | 19680 |
| [`hy-led-h4`](../products/hy-led-h4.md) | 50×40×30 | 30 | 600 | 1083 | 21660 |
| [`hy-led-h7`](../products/hy-led-h7.md) | 50×40×30 | 30 | 600 | 1083 | 21660 |
| [`hy-led-bar`](../products/hy-led-bar.md) | 60×20×15 | 100 | 1000 | 3611 | 36110 |
