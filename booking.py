from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from prettytable import PrettyTable
from selenium.webdriver.support.ui import WebDriverWait
import time


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\darre\chromedriver.exe"):
        super(Booking, self).__init__(driver_path)

    def homepage(self):
        self.maximize_window()
        self.get("https://www.booking.com/")
