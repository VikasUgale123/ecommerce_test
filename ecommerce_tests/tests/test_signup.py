import pytest
from selenium.webdriver.common.by import By

def test_signup_positive(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "signin2").click()
    driver.find_element(By.ID, "sign-username").send_keys("newuser")
    driver.find_element(By.ID, "sign-password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()


def test_signup_negative(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "signin2").click()
    driver.find_element(By.ID, "sign-username").send_keys("")
    driver.find_element(By.ID, "sign-password").send_keys("")
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

