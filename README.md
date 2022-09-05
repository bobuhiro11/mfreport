# mfreport

[![test](https://github.com/bobuhiro11/mfreport/actions/workflows/test.yaml/badge.svg)](https://github.com/bobuhiro11/mfreport/actions/workflows/test.yaml)
[![License](https://img.shields.io/github/license/bobuhiro11/mfreport.svg)](https://github.com/bobuhiro11/mfreport/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/mfreport.svg)](https://badge.fury.io/py/mfreport)
[![Python Versions](https://img.shields.io/pypi/pyversions/mfreport.svg?logo=python&logoColor=white)](https://pypi.org/project/mfreport)
[![codecov](https://codecov.io/gh/bobuhiro11/mfreport/branch/main/graph/badge.svg)](https://codecov.io/gh/bobuhiro11/mfreport)

mfreport retrieves a list of assets from moneyforward.com, formats and outputs it.
Please use this tool for personal purposes only.

## Usage

```bash
$ pip install mfreport
$ mfreport -h
usage: main.py [-h] [-u USER] [-p PASSWORD] [-o OTP] [-e]

options:
  -h, --help            show this help message and exit
  -u USER, --user USER  username
  -p PASSWORD, --password PASSWORD
                        password
  -o OTP, --otp OTP     one time password
  -e, --example         Use sample data instead of data downloaded from moneyforward
```

## Example

```bash
$ mfreport -e
2022-09-05 18:54:23,097 mfreport started.
2022-09-05 18:54:23,097 Using example data.
2022-09-05 18:54:23,097 Done.
2022-09-05 18:54:23,098 Downloading from yfinance started. Please wait.
2022-09-05 18:54:23,099 Done.
──────────────────────────────────────────────────────────────────────────────────────────────────
        units    price  profit                        shortName  divTotal  divJan  divFeb  \
IBM        30  1080000  222222  International Business Machines     26707       0    6571
7203.T     50   100000   11111                     TOYOTA MOTOR      2550       0       0

        divMar  divApr  divMay  divJun  divJul  divAug  divSep  divOct  divNov  divDec
IBM          0       0    6611       0       0    6611       0       0    6915       0
7203.T    1350       0       0       0       0       0    1200       0       0       0
──────────────────────────────────────────────────────────────────────────────────────────────────
Total unrealized capital gain is 233,333 JPY.
──────────────────────────────────────────────────────────────────────────────────────────────────
            Monthly dividends (total annual dividend is 29,257 JPY)
   ┌──────────────────────────────────────────────────────────────────────┐
Jan┤                                                                      │
Feb┤███████████████████████████████████████████████████████████████████   │
Mar┤██████████████                                                        │
Apr┤                                                                      │
May┤███████████████████████████████████████████████████████████████████   │
Jun┤                                                                      │
Jul┤                                                                      │
Aug┤███████████████████████████████████████████████████████████████████   │
Sep┤█████████████                                                         │
Oct┤                                                                      │
Nov┤██████████████████████████████████████████████████████████████████████│
Dec┤                                                                      │
   └┬────────────────┬─────────────────┬────────────────┬────────────────┬┘
    0.0           1728.5            3457.0           5185.5         6914.0
──────────────────────────────────────────────────────────────────────────────────────────────────
2022-09-05 18:54:23,104 mfreport finished.
```
