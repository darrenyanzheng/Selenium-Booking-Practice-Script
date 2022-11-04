from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from prettytable import PrettyTable
from selenium.webdriver.support.ui import WebDriverWait

import time


class Search:
    def __init__(self, webdriver):
        self._webdriver = webdriver

    # try except NoSuchElementException used because Booking.com will generate a completely different webpage with
    # different structure at times, using different HTML elements and selectors while retaining the same webpage layout /
    # look

    def where_to_go(self, place_to_go):
        where_to_go = WebDriverWait(self._webdriver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name = "ss"]'))
        )
        where_to_go.send_keys(place_to_go)

        self._webdriver.implicitly_wait(3)
        try:
            first_element = self._webdriver.find_element(By.CSS_SELECTOR, 'ul li[data-i = "0"]')
            first_element.click()
        except NoSuchElementException:
            first_element = self._webdriver.find_element(By.CSS_SELECTOR, 'ul li div[tabindex = "-1"]')
            first_element.click()

    def when_to_go(self, check_in, check_out):
        try:
            check_in_element = self._webdriver.find_element(By.CSS_SELECTOR,
                                                            f'table td.bui-calendar__date[data-date="{check_in}"]')
            check_in_element.click()

            check_out_element = self._webdriver.find_element(By.CSS_SELECTOR,
                                                             f'table td.bui-calendar__date[data-date="{check_out}"]')
            check_out_element.click()

        except NoSuchElementException:
            calendar = self._webdriver.find_element(By.CSS_SELECTOR, 'button[data-testid="date-display-field-start"]')
            calendar.click()

            check_in_element = self._webdriver.find_element(By.CSS_SELECTOR,
                                                            f'table td span[tabindex = "-1"][role = "checkbox"][data-date="{check_in}"]')
            check_in_element.click()

            check_out_element = self._webdriver.find_element(By.CSS_SELECTOR,
                                                             f'table td span[tabindex = "-1"][role = "checkbox"][data-date="{check_out}"]')
            check_out_element.click()

    def toggle_guests(self):
        try:
            occupancy_config = self._webdriver.find_element("id", "xp__guests__toggle")
            occupancy_config.click()

        except NoSuchElementException:
            occupancy_config = self._webdriver.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
            occupancy_config.click()

    def increase_adults(self):
        try:
            increase_adult_button = self._webdriver.find_element(By.CSS_SELECTOR,
                                                                 'button[aria-label="Increase number of Adults"]')
            increase_adult_button.click()

        # xpath here when the layout changes and it is not clear which selector to use
        except NoSuchElementException:
            increase_adult_button = self._webdriver.find_element(By.XPATH,
                                                                 '//*[@id="indexsearch"]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[2]')
            increase_adult_button.click()

    def decrease_adults(self):
        try:
            decrease_adult_button = self._webdriver.find_element(By.CSS_SELECTOR,
                                                                 'button[aria-label="Decrease number of Adults"]')
            decrease_adult_button.click()

        except NoSuchElementException:
            decrease_adult_button = self._webdriver.find_element(By.CSS_SELECTOR, 'button[tabindex = "-1"]')
            decrease_adult_button.click()

    def increase_children(self):
        try:
            increase_children_button = self._webdriver.find_element(By.CSS_SELECTOR,
                                                                    'button[aria-label="Increase number of Children"]')
            increase_children_button.click()

        except NoSuchElementException:
            increase_children_button = self._webdriver.find_element(By.XPATH,
                                                                    '//*[@id="indexsearch"]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[2]/div[2]/button[2]')
            increase_children_button.click()

    def decrease_children(self):
        try:
            decrease_children_button = self._webdriver.find_element(By.CSS_SELECTOR,
                                                                    'button[aria-label="Decrease number of Children"]')
            decrease_children_button.click()

        except NoSuchElementException:
            decrease_children_button = self._webdriver.find_element(By.XPATH,
                                                                    '//*[@id="indexsearch"]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[2]/div[2]/button[1]')
            decrease_children_button.click()

    def increase_rooms(self):
        try:
            increase_room_button = self._webdriver.find_element(By.CSS_SELECTOR,
                                                                'button[aria-label="Increase number of Rooms"]')
            increase_room_button.click()

        except NoSuchElementException:
            increase_room_button = self._webdriver.find_element(By.XPATH,
                                                                '//*[@id="indexsearch"]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[3]/div[2]/button[2]')
            increase_room_button.click()

    def decrease_rooms(self):
        try:
            increase_room_button = self._webdriver.find_element(By.CSS_SELECTOR,
                                                                'button[aria-label="Decrease number of Rooms"]')
            increase_room_button.click()

        except NoSuchElementException:

            decrease_room_button = self._webdriver.find_element(By.XPATH,
                                                                '//*[@id="indexsearch"]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[3]/div[2]/button[1]')
            decrease_room_button.click()

    def submit(self):
        try:
            submit_button = self._webdriver.find_element(By.CSS_SELECTOR, "button.sb-searchbox__button ")
            submit_button.click()
        except NoSuchElementException:
            submit_button = self._webdriver.find_element(By.XPATH,
                                                         "/html/body/div[1]/div[2]/div/div/div/form/div[1]/div[4]/button/span")
            submit_button.click()
