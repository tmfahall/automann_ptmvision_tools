from automann_log_in import go_to_and_log_in
from selenium_add_ons import get_element
from login_credentials import automann_username, automann_password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def clean_the_cart():
    driver = go_to_and_log_in()

    driver.get("https://www.automann.com/checkout/quickorder")

    cart_table_row_locator = (By.CSS_SELECTOR, "#shopping-cart-table > tbody > tr:nth-child(1)")
    cart_table_row = get_element(cart_table_row_locator, driver)


clean_the_cart()
