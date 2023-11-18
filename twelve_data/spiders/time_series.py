import logging
from urllib.parse import urlencode

import scrapy

from twelve_data.items import TimeSeriesItem
from utils.twelve_data import get_headers


class TimeSeriesSpider(scrapy.Spider):
    name = "time_series"
    allowed_domains = ["api.twelvedata.com"]

    # interval : 1min | 5min | 15min | 30min | 45min | 1h | 2h | 4h | 1day | 1week | 1month
    interval_list = [
        "1min",
        "5min",
        "15min",
        "30min",
        "45min",
        "1h",
        "2h",
        "4h",
        "1day",
        "1week",
        "1month",
    ]
    # outputsize : max is 5000
    outputsize = 5000
    # format : csv or json
    format = "json"

    def start_requests(self):
        logging.info("Scraping start.")
        url = "https://api.twelvedata.com/time_series"
        symbol_list = ["XAU/USD", "USD/THB", "THB/USD", "WTI/USD"]
        for symbol in symbol_list:
            for interval in self.interval_list:
                query_string = urlencode(
                    {
                        "symbol": symbol,
                        "interval": interval,
                        "outputsize": self.outputsize,
                        "format": self.format,
                    }
                )
                yield scrapy.Request(
                    url=f"{url}?{query_string}",
                    method="GET",
                    headers=get_headers(),
                    callback=self.parse,
                )
            #     break # Debug
            # break # Debug
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
