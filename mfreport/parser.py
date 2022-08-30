import re

import pandas as pd
from bs4 import BeautifulSoup


def get_int(td):
    m = re.match(r"[\-0-9]+", td.text.strip().replace(",", ""))
    return int(m[0])


def get_ticker(td):
    s = td.text.strip()

    if s.isdigit():
        return s + ".T"

    return s


class Parser:
    def __init__(self, html):
        self.html = html

    def get_stock(self):
        soup = BeautifulSoup(self.html, "lxml")

        id = "portfolio_det_eq"
        tr_list = soup.find(id=id).find("table").find("tbody").find_all("tr")

        m = {}
        for tr in tr_list:
            d = tr.find_all("td")
            r = [
                get_int(d[2]),
                get_int(d[3]),
                get_int(d[4]),
                get_int(d[5]),
            ]
            ticker = get_ticker(d[0])
            m[ticker] = r

        df = pd.DataFrame.from_dict(
            m,
            orient="index",
            columns=[
                "units",
                "unit_cost",
                "unit_price",
                "sum_price",
            ],
        )

        return df
