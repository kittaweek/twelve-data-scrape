import logging
from urllib.parse import urlencode

import scrapy

from twelve_data.items import TimeSeriesItem
from utils.twelve_data import get_dates
from utils.twelve_data import get_headers


class TimeSeriesManualSpider(scrapy.Spider):
    name = "time_series_manual"
    allowed_domains = ["api.twelvedata.com"]
    custom_settings = {
        "FEEDS": {
            "output/%(name)s/%(interval)s/%(time)s.csv": {
                "format": "csv",
                "overwrite": True,
            }
        }
    }

    # interval : 1min | 5min | 15min | 30min | 45min | 1h | 2h | 4h | 1day | 1week | 1month
    interval = "1min"
    # outputsize : max is 5000
    outputsize = 5000
    # format : csv or json
    format = "json"
    symbol = "XAU/USD"

    def __init__(
        self, symbol: str = "XAU/USD", interval: str = "1min", outputsize: str = "5000"
    ):
        self.symbol = symbol
        self.interval = interval
        self.outputsize = int(outputsize)

    def start_requests(self):
        logging.info("Scraping start.")
        url = "https://api.twelvedata.com/time_series"
        params = {
            "symbol": self.symbol,
            "interval": self.interval,
            "outputsize": self.outputsize,
            "format": self.format,
        }
        if self.interval not in ["1month", "1week"]:
            start_date, end_date = get_dates(self.interval, self.outputsize)
            params = {
                **params,
                "start_date": start_date,
                "end_date": end_date,
            }

        query_string = urlencode(
            {
                "timezone": "UTC",
                **params,
            }
        )
        yield scrapy.Request(
            url=f"{url}?{query_string}",
            method="GET",
            headers=get_headers(),
            callback=self.parse,
        )

        logging.info("Scraping completed.")

    def parse(self, response):
        data = response.json()
        if data["status"] == "ok":
            for i in data["values"]:
                listing = TimeSeriesItem()
                listing["symbol"] = data["meta"]["symbol"]
                listing["datetime"] = i["datetime"]
                listing["open"] = i["open"]
                listing["high"] = i["high"]
                listing["low"] = i["low"]
                listing["close"] = i["close"]
                yield listing
