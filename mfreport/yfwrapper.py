from datetime import datetime
import yfinance as yf
import pandas as pd
from collections import defaultdict


class Yfwrapper:
    def __init__(self, symbols):
        self.symbols = symbols

    def get_info(self):
        usdjpy = yf.Ticker("JPY=X").info["bid"]
        last_year = str(datetime.now().year - 1)
        m = defaultdict(lambda: [])

        for symbol in self.symbols:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            divs = ticker.dividends.filter(regex="^" + last_year)
            toJpy = usdjpy if info["currency"] == "USD" else 1.0

            m[symbol].append(info["shortName"])
            m[symbol].append(divs.sum() * toJpy)

            divs_per_month = [0.0] * 12
            for k, v in divs.items():
                i = k.month - 1
                divs_per_month[i] = float(v) * toJpy

            m[symbol].extend(divs_per_month)

        columns = ["shortName", "divTotal"] + [
            datetime(1111, i + 1, 11).strftime("div%b") for i in range(12)
        ]

        df = pd.DataFrame.from_dict(
            m,
            orient="index",
            columns=columns,
        )

        return df
