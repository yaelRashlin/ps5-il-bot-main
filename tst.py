import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import winsound
import configparser as configparser

# ------------------------------
# test_pass:
# ------------------------------
class selenium_init():
    def __init__(self) -> None:
        options = Options()
        options.add_argument("user-data-dir=C:\\Users\\ps5\\AppData\\Local\\Google\\Chrome\\User Data")
        self.driver = webdriver.Chrome('chromedriver.exe', options=options)