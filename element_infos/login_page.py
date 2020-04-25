import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '../webdiver/geckodriver')

class LoginPage(object):
    def __init__(self):
        self.dirver = webdriver.Firefox()
        self.dirver.implicitly_wait(10)
        self.dirver.maximize_window()
        self.dirver.get("http://127.0.0.1/zentao/user-login.html")
        self.username_inputbox = self.dirver.find_element(By.XPATH,'//input[@name="account"]')  #属性===》页面的控件
        self.password_inputbox = self.dirver.find_element(By.XPATH,'//input[@name="password"]')
        self.login_button =  self.dirver.find_element(By.XPATH,'//button[@id="submit"]')
        self.Keeplogin_checkout =  self.dirver.find_element(By.XPATH,'//input[@name="keepLogin[]"]')

    def input_username(self,username):  #方法=====>控件的操作
        self.username_inputbox.send_keys(username)


    def input_password(self,password):
        self.password_inputbox.send_keys(password)


    def click_login(self):
        self.login_button.click()


if __name__ == "__main__":
    login_page = LoginPage()
    login_page.input_username('admin')
    login_page.input_password('idontKNOW666')
    login_page.click_login()