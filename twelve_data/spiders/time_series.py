import logging
from urllib.parse import urlencode

import scrapy

from twelve_data.items import TimeSeriesItem
from utils.twelve_data import create_block_oldest_date
from utils.twelve_data import get_dates
from utils.twelve_data import get_headers
from utils.twelve_data import is_block_oldest_date


class TimeSeriesSpider(scrapy.Spider):
    name = "time_series"
    allowed_domains = ["api.twelvedata.com"]
    custom_settings = {
        "FEEDS": {
            "./outputs/%(name)s/%(interval)s/%(time)s.csv": {
                "format": "csv",
                "overwrite": True,
            }
        }
    }
    # Symbol ticker of the instrument
    symbol = "XAU/USD"

    # Format : csv or json
    start_date = None  # Format : YYYY-MM-DD
    end_date = None  # Format : YYYY-MM-DD

    # Interval : 1min | 5min | 15min | 30min | 45min | 1h | 2h | 4h | 1day | 1week | 1month
    interval = "1min"

    # Outputsize : 1 - 5000
    outputsize = 5000

    # Format : csv or json
    format = "json"

    # check is auto scrape
    is_auto = False

    def __init__(
        self,
        symbol: str = "XAU/USD",
        start_date: str | None = None,
        end_date: str | None = None,
        interval: str = "1min",
        outputsize: str = "5000",
        *args,
        **kwargs,
    ):
        super(TimeSeriesSpider, self).__init__(*args, **kwargs)
        self.symbol = symbol
        self.interval = interval
        self.outputsize = int(outputsize)
        self.start_date = start_date
        self.end_date = end_date

    def start_requests(self):
        logging.info("Scraping start.")

        url = "https://api.twelvedata.com/time_series"
        params = {
            "symbol": self.symbol,
            "interval": self.interval,
            "outputsize": self.outputsize,
            "format": self.format,
        }

        # Get Start and End Date
        if self.interval not in ["1month", "1week"]:
            if self.start_date is None and self.end_date is None:
                self.is_auto = True
                self.start_date, self.end_date = get_dates(
                    self.symbol, self.interval, self.outputsize
                )
            params = {
                **params,
                "start_date": self.start_date,
                "end_date": self.end_date,
            }
        # Check Auto is Lastest
        if not self.is_auto or (
            self.is_auto and not is_block_oldest_date(symbol=self.symbol)
        ):

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
        print(data["status"])
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
        elif data["status"] == "error" and self.is_auto:
            create_block_oldest_date(symbol=self.symbol)
