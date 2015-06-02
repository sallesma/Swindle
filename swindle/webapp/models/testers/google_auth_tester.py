from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger("swindle")


class GoogleAuthTester():
    def can_auth(self, user):
        driver = webdriver.Firefox()
        driver.get("https://accounts.google.com/ServiceLogin#identifier")
        driver.implicitly_wait(1)

        driver.find_element_by_id("Email").send_keys(user.testdata.email)
        driver.get("https://accounts.google.com/ServiceLogin#password")
        driver.find_element_by_id("Passwd").send_keys(user.testdata.password)
        driver.find_element_by_id("signIn").submit()
        try:
            a = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "gb_E"))
            )
            email = driver.find_element_by_class_name("gb_E").get_attribute('innerHTML')
            driver.close()
            return email == user.testdata.email
        except TimeoutException:
            driver.close()
            return False


