import pytest
from selenium.webdriver.common.by import By

login_data = [
    ("validuser1", "validpassword1", "success"),
    ("validuser2", "validpassword2", "success"),
    ("invaliduser1", "invalidpassword1", "failure"),
    ("invaliduser2", "invalidpassword2", "failure")
]


@pytest.mark.parametrize("username,password,expected_result", login_data)
def test_login(driver, username, password, expected_result):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "login2").click()
    driver.find_element(By.ID, "loginusername").send_keys(username)
    driver.find_element(By.ID, "loginpassword").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    if expected_result == "success":
        assert driver.find_element(By.ID, "logout2").is_displayed(), "Login failed for valid credentials"
    else:
        assert driver.find_element(By.ID, "login2").is_displayed(), "Login succeeded for invalid credentials"
