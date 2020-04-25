import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '../webdiver/geckodriver')

class MainPage(object):
    def __init__(self):
        login_page = LoginPage()
        login_page.input_username('admin')
        login_page.input_password('idontKNOW666')
        login_page.click_login()
        self.driver = login_page.dirver     #把login_page的对象转移到main_page ,让下面可以使用元素识别
        self.companyname_showbox =self.dirver.find_element(By.XPATH,'//h1[@id="companyname"]')
        self.myzone_menu = self.dirver.find_element(By.XPATH,'//li[@data-id="my"]')
        self.Product_menu = self.dirver.find_element(By.XPATH,'//li[@data-id="product"]')
        self.username_showspan = self.dirver.find_element(By.XPATH, '//span[@class="user-name"]')

    def get_companyname(self):     #获取公司名称
        Value = self.companyname_showbox.get_attribute('title')
        return Value

    def goto_myzone(self):     #进入我的地盘菜单
        self.myzone_menu.click()

    def goto_product(self):     #进入产品菜单
        self.Product_menu.click()

    def get_unesrname(self):
        value = self.username_showspan.text
        return value

if __name__ == "__main__":
    main_page = MainPage()
    username= main_page.get_unesrname()
    print(username)
