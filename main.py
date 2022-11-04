from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from prettytable import PrettyTable
from selenium.webdriver.support.ui import WebDriverWait
import time





driver = Booking()
driver.homepage()
driver.where_to_go("New York")
driver.when_to_go("2022-11-30", "2022-12-05")
driver.toggle_guests()
driver.increase_adults()
driver.increase_rooms()
driver.submit()
driver.stars(4)
driver.review_score(80)
driver.display()
driver.more_pages()
pages_to_see = int(input())
for x in range(pages_to_see):
    driver.next_page()
    driver.display()
