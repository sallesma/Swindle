from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger("swindle")


class TrelloAuthTester():
    def can_auth(self, user):
        driver = webdriver.Firefox()
        driver.get("https://trello.com/login")
        driver.implicitly_wait(1)

        driver.find_element_by_id("user").send_keys(user.username)
        driver.find_element_by_id("password").send_keys(user.testpassword.test_password)
        driver.find_element_by_id("login").click()

        try:
            a = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "header-boards"))
            )
            return True
        except TimeoutException:
            driver.close()
            return False


