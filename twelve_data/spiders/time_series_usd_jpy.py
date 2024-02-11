from twelve_data.spiders.time_series import TimeSeriesSpider


class TimeSeriesUsdJpySpider(TimeSeriesSpider):
    name = "time_series_usd_jpy"
    allowed_domains = ["api.twelvedata.com"]

    # Symbol ticker of the instrument
    symbol = "USD/JPY"

    # Format : csv or json
    start_date = None  # Format : YYYY-MM-DD
    end_date = None  # Format : YYYY-MM-DD

    # Interval : 1min | 5min | 15min | 30min | 45min | 1h | 2h | 4h | 1day | 1week | 1month
    interval = "1min"

    # Outputsize : 1 - 5000
    outputsize = 5000

    # Format : csv or json
    format = "json"

    def __init__(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: str = "1min",
        outputsize: str = "5000",
        *args,
        **kwargs,
    ):
        super(TimeSeriesSpider, self).__init__(*args, **kwargs)
        self.interval = interval
        self.outputsize = int(outputsize)
        self.start_date = start_date
        self.end_date = end_date
