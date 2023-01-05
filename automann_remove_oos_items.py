from selenium_add_ons import get_element
from selenium.webdriver.common.by import By
from time import sleep


def clean_the_cart(driver):
    driver.get("https://www.automann.com/checkout/cart/")

    cart_table_locator = (By.CSS_SELECTOR, "#shopping-cart-table > tbody")
    cart_table = get_element(cart_table_locator, driver)

    sleep(10)

    counter_oos = 0

    # first pass to remove items that are completely out of stock
    for row in cart_table.find_elements(By.CSS_SELECTOR, "tr"):
        cell = row.find_element(By.CSS_SELECTOR, "td.col.qty > div.stock > ul > li:nth-child(1) > span")
        stock_status_full = cell.text.strip().lower()
        stock_status = stock_status_full[-2:]

        # find "Out of Stock"
        if stock_status == "ck":
            check_box = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) > input.select")
            check_box.click()
            counter_oos += 1

    if counter_oos > 0:
        move_to_out_of_stock_selector_locator = (By.CSS_SELECTOR, "#with_selected_action > optgroup:nth-child(2) > \
                                                                    option:nth-child(3)")
        move_to_out_of_stock_option_element = get_element(move_to_out_of_stock_selector_locator, driver)
        move_to_out_of_stock_option_element.click()

        submit_button_locator = (By.CSS_SELECTOR, "#with_selected_submit")
        submit_button = get_element(submit_button_locator, driver)
        submit_button.click()

    print(f"{counter_oos} items are out of stock")

    driver.get("https://www.automann.com/checkout/cart/")

    sleep(10)

    cart_table_locator = (By.CSS_SELECTOR, "#shopping-cart-table > tbody")
    cart_table = get_element(cart_table_locator, driver)

    counter_oos_il = 0

    # second pass to remove items that are out of stock in the currently selected location
    for row in cart_table.find_elements(By.CSS_SELECTOR, "tr"):
        cell = row.find_element(By.CSS_SELECTOR, "td.col.qty > div.stock > ul > li:nth-child(1) > span")
        stock_status_full = cell.text.strip().lower()
        stock_status = stock_status_full[-2:]

        # find if last 2 characters are in the list of possibles
        possible_locations = ["il", "ca", "tx", "nj"]
        if stock_status in possible_locations:
            check_box = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) > input.select")
            check_box.click()
            counter_oos_il += 1

    if counter_oos_il > 0:
        move_to_out_of_stock_il_selector_locator = (By.CSS_SELECTOR, "#with_selected_action > optgroup:nth-child(2) > \
                                                                    option:nth-child(4)")
        move_to_out_of_stock_option_element = get_element(move_to_out_of_stock_il_selector_locator, driver)
        move_to_out_of_stock_option_element.click()

        submit_button_locator = (By.CSS_SELECTOR, "#with_selected_submit")
        submit_button = get_element(submit_button_locator, driver)
        submit_button.click()

    print(f"{counter_oos_il} items out of stock from selected location")


clean_the_cart()
