import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# fmt: off
URL = "https://id.moneyforward.com/sign_in/email"  # noqa: E501
XPATH_USER = "/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/input"  # noqa: E501
XPATH_USER_BTN = "/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[4]/input"  # noqa: E501
XPATH_PASSWORD = "/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/input[2]"  # noqa: E501
XPATH_PASSWORD_BTN = "/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[3]/input"  # noqa: E501
XPATH_OTP = "/html/body/main/div/div/div/section/div[1]/section/form/div[2]/div/div[1]/input"  # noqa: E501
XPATH_OTP_BTN = "/html/body/main/div/div/div/section/div[1]/section/form/div[2]/div/div[2]/input"  # noqa: E501
XPATH_ACCOUNT_BTN = "/html/body/main/div/div/div/div[1]/div/ul/li/a"  # noqa: E501
XPATH_TOP_BTN = "/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[2]/input"  # noqa: E501
XPATH_PORTFILIO_BTN = "/html/body/div[1]/div[1]/div[1]/header/div[2]/ul/li[4]/a"  # noqa: E501
# fmt: on


example_html = """
<div id="portfolio_det_eq">
    <table>
        <tbody>
            <tr>
                <td>IBM</td><!-- ticker -->
                <td></td>
                <td>30</td><!-- units -->
                <td></td>
                <td></td>
                <td>1,080,000円</td><!-- price -->
                <td><span></span></td>
                <td><span>222,222円</span></td><!-- profit -->
                <td><span></span></td>
                <td></td>
                <td></td>
                <td"></td>
                <td"></td>
            </tr>
            <tr>
                <td>7203</td><!-- ticker -->
                <td></td>
                <td>50</td><!-- units -->
                <td></td>
                <td></td>
                <td>100,000円</td><!-- price -->
                <td><span></span></td>
                <td><span>11,111円</span></td><!-- profit -->
                <td><span></span></td>
                <td></td>
                <td></td>
                <td"></td>
                <td"></td>
            </tr>
        </tbody>
    </table>
</div>
"""  # noqa: E501


class Client:
    def __init__(self, user, password, otp):
        self.user = user
        self.password = password
        self.otp = otp
        self.cache_name = "mf_portfolio_{}.html".format(
            datetime.date.today().strftime("%Y%m%d")
        )

    def get_html(self):
        if os.path.exists(self.cache_name):
            with open(self.cache_name) as f:
                return f.read()

        b = webdriver.Chrome(ChromeDriverManager().install())
        b.implicitly_wait(3)
        b.get(URL)

        b.find_element(By.XPATH, XPATH_USER).send_keys(self.user)
        b.find_element(By.XPATH, XPATH_USER_BTN).click()

        b.find_element(By.XPATH, XPATH_PASSWORD).send_keys(self.password)
        b.find_element(By.XPATH, XPATH_PASSWORD_BTN).click()

        b.find_element(By.XPATH, XPATH_OTP).send_keys(self.otp)
        b.find_element(By.XPATH, XPATH_OTP_BTN).click()

        b.find_element(By.XPATH, XPATH_ACCOUNT_BTN).click()
        b.find_element(By.XPATH, XPATH_TOP_BTN).click()
        b.find_element(By.XPATH, XPATH_PORTFILIO_BTN).click()

        html = b.find_element(By.XPATH, "//*").get_attribute("outerHTML")

        with open(self.cache_name, mode="w") as f:
            f.write(html)

        return html
