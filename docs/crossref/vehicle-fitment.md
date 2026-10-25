# Vehicle Fitment Cross-Reference

Mapping between SKU models and the vehicle types they fit, rendered from each SKU's `applicable_vehicles` field.
> **Auto-generated** by `scripts/build-db-pages.py` from the canonical dataset `data/products.json` (v0.1.0, 2026-10-25). Do not edit values by hand — edit the dataset, then rebuild.

## Model → vehicle type

| Model | Category | Applicable vehicle types |
|---|---|---|
| [`hy-af-nano`](../products/hy-af-nano.md) | Air Filter | passenger cars, SUVs |
| [`hy-af-panel`](../products/hy-af-panel.md) | Air Filter | passenger cars |
| [`hy-af-round`](../products/hy-af-round.md) | Air Filter | light trucks, commercial vehicles |
| [`hy-af-heavy`](../products/hy-af-heavy.md) | Air Filter | construction machinery, agricultural machinery, heavy trucks |
| [`hy-cf-particle`](../products/hy-cf-particle.md) | Cabin Filter | passenger cars |
| [`hy-cf-carbon`](../products/hy-cf-carbon.md) | Cabin Filter | passenger cars, SUVs |
| [`hy-cf-hepa`](../products/hy-cf-hepa.md) | Cabin Filter | passenger cars, SUVs, premium vehicles |
| [`hy-of-spinon`](../products/hy-of-spinon.md) | Oil Filter | passenger cars |
| [`hy-of-cartridge`](../products/hy-of-cartridge.md) | Oil Filter | passenger cars (EU/JP models) |
| [`hy-of-hd`](../products/hy-of-hd.md) | Oil Filter | heavy trucks, construction machinery, agricultural machinery |
| [`hy-of-longlife`](../products/hy-of-longlife.md) | Oil Filter | passenger cars (extended oil-change interval) |
| [`hy-ff-spinon`](../products/hy-ff-spinon.md) | Fuel Filter | diesel passenger cars, light commercial vehicles |
| [`hy-ff-inline`](../products/hy-ff-inline.md) | Fuel Filter | gasoline passenger cars |
| [`hy-ff-water`](../products/hy-ff-water.md) | Fuel Filter | diesel trucks, construction machinery, agricultural machinery |
| [`hy-wb-beam`](../products/hy-wb-beam.md) | Wiper Blade | passenger cars |
| [`hy-wb-hybrid`](../products/hy-wb-hybrid.md) | Wiper Blade | passenger cars, SUVs |
| [`hy-wb-rear`](../products/hy-wb-rear.md) | Wiper Blade | SUV rear, hatchback rear |
| [`hy-tf-pan`](../products/hy-tf-pan.md) | Transmission Filter Screen | automatic transmission vehicles |
| [`hy-tf-kit`](../products/hy-tf-kit.md) | Transmission Filter Screen | automatic transmission vehicles (service kit) |
| [`hy-led-h4`](../products/hy-led-h4.md) | LED Lights | passenger cars (H4/9003 socket) |
| [`hy-led-h7`](../products/hy-led-h7.md) | LED Lights | passenger cars (H7 socket) |
| [`hy-led-bar`](../products/hy-led-bar.md) | LED Lights | off-road vehicles, trucks, machinery (auxiliary lighting) |

## Vehicle type → model (reverse index)

| Vehicle type | Models |
|---|---|
| SUV rear | `hy-wb-rear` |
| SUVs | `hy-af-nano` · `hy-cf-carbon` · `hy-cf-hepa` · `hy-wb-hybrid` |
| agricultural machinery | `hy-af-heavy` · `hy-ff-water` · `hy-of-hd` |
| automatic transmission vehicles | `hy-tf-pan` |
| automatic transmission vehicles (service kit) | `hy-tf-kit` |
| commercial vehicles | `hy-af-round` |
| construction machinery | `hy-af-heavy` · `hy-ff-water` · `hy-of-hd` |
| diesel passenger cars | `hy-ff-spinon` |
| diesel trucks | `hy-ff-water` |
| gasoline passenger cars | `hy-ff-inline` |
| hatchback rear | `hy-wb-rear` |
| heavy trucks | `hy-af-heavy` · `hy-of-hd` |
| light commercial vehicles | `hy-ff-spinon` |
| light trucks | `hy-af-round` |
| machinery (auxiliary lighting) | `hy-led-bar` |
| off-road vehicles | `hy-led-bar` |
| passenger cars | `hy-af-nano` · `hy-af-panel` · `hy-cf-carbon` · `hy-cf-hepa` · `hy-cf-particle` · `hy-of-spinon` · `hy-wb-beam` · `hy-wb-hybrid` |
| passenger cars (EU/JP models) | `hy-of-cartridge` |
| passenger cars (H4/9003 socket) | `hy-led-h4` |
| passenger cars (H7 socket) | `hy-led-h7` |
| passenger cars (extended oil-change interval) | `hy-of-longlife` |
| premium vehicles | `hy-cf-hepa` |
| trucks | `hy-led-bar` |
