import shutil

import plotext as plt


def hline():
    width = shutil.get_terminal_size().columns
    print("\u2500" * width)


class Writer:
    def __init__(self, df):
        self.df = df

    def write(self):
        hline()  # ------------------
        print(self.df)

        hline()  # ------------------
        gain = self.df["profit"].sum()
        print("Total unrealized capital gain is {:,d} yen.".format(gain))

        hline()  # ------------------
        df_divs = self.df.filter(regex="^div", axis=1)
        df_divs = df_divs.drop(["divTotal"], axis=1).sum()
        keys = []
        vals = []
        for k, v in df_divs.items():
            keys.append(k.replace("div", ""))
            vals.append(int(v))

        keys.reverse()
        vals.reverse()

        annual_div = int(self.df["divTotal"].sum())

        plt.plotsize(shutil.get_terminal_size().columns / 2, 20)
        t = "Monthly dividends (total annual dividend is {:,d} yen)"
        plt.title(t.format(annual_div))
        plt.bar(keys, vals, orientation="h", width=0.3)
        plt.show()

        hline()  # ------------------
