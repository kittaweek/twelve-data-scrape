import logging
from urllib.parse import urlencode

import scrapy

from twelve_data.items import ForexPairItem
from utils.twelve_data import get_headers


class ForexPairSpider(scrapy.Spider):
    name = "forex_pair"
    allowed_domains = ["api.twelvedata.com"]
    currency_base = "USD"

    def __init__(
        self,
        currency_base: str = "USD",
        *args,
        **kwargs,
    ):
        super(ForexPairSpider, self).__init__(*args, **kwargs)
        self.currency_base = currency_base

    def start_requests(self):
        logging.info("Scraping start.")
        url = "https://api.twelvedata.com/forex_pairs"
        query_string = urlencode(
            {"currency_base": self.currency_base, "format": "json"}
        )
        logging.info(f"Getting : {self.currency_base}")
        yield scrapy.Request(
            url=f"{url}?{query_string}",
            method="GET",
            headers=get_headers(),
            callback=self.parse,
        )
        logging.info(f"Get {self.currency_base} completed.")

        # break # Debug
        logging.info("Scraping completed.")

    def parse(self, response):
        data = response.json()
        if data["status"] == "ok":
            for i in data["data"]:
                listing = ForexPairItem()
                listing["symbol"] = i["symbol"]
                listing["group"] = i["currency_group"]
                listing["base"] = i["currency_base"]
                listing["quote"] = i["currency_quote"]
                yield listing
