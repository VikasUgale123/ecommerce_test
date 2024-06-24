import pytest
from selenium.webdriver.common.by import By

def test_logout(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "login2").click()
    driver.find_element(By.ID, "loginusername").send_keys("validuser1")
    driver.find_element(By.ID, "loginpassword").send_keys("validpassword1")
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()
    driver.find_element(By.ID, "logout2").click()

