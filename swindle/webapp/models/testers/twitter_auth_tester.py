from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger("swindle")


class TwitterAuthTester():
    def can_auth(self, user):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("https://twitter.com/")

        driver.find_element_by_id("signin-email").send_keys(user.testdata.email)
        driver.find_element_by_id("signin-password").send_keys(user.testdata.password)
        driver.find_element_by_id("signin-password").submit()

        try:
            a = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "user-dropdown"))
            )
            driver.close()
            return True
        except TimeoutException:
            driver.get("https://twitter.com/")

            driver.find_element_by_id("signin-email").send_keys(user.testdata.username)
            driver.find_element_by_id("signin-password").send_keys(user.testdata.password)
            driver.find_element_by_id("signin-password").submit()

            try:
                a = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "user-dropdown"))
                )
                driver.close()
                return True
            except TimeoutException:
                driver.close()
                return False


