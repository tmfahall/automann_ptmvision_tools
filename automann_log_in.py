from selenium_add_ons import get_element
from login_credentials import automann_username2, automann_password2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from time import sleep


def go_to_and_log_in():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    def go_to_website():
        driver.get("https://www.automann.com/customer/account/login")
        sleep(2)
        driver.maximize_window()

    def log_in():
        email_input_locator = (By.CSS_SELECTOR, "#email")
        email_input = get_element(email_input_locator, driver)
        email_input.send_keys(automann_username2)

        password_input_locator = (By.CSS_SELECTOR, "#pass")
        password_input = get_element(password_input_locator, driver)
        password_input.send_keys(automann_password2)

        log_in_button_locator = (By.CSS_SELECTOR, "#send2")
        log_in_button = get_element(log_in_button_locator, driver)
        log_in_button.click()

    go_to_website()
    log_in()

    return driver
