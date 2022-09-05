import argparse
import shutil

import pandas as pd

from mfreport.client import Client, example_html
from mfreport.logger import logger
from mfreport.parser import Parser
from mfreport.writer import Writer
from mfreport.yfwrapper import Yfwrapper


def get_params():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="username")
    parser.add_argument("-p", "--password", help="password")
    parser.add_argument("-o", "--otp", help="one time password")
    parser.add_argument(
        "-e",
        "--example",
        action="store_true",
        help="Use sample data instead of data downloaded from moneyforward",
    )
    return parser.parse_args()


def msg():
    return "Hello, world!"


def main():
    pd.options.display.precision = 0
    pd.options.display.max_columns = None
    pd.options.display.width = shutil.get_terminal_size().columns

    p = get_params()

    logger.info("mfreport started.")
    c = Client(p.user, p.password, p.otp)

    if p.example:
        logger.info("Using example data.")
        html = example_html
        logger.info("Done.")
    else:
        logger.info("Downloading from moneyforward.com started. Please wait.")
        html = c.get_html()
        logger.info("Done.")

    df1 = Parser(html).get_stock()

    logger.info("Downloading from yfinance started. Please wait.")
    df2 = Yfwrapper(df1["units"]).get_info()
    logger.info("Done.")

    df = pd.merge(df1, df2, left_index=True, right_index=True)
    Writer(df).write()

    logger.info("mfreport finished.")


if __name__ == "__main__":
    main()
