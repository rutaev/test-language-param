import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_btn_availability(browser):
    browser.get(link)
    add_to_basket_btn = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))
    assert add_to_basket_btn != 0, "Не найдена кнопка 'Добавить в корзину'"
