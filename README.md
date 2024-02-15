# Twelve Data Scrape #

Forex data scraping by [scrapy](https://docs.scrapy.org/en/latest/index.html).
[Why to used Scrapy](https://proxyway.com/guides/scrapy-vs-beautiful-soup-vs-selenium).

----------------------------------------------

### Spider List ###

#### 1. Forex pair

SPIDER_NAME : forex_pair
Description : Get array of forex pairs available.

| Parameters    | Type   | Default | Description                                       |
| ------------- | ------ | ------- | ------------------------------------------------- |
| currency_base | string | "USD"     | Base currency name according to ISO 4217 standard |

#### 2. Time Series

SPIDER_NAME : time_series
Description : Get metadata and time series of symbol.

| Parameters | Type   | Default   | Description                                                                                              |
| ---------- | ------ | --------- | -------------------------------------------------------------------------------------------------------- |
| interval   | string | "1min"    | Time frame in time series : "1min","5min","15min","30min","45min","1h","2h","4h","1day","1week","1month" |
| outputsize | int    | 5000      | Number of response : 1-5000                                                                              |
| format     | string | "json"    | Data response format : "json" or "csv"                                                                   |
| symbol     | string | "XAU/USD" | Symbol ticker of the instrument                                                                          |

#### 2.1 Time Series By symbols


| Symbol  | Type   | Scrapy Name         |
| ------- | ------ | ------------------- |
| Gold    | Metal  | time_series_xau_usd |
| Silver  | Metal  | time_series_xag_usd |
| EUR/USD | Major  | time_series_eur_usd |
| GBP/USD | Major  | time_series_gbp_usd |
| USD/JPY | Major  | time_series_usd_jpy |
| AUD/JPY | Minor  | time_series_aud_jpy |
| AUD/CAD | Minor  | time_series_aud_cad |
| GBP/CAD | Minor  | time_series_gbp_cad |
| GBP/AUD | Minor  | time_series_gbp_aud |
| BTC/USD | Crypto | time_series_btc_usd |
| ETH/USD | Crypto | time_series_eth_usd |

----------------------------------------------


## Development
With Poetry
### Setup

```shell
poetry update
poetry shell
```

### How to used

```shell
scrapy crawl ${SPIDER_NAME} -a {PAEAMETERS}={VALUE}
```

----------------------------------------------

## Production
With Docker & scrapyd
### Setup

1. Fix .env
2. Create GCS credentials.json to project path
3. Run Docker compose command

```shell
docker compose up -d
```

### How to used

```shell
curl http://localhost:6800/schedule.json -d project=default -d spider=time_series -d {PAEAMETERS}={VALUE}
```

Web client : http://localhost:{PORT}

----------------------------------------------

## License

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2023-present, Kittawee Kongpan
