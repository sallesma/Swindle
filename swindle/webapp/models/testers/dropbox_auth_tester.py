from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger("swindle")


class DropboxAuthTester():
    def can_auth(self, user):
        driver = webdriver.Firefox()
        driver.get("https://www.dropbox.com/login")
        driver.implicitly_wait(1)

        driver.find_element_by_css_selector(".login-form input[name='login_email']").send_keys(user.testdata.email)
        driver.find_element_by_css_selector(".login-form input[name='login_password']").send_keys(user.testdata.password)
        driver.find_element_by_css_selector(".login-form button[type='submit']").click()
        try:
            a = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "browse"))
            )
            driver.close()
            return True
        except TimeoutException:
            driver.close()
            return False


