from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger("swindle")


class FacebookAuthTester():
    def can_auth(self, user):
        driver = webdriver.Firefox()
        driver.get("https://www.facebook.com/")
        driver.implicitly_wait(1)

        driver.find_element_by_name("email").send_keys(user.testdata.email)
        driver.find_element_by_name("pass").send_keys(user.testdata.password)
        driver.find_element_by_id("login_form").submit()
        try:
            a = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "fbxWelcomeBoxName"))
            )
            driver.close()
            return True
        except TimeoutException:
            driver.close()
            return False


