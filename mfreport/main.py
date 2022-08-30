import argparse

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


def main():
    logger.info("mfreport started.")
    p = get_params()

    logger.info("Downloading from moneyforward.com started. Please wait.")
    c = Client(p.user, p.password, p.otp)
    html = c.get_html()
    logger.info("Done.")

    logger.info("All stocks are as below:")
    df = Parser(html).get_stock()
    print(df)

    logger.info("All symbols are as below:")
    symbols = df.index.values.tolist()
    print(symbols)

    logger.info("Downloading from yfinance started. Please wait.")
    df2 = Yfwrapper(symbols=symbols).get_info()
    logger.info("Done.")

    logger.info("All infos are as below:")
    print(df2)

    logger.info("mfreport finished.")


if __name__ == "__main__":
    main()
