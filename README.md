# Rightmove Rental Insights – Case Study (CSV + Deltas + Analysis)

This repository showcases what I deliver for clients:
- **Clean, analysis-ready CSV** of rental listings (html stripped, normalized prices)
- **Delta files** between runs: `new.csv`, `changed.csv`, `dropped.csv`
- A **tiny analysis script** that summarizes the data and produces a quick chart

> Note: This is a **case study**. It uses **synthetic/sample data** and does **not** include target-specific scraping code or selectors.

---

## What’s included

- `examples/rightmove_sample.csv` – sample dataset with the exact schema I use in production
- `examples/deltas/` – sample `new.csv`, `changed.csv`, `dropped.csv`
- `scripts/analyse.py` – quick script to compute summary stats and a chart

## CSV schema

Columns (selected):
- **id** – listing id  
- **title, subtitle, description** – cleaned, single-line text  
- **price, price_gbp, price_freq (pcm/pw), price_pcm_est** – normalized price fields  
- **bedrooms, bathrooms, property_type, transaction_type**  
- **available, archived**  
- **address_display, latitude, longitude**  
- **phone, phone_digits, agency_company, agency_branch, agency_address**  
- **tags, features, photos_count, floorplans_count**

All text is HTML-stripped and normalized.

## Quick start

```bash
pip install -r requirements.txt
python scripts/analyse.py --csv examples/rightmove_sample.csv
