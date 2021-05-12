from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, re


class Scraper:

    def __init__(self):
        self.chrome_options = Options()
        #self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument("--disable-infobars")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-popup-blocking")
        self.chrome_options.add_experimental_option("useAutomationExtension", False)
        self.chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])


    def scrap_web(self,url):
        self.driver = webdriver.Chrome ("C:/Users/escob/Documents/Projects/WebScrapingExample/chromedriver.exe"
                                   , options = self.chrome_options)
        self.driver.get(url)
    
    def send_isbn(self, isbn, xpath):
        _search_bar = self.driver.find_element_by_xpath(xpath)
        _search_bar.send_keys(isbn)
    
    def get_value(self, xpath):
        button = self.driver.find_element_by_xpath(xpath)
        button.click()
         
    def get_price(self, xpath):
        price = self.driver.find_element_by_xpath(xpath)
        string  = price.text
        pattern = '(?:[\£\$\€]{1}[,\d]+.?\d*)'
        price =  re.findall(pattern, string)
        return float(price[0][1:])
    
    def change_tab(self, xpath):
        if xpath == '0':
            pass
        else:
            _tab = self.driver.find_element_by_xpath(xpath)
            _tab.click()
    
    def click_basket(self, xpath):
        if xpath == '0':
            pass
        else:
            basket = self.driver.find_element_by_xpath(xpath)
            basket.click()
            time.sleep(3)
            basket = self.driver.find_element_by_xpath(xpath)
            basket.click()
            time.sleep(3)
    
    def driver_close(self):
        self.driver.close()