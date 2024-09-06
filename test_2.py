from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options)
    driver.get('https://10.0.5.67/')
    driver.implicitly_wait(20)
    
    return driver

def test_login(driver):
    login = driver.find_element(by=By.CSS_SELECTOR, value='div.form-group:nth-child(1) > label:nth-child(1) > input:nth-child(1)')
    login.send_keys('admin')

    password = driver.find_element(by=By.CSS_SELECTOR, value='.input__element_password')
    password.send_keys('admin')

    button = driver.find_element(by=By.CSS_SELECTOR, value='.button')
    button.click()

    time.sleep(1)

    assert driver.current_url == 'https://10.0.5.67/app/task-new'
