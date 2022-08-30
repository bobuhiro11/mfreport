import argparse

from mfreport.client import Client
from mfreport.parser import Parser


def get_params():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="username")
    parser.add_argument("-p", "--password", help="password")
    parser.add_argument("-o", "--otp", help="one time password")
    return parser.parse_args()


def msg():
    return "Hello, world!"


def main():
    p = get_params()
    c = Client(p.user, p.password, p.otp)
    html = c.get_html()
    df = Parser(html).get_stock()
    print(df)


if __name__ == "__main__":
    main()
