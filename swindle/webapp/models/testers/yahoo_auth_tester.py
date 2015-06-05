from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger("swindle")


class YahooAuthTester():
    def can_auth(self, user):
        driver = webdriver.Firefox()
        driver.get("https://login.yahoo.com/config/mail")
        driver.implicitly_wait(1)

        driver.find_element_by_id("login-username").send_keys(user.testdata.email)
        driver.find_element_by_id("login-passwd").send_keys(user.testdata.password)
        driver.find_element_by_id("login-signin").click()
        try:
            a = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "yucs-profile-panel"))
            )
            driver.close()
            return True
        except TimeoutException:
            driver.close()
            return False


