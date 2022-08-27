from mfreport.client import Client
import argparse


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
    print(c.get_html())


if __name__ == "__main__":
    main()
