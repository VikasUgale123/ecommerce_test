import pytest
from selenium.webdriver.common.by import By

def test_add_product_to_cart(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.LINK_TEXT, "Next").click()
    products = driver.find_elements(By.CLASS_NAME, "card-title")
    last_product = products[-1]
    last_product.click()
    driver.find_element(By.LINK_TEXT, "Add to cart").click()

