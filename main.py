import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from scraper.scraper import Scraper
from db.db_manager import DBManager

# database config
db = DBManager('./db/sqllitedb')

# web driver
s = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# targets
target_product_url = "https://www.barnesandnoble.com/w/effective-python-brett-slatkin/1130203296?ean=9780134853987"

basic_targets = {
    "title": '//*[@id="pdp-header-info"]/h1',
    "isbn_13": '//*[@id="ProductDetailsTab"]/table/tbody[1]/tr[1]/td',
    "publisher": '//*[@id="ProductDetailsTab"]/table/tbody[1]/tr[2]/td/a/span',
    "publication_date": '//*[@id="ProductDetailsTab"]/table/tbody[1]/tr[3]/td',
    "series": '//*[@id="ProductDetailsTab"]/table/tbody[1]/tr[4]/td/a',
    "edition_description": '//*[@id="ProductDetailsTab"]/table/tbody[1]/tr[5]/td',
    "pages": '//*[@id="ProductDetailsTab"]/table/tbody[1]/tr[6]/td',
    "sales_rank": '//*[@id="ProductDetailsTab"]/table/tbody[1]/tr[7]/td',
    "price": '//*[@id="pdp-cur-price"]'
}

product_dimensions = '//*[@id="ProductDetailsTab"]/table/tbody[1]/tr[8]/td'

def parse_dimensions(string):
    """Parse dimensions string into an array of Length, width, and height values."""
    parsed = re.findall(r"(\d*.\d\d)", string)
    return parsed


def main():
    print("Launcher scraper...")
    results = {}
    scraper = Scraper(driver, target_product_url)

    for target, xpath in basic_targets.items():
        results[target] = scraper.get_by_xpath(xpath).get_attribute("textContent")

    dimensions = scraper.get_by_xpath(product_dimensions).get_attribute("textContent")

    parsed = parse_dimensions(dimensions)
    results['product_width'] = parsed[0]
    results['product_height'] = parsed[1]
    results['product_depth'] = parsed[2]

    value_tuple = tuple(results.values())
    db.insert_book(value_tuple)
    print(f"Database entry saved: {results}")

    print("Scrape complete.")


if __name__ == "__main__":
    main()
