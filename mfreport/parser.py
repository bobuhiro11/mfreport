import re
from collections import defaultdict

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

        m = defaultdict(lambda: [0] * 3)
        for tr in tr_list:
            d = tr.find_all("td")

            ticker = get_ticker(d[0])

            units = get_int(d[2])
            price = get_int(d[5])
            profit = get_int(d[7])

            m[ticker][0] += units
            m[ticker][1] += price
            m[ticker][2] += profit

        df = pd.DataFrame.from_dict(
            m,
            orient="index",
            columns=[
                "units",
                "price",
                "profit",
            ],
        )

        return df
