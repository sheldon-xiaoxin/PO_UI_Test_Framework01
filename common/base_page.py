import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utills import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    #浏览器操作封装 ----> 二次封装
    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开url地址  %s'  %url)

       #浏览器的最大化
    def set_browser_max(self):
        self.dirver.maximize_window()
        logger.info('设置浏览器最大化')


    def set_browser_min(self):
        self.dirver.minimize_window()
        logger.info('浏览器最小化')

    def refresh(self):
        self.dirver.refresh()
        logger.info('浏览器刷新操作')


    def get_title(self):
        value = self.dirver.title
        logger.info('获取网页标题，标题是%s'  %value)
        return value


    #元素操作封装
    #element_info = {'element_name': '用户名输入框','locator_type': 'xpath','locator_value': '//button[@id="submit"] 'timeout': 5}
    #元素识别的封装
    def find_element(self,element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type =By.XPATH
        element = WebDriverWait(self.driver, locator_timeout) \
            .until(lambda x: x.find_element(locator_type, locator_value_info))
        logger.info('[%s]元素识别成功' % element_info['element_name'])
        # element = WebDriverWait(self.driver, locator_timeout)\
        #     .until(EC.presence_of_element_located((locator_type, locator_value_info)))
        return element

    # 点击元素方法
    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素进行点击操作' % element_info['element_name'])


    #输入元素的内容方法
    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容：%s' %(element_info['element_name'],content))
