# Fitment Completeness & Coverage

> **Editorial supplement (manual).** This page documents the *current granularity* of the fitment data in the canonical dataset and the forward path to OE-number-level fitment. It complements the auto-generated [vehicle-fitment.md](vehicle-fitment.md) (model ↔ vehicle-type mapping). It is not overwritten by `scripts/build-db-pages.py`.

## What "fitment" means at this stage

Fitment in the hycarfilter dataset is expressed at **two levels of granularity**:

| Level | Where it lives | Example | Status |
|---|---|---|---|
| **Vehicle type** | `products[].applicable_vehicles[]` | `passenger cars`, `heavy trucks`, `agricultural machinery` | ✅ populated for all 22 SKUs |
| **Fitment-critical detail** | `products[].dimensions{thread,gasket}` and `products[].materials{seal,endcap}` | `3/4-16 UNF`, `M16x1.5`, `NBR gasket` | ✅ populated where applicable (oil/fuel filters) |
| **OE part-number level** | `products[].oe_numbers[]` and `products[].cross_reference[]` | `17801-XXXXX` | ⚠️ **seed placeholders** — unverified |

The fitment table therefore tells a buyer *which vehicle class* a SKU serves, but **not yet** *which specific make/model/year* it fits. That second level is the destination for Phase 4+.

## Fitment granularity by category

| Category | Fitment-critical dimension | Current completeness |
|---|---|---|
| Air filter | Panel L×W×H, round H×OD×ID, seal | Dimensions present; vehicle-level fitment |
| Cabin filter | Panel L×W×H, frame & seal | Dimensions present; vehicle-level fitment |
| Oil filter | Thread, gasket, bypass setting | Thread + gasket present; **thread is the OE anchor** |
| Fuel filter | Thread / quick-connect, diesel vs gasoline | Thread + fitting type present; **fitting is the OE anchor** |
| Wiper blade | Length, adapter type | Length present; adapter set documented in editorial |
| Transmission filter | Transmission model (Aisin/ZF/GM), gasket material | Vehicle-level only — **needs transmission-model key** |
| LED lights | Socket (H4/H7), CANbus decoder | Socket present; decoder noted in editorial |

## Why transmission filters need the most work

Transmission filters are the **least complete** fitment dimension in the dataset. They are transmission-specific, not vehicle-generic — a filter matches a specific Aisin / ZF / GM transmission model and its pick-up tube, not a vehicle nameplate. The current `applicable_vehicles` value (`automatic transmission vehicles`) is too coarse to be a real fitment key.

**Forward path:** add a `transmission_model` / `pickup_fit` field to the schema, populate it per SKU, and regenerate the fitment index keyed by transmission model rather than vehicle class.

## The OE-number roadmap

Reaching OE-part-number-level fitment is a data-verification exercise, not a writing exercise. It requires:

1. Confirming each SKU against manufacturer OE catalogues (per SKU, per market).
2. Replacing `XXXXX` / `YYYYY` placeholders with verified OE numbers.
3. Promoting `status` from `seed` → `draft` → `final` as each value is verified.
4. Regenerating [oe-cross-reference.md](oe-cross-reference.md) from the verified dataset.

Until then, the OE and competitor cross-references remain **reference nature only**, and every generated page already flags this. Do not treat a placeholder OE number as a verified fitment claim.

## What is honest to claim today

- **Claim:** the vehicle *class* and *fitment-critical dimensions* (thread, gasket, socket, panel dimensions) each SKU serves.
- **Do not claim:** specific make / model / year coverage, or that any `XXXXX` OE number is a verified match.

This page will be updated as the dataset matures from `seed` toward `final`.
