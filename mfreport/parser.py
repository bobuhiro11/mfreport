from bs4 import BeautifulSoup
import re
import pandas as pd


def get_float(td):
    m = re.match(r"[0-9\.]+", td.text.replace(",", ""))
    return float(m[0])


def get_int(td):
    m = re.match(r"[0-9]+", td.text.replace(",", ""))
    return int(m[0])


def get_str(td):
    return td.text


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
                get_int(d[0]),
                get_str(d[1]),
                get_int(d[2]),
                get_int(d[3]),
                get_int(d[4]),
                get_int(d[5]),
                get_int(d[6]),
                get_int(d[7]),
                get_float(d[8]),
            ]
            m[r[0]] = r

        df = pd.DataFrame.from_dict(
            m,
            orient="index",
            columns=[
                "ticker",
                "name",
                "n",
                "avg_unit_price",
                "cur_unit_price",
                "cur_sum_price",
                "foo",
                "bar",
                "baz",
            ],
        )

        return df
