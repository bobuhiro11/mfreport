import os
from collections import defaultdict
from datetime import datetime

import pandas as pd
import yfinance as yf


def getShortName(info):
    s = info["shortName"]
    keywords = [
        ", Inc.",
        " CO LTD",
        " Inc.",
        ", Series 1",
        " CORPORATION",
        " CORP.",
        " CORP",
        " INC",
        " FUND",
        " HOLDINGS",
        " HLDS",
        " Limited",
        " (The)",
        " CO",
        " S&",
        " CHAIN",
        " Corporation",
    ]

    for k in keywords:
        s = s.replace(k, "")

    return s


class Yfwrapper:
    def __init__(self, units):
        self.units = units

    def get_info(self):
        if os.path.exists("yf.pkl"):
            return pd.read_pickle("yf.pkl")

        symbols = self.units.keys().tolist()
        usdjpy = yf.Ticker("JPY=X").info["bid"]
        last_year = str(datetime.now().year - 1)
        m = defaultdict(lambda: [])

        for symbol in symbols:
            units = self.units[symbol]
            ticker = yf.Ticker(symbol)
            info = ticker.info
            divs = ticker.dividends.filter(regex="^" + last_year)
            toJpy = usdjpy if info["currency"] == "USD" else 1.0

            m[symbol].append(getShortName(info))
            m[symbol].append(divs.sum() * toJpy * units)

            divs_per_month = [0.0] * 12
            for k, v in divs.items():
                i = k.month - 1
                divs_per_month[i] = float(v) * toJpy * units

            m[symbol].extend(divs_per_month)

        columns = ["shortName", "divTotal"] + [
            datetime(1111, i + 1, 11).strftime("div%b") for i in range(12)
        ]

        df = pd.DataFrame.from_dict(
            m,
            orient="index",
            columns=columns,
        )

        df.to_pickle("yf.pkl")

        return df
