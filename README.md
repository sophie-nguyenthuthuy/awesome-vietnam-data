# Awesome Vietnam Data 🇻🇳 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open datasets, APIs, and data tools for Vietnam — for data engineers, analysts, researchers, and builders.

*Curated by [@sophie-nguyenthuthuy](https://github.com/sophie-nguyenthuthuy). PRs welcome — see [Contributing](#contributing).*

*🇻🇳 Tiếng Việt: [README.vi.md](README.vi.md) · Starter datasets (provinces 2025, GDP & population 1960–2024, airports, Tết, holidays): [`data/`](data/)*

## Contents

- [Official & Government](#official--government)
- [Economy & Finance](#economy--finance)
- [Geospatial](#geospatial)
- [Vietnamese NLP](#vietnamese-nlp)
- [Environment & Weather](#environment--weather)
- [Demographics & Development](#demographics--development)
- [Tools & Libraries](#tools--libraries)
- [Working with Vietnamese data: gotchas](#working-with-vietnamese-data-gotchas)

## Official & Government

- [General Statistics Office (GSO)](https://www.gso.gov.vn) — official statistics: CPI, GDP, population, trade, industry. Monthly/quarterly/annual releases; many tables downloadable.
- [Vietnam Open Data Portal](https://data.gov.vn) — the national open data portal; ministries and provinces publish datasets here.
- [State Bank of Vietnam (SBV)](https://www.sbv.gov.vn) — exchange rates, interest rates, monetary statistics, credit institution data.
- [National Business Registration Portal](https://dangkykinhdoanh.gov.vn) — business registration lookups.
- [Vietnam Customs](https://www.customs.gov.vn) — import/export statistics by commodity and partner country.

## Economy & Finance

- [World Bank — Vietnam](https://data.worldbank.org/country/vietnam) — hundreds of macro indicators, clean API, long time series.
- [IMF Data — Vietnam](https://data.imf.org) — balance of payments, government finance, IFS series.
- [Asian Development Bank — Key Indicators](https://www.adb.org/what-we-do/data/statistics) — comparable ASEAN-wide indicators.
- [Ho Chi Minh Stock Exchange (HOSE)](https://www.hsx.vn) — listings, indices, disclosure filings.
- [Hanoi Stock Exchange (HNX)](https://www.hnx.vn) — HNX/UPCoM listings and market data.
- [vnstock (Python)](https://github.com/thinh-vu/vnstock) — Python library for Vietnamese stock market data.

## Geospatial

- [OpenStreetMap Vietnam extracts (Geofabrik)](https://download.geofabrik.de/asia/vietnam.html) — full OSM extract, refreshed daily; the workhorse for VN geodata.
- [GADM — Vietnam administrative boundaries](https://gadm.org) — province/district/commune boundary polygons.
- [HDX — Vietnam](https://data.humdata.org/group/vnm) — humanitarian datasets: admin boundaries, population grids, infrastructure.
- [WorldPop — Vietnam](https://www.worldpop.org) — gridded population estimates (100m resolution).

## Vietnamese NLP

- [PhoBERT](https://github.com/VinAIResearch/PhoBERT) — pre-trained BERT for Vietnamese (VinAI); the standard baseline.
- [underthesea](https://github.com/undertheseanlp/underthesea) — Vietnamese NLP toolkit: tokenization, POS, NER, sentiment.
- [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP) — word segmentation, POS, NER, dependency parsing.
- [VLSP shared tasks](https://vlsp.org.vn) — Vietnamese Language and Speech Processing community datasets and benchmarks.
- [Hugging Face — Vietnamese datasets](https://huggingface.co/datasets?language=language:vi) — filterable index of vi-language corpora and benchmarks.

## Environment & Weather

- [IQAir — Vietnam air quality](https://www.iqair.com/vietnam) — real-time AQI for VN cities (API available).
- [OpenAQ](https://openaq.org) — open air-quality measurements incl. Vietnamese stations, with API.
- [NCHMF](https://nchmf.gov.vn) — National Centre for Hydro-Meteorological Forecasting: weather, hydrology, storm warnings.
- [Open-Meteo](https://open-meteo.com) — free weather API with VN coverage, no key required; good for pipelines and teaching.

## Demographics & Development

- [UN Data — Viet Nam](https://data.un.org) — UN statistical system indicators.
- [DHS Program — Vietnam surveys](https://dhsprogram.com) — health and demographic microdata (registration required).
- [UNICEF MICS](https://mics.unicef.org) — multiple indicator cluster surveys incl. Vietnam.
- [Our World in Data](https://ourworldindata.org) — charts + downloadable VN series for health, energy, education.

## Tools & Libraries

- [vnstock](https://github.com/thinh-vu/vnstock) — stock market data (also listed above).
- [underthesea](https://github.com/undertheseanlp/underthesea) / [pyvi](https://github.com/trungtv/pyvi) — text processing for Vietnamese.
- [inflation-crawler](https://github.com/sophie-nguyenthuthuy/data-engineering/tree/main/inflation-crawler) — VN CPI/inflation crawler → DuckDB → FastAPI (part of my DE monorepo).
- [savings-rate-engine](https://github.com/sophie-nguyenthuthuy/data-engineering/tree/main/savings-rate-engine) — scrapes & normalizes VN bank savings rates.

## Working with Vietnamese data: gotchas

A few hard-won notes for data engineers:

- **Encoding**: legacy files may use TCVN3 or VNI instead of UTF-8; always detect before parsing. Unicode normalization matters — the same word can be NFC or NFD encoded (`ế` as one codepoint vs. `e` + two combining marks). Normalize to NFC at ingestion.
- **Names & addresses**: family-name-first ordering; province/district/ward hierarchy changes over time (administrative mergers are frequent — keep a date-versioned admin-unit dimension table).
- **Numbers**: VND amounts are large — use 64-bit ints, never float; thousands separators are `.` and decimal commas `,` in many sources.
- **Dates**: `dd/mm/yyyy` dominates; lunar-calendar holidays (Tết) shift yearly and matter for any time-series seasonality work.

## Contributing

Found a great source, or a dead link? Open a PR — one line per entry, format `[Name](url) — short description (what's in it, access method)`. Sources must be legally accessible; no scraped dumps of ToS-protected sites.

## License

[CC0](https://creativecommons.org/publicdomain/zero/1.0/) — public domain dedication.
# awesome-vietnam-data
🇻🇳 Curated open datasets, APIs &amp; tools for Vietnam — for data engineers and researchers
