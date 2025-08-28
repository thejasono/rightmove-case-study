# Rightmove Rental Insights — Case Study (CSV + Deltas + Weekly Feed)

**Case study shows** how a rental data feed can be delivered as a clean CSV with **change tracking (deltas)** and a lightweight **analysis snapshot** suitable for Excel/BI tools and quick decision-making.

> This is a **sanitised case study**: it includes sample CSVs and analysis only.
> Target-specific scraping code/selectors are not included.

---

## Walkthrough (what happens end-to-end)

1. Collect listings for chosen areas/filters.
2. Clean and normalise fields (HTML-free text, price in `pcm`, agent & location fields).
3. Write a **single CSV** that’s ready for Excel/Sheets/BI.
4. Compare against the previous snapshot → produce **deltas**:

   * `new.csv` (arrivals)
   * `changed.csv` (e.g., price moves)
   * `dropped.csv` (no longer present)
5. (Optional) Generate a **1-page chart** for fast stakeholder review.

---

## What’s included in this repo

* `examples/rightmove.csv` — sample dataset using the production schema
* `examples/deltas/` — sample `new.csv`, `changed.csv`, `dropped.csv`
* `scripts/analyse.py` — tiny analysis script (prints summary + saves a chart)

**Quick start**

```bash
pip install -r requirements.txt
python -m scripts.analyse --csv examples/rightmove.csv
# -> prints median monthly price by bedrooms
# -> writes examples/summary.png
```

---

## CSV schema (selected columns)

* **Core:** `id`, `title`, `subtitle`, `description` (single-line, HTML stripped)
* **Price:** `price` (raw), `price_gbp`, `price_freq` (`pcm`/`pw`), `price_pcm_est` (monthly)
* **Beds/Baths:** `bedrooms`, `bathrooms`
* **Type/Status:** `property_type`, `transaction_type`, `available`, `archived`
* **Location:** `address_display`, `latitude`, `longitude`
* **Agent:** `phone`, `phone_digits`, `agency_company`, `agency_branch`, `agency_address`
* **Extras:** `tags`, `features`, `photos_count`, `floorplans_count`

All text is normalised and de-HTML’d for easy filtering, pivoting, and charting.

---

## Use cases (how teams employ this)

* **Market snapshot** for a borough/segment: CSV for analysis + deltas to track week-over-week changes.
* **Lead triage**: surface **new** or **price-dropped** listings that match criteria.
* **Competitor tracking**: monitor agents, pricing bands, and time-on-market proxies.
* **Ops dashboards**: push to Google Sheets/BI and refresh on a schedule.

---

## What’s included in a typical engagement

* Clean CSV with normalised prices (`price_pcm_est`) and agent/location fields
* Deltas: `new.csv`, `changed.csv`, `dropped.csv` after each refresh
* A small visual summary (PNG) for quick internal sharing
* Respectful, concurrency-limited collection with retry/backoff and skip logs

---

## Other things I can offer alongside this

* **Google Sheets sync** (for non-technical stakeholders)
* **Slack/Email alerts** (e.g., price drops, new within criteria)
* **CRM/Airtable/HubSpot push** (pipe deltas straight into your workflow)
* **Custom charts/decks** (beds mix, price bands, postcode summaries)
* **Geospatial add-ons** (postcode enrichment, simple heatmaps)

---

## Tech used in this repo (analysis layer)

* Python, pandas, matplotlib

> The case study focuses on artefacts and analysis. Target-specific collection logic remains private by design.

---

If you want a private demo aligned to your areas and filters, reach out and a short walkthrough can be shared.
