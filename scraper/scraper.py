from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class Scraper:
    def __init__(self, web_driver, target_url):
        self._driver = web_driver
        self.target = self._driver.get(target_url)
        self._wait = WebDriverWait(self._driver, 20)

    def __del__(self):
        self._driver.quit()

    def get_by_xpath(self, xpath):
        return self._wait.until(ec.presence_of_element_located((By.XPATH, xpath)))

