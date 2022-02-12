from __future__ import annotations
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class Scraper:
    def __init__(self, web_driver: webdriver, target_url: str):
        self._driver = web_driver
        self.target = self._driver.get(target_url)
        self._wait = WebDriverWait(self._driver, 20)

    def __del__(self):
        self._driver.quit()

    def get_by_xpath(self, xpath: str) -> WebElement:
        return self._wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
