import argparse
import shutil

import pandas as pd

from mfreport.client import Client
from mfreport.logger import logger
from mfreport.parser import Parser
from mfreport.yfwrapper import Yfwrapper


def get_params():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="username")
    parser.add_argument("-p", "--password", help="password")
    parser.add_argument("-o", "--otp", help="one time password")
    return parser.parse_args()


def msg():
    return "Hello, world!"


def hline():
    width = shutil.get_terminal_size().columns
    print("\u2500" * width)


def main():
    pd.options.display.precision = 0

    logger.info("mfreport started.")
    p = get_params()

    logger.info("Downloading from moneyforward.com started. Please wait.")
    html = Client(p.user, p.password, p.otp).get_html()
    df1 = Parser(html).get_stock()
    logger.info("Done.")

    logger.info("Downloading from yfinance started. Please wait.")
    df2 = Yfwrapper(df1["units"]).get_info()
    logger.info("Done.")

    df = pd.merge(df1, df2, left_index=True, right_index=True)
    df3 = df.filter(regex="^div", axis=1).drop(["divTotal"], axis=1).sum()
    gain = df["profit"].sum()
    annual_div = int(df["divTotal"].sum())

    hline()
    print(df)

    hline()
    print("Total unrealized capital gain is {:,d} yen.".format(gain))
    print("Total annual dividend is {:,d} yen.".format(annual_div))

    for k, v in df3.items():
        print(" * {:7,d} yen in {}.".format(int(v), k.replace("div", "")))

    hline()

    logger.info("mfreport finished.")


if __name__ == "__main__":
    main()
