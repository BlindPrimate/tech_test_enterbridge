import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from scraper.scraper import Scraper

s = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)

target_product_url = "https://www.barnesandnoble.com/w/effective-python-brett-slatkin/1130203296?ean=9780134853987"



def main():
    scraper = Scraper(driver, target_product_url)
    test = scraper.get_by_xpath('/html/body/main/div[3]/div[1]/section/div[2]/div/div[3]/div[1]/header/div/h1')
    print(test)



if __name__ == "__main__":
    main()
