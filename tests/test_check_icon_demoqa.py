# from selenium import webdriver
from selenium.webdriver.common.by import By


def test(browser):
    # driver = webdriver.Chrome()
    browser.get("https://demoqa.com/")

    # поиск элемента

    icon = browser.find_element(By.CSS_SELECTOR, '#app>header>a')

    if icon is None:
        print("Element is not found")
    else:
        print("Element is found")



