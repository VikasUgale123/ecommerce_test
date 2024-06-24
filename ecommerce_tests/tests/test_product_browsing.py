import pytest
from selenium.webdriver.common.by import By

def test_product_display(driver):
    driver.get("https://www.demoblaze.com/")
    products = driver.find_elements(By.CLASS_NAME, "card-title")
    assert len(products) > 0, "No products displayed on homepage"

def test_product_navigation(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.LINK_TEXT, "Laptops").click()

