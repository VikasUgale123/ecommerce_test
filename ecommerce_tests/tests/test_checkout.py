import pytest
from selenium.webdriver.common.by import By

def test_successful_checkout(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "cartur").click()
    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()


def test_checkout_without_products(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "cartur").click()
    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

