from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def set_driver_options() -> webdriver.Chrome:
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-gpu")
    # option.add_argument("--headless")
    option.add_argument(f"user-agent={UserAgent().random}")
    driver = webdriver.Chrome(options=option)
    return driver
