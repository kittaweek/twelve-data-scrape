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

```shell
docker compose up -d
```

### How to used

```shell
curl http://localhost:{PORT}/schedule.json -d project=default -d spider={SPIDER_NAME} -d {PAEAMETERS}={VALUE}
```

Web client : http://localhost:{PORT}

----------------------------------------------

## License

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2023-present, Kittawee Kongpan
