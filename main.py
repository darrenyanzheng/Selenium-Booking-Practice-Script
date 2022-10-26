from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from prettytable import PrettyTable
import time


# try except NoSuchElementException used because Booking.com will generate a completely different webpage with
# different structure at times, using different HTML elements and selectors while retaining the same webpage layout /
# look
class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\darre\chromedriver.exe"):
        super(Booking, self).__init__(driver_path)

    def homepage(self):
        self.maximize_window()
        self.get("https://www.booking.com/")

    def where_to_go(self, place_to_go):
        self.implicitly_wait(2)
        where_to_go = self.find_element(By.CSS_SELECTOR, 'input[name = "ss"]')
        where_to_go.send_keys(place_to_go)
        self.implicitly_wait(4)
        try:
            first_element = self.find_element(By.CSS_SELECTOR, 'ul li[data-i = "0"]')
            first_element.click()
        except NoSuchElementException:
            first_element = self.find_element(By.CSS_SELECTOR, 'li div[tabindex = "-1"]')
            first_element.click()

    def when_to_go(self, check_in, check_out):
        self.implicitly_wait(2)
        try:
            check_in_element = self.find_element(By.CSS_SELECTOR,
                                                 f'table td.bui-calendar__date[data-date="{check_in}"]')
            check_in_element.click()

            self.implicitly_wait(2)

            check_out_element = self.find_element(By.CSS_SELECTOR,
                                                  f'table td.bui-calendar__date[data-date="{check_out}"]')
            check_out_element.click()

        except NoSuchElementException:

            calendar = self.find_element(By.CSS_SELECTOR, 'button[data-testid="date-display-field-start"]')
            calendar.click()

            check_in_element = self.find_element(By.CSS_SELECTOR,
                                                 f'table td span[tabindex = "-1"][role = "checkbox"][data-date="{check_in}"]')
            check_in_element.click()

            self.implicitly_wait(2)

            check_out_element = self.find_element(By.CSS_SELECTOR,
                                                  f'table td span[tabindex = "-1"][role = "checkbox"][data-date="{check_out}"]')
            check_out_element.click()

    def toggle_guests(self):
        self.implicitly_wait(2)
        try:
            occupancy_config = self.find_element("id", "xp__guests__toggle")
            occupancy_config.click()

        except NoSuchElementException:
            occupancy_config = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
            occupancy_config.click()

    def increase_adults(self):
        self.implicitly_wait(2)

        try:
            increase_adult_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
            increase_adult_button.click()

        # xpath here when the layout changes and it is not clear which selector to use
        except NoSuchElementException:
            increase_adult_button = self.find_element(By.XPATH,
                                                      '//*[@id="indexsearch"]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[2]')
            increase_adult_button.click()

    def decrease_adults(self):
        self.implicitly_wait(2)

        try:
            decrease_adult_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
            decrease_adult_button.click()

        except NoSuchElementException:
            decrease_adult_button = self.find_element(By.CSS_SELECTOR, 'button[tabindex = "-1"]')
            decrease_adult_button.click()

    def increase_children(self):

        try:
            increase_children_button = self.find_element(By.CSS_SELECTOR,
                                                         'button[aria-label="Increase number of Children"]')
            increase_children_button.click()

        except NoSuchElementException:
            increase_children_button = self.find_element(By.XPATH,
                                                         '//*[@id="indexsearch"]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[2]/div[2]/button[2]')
            increase_children_button.click()

    def decrease_children(self):

        try:
            decrease_children_button = self.find_element(By.CSS_SELECTOR,
                                                         'button[aria-label="Decrease number of Children"]')
            decrease_children_button.click()

        except NoSuchElementException:
            decrease_children_button = self.find_element(By.XPATH,
                                                         '//*[@id="indexsearch"]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[2]/div[2]/button[1]')
            decrease_children_button.click()

    def increase_rooms(self):
        try:
            increase_room_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]')
            increase_room_button.click()

        except NoSuchElementException:
            increase_room_button = self.find_element(By.XPATH,
                                                     '//*[@id="indexsearch"]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[3]/div[2]/button[2]')
            increase_room_button.click()

    def decrease_rooms(self):

        try:
            increase_room_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Rooms"]')
            increase_room_button.click()

        except NoSuchElementException:

            decrease_room_button = self.find_element(By.XPATH,
                                                     '//*[@id="indexsearch"]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[3]/div[2]/button[1]')
            decrease_room_button.click()

    def submit(self):
        try:
            submit_button = self.find_element(By.CSS_SELECTOR, "button.sb-searchbox__button ")
            submit_button.click()
        except NoSuchElementException:
            submit_button = self.find_element(By.XPATH,
                                              "/html/body/div[1]/div[2]/div/div/div/form/div[1]/div[4]/button/span")
            submit_button.click()

    def stars(self, stars):
        self.implicitly_wait(7)
        stars = self.find_element(By.CSS_SELECTOR, f'input[name="class={stars}"]')
        # used javascript click instead of webdriver click because the WebDriver can't click on it
        driver.execute_script("arguments[0].click();", stars)

    def review_score(self, score):
        self.implicitly_wait(5)
        score = self.find_element(By.CSS_SELECTOR, f'input[value="review_score={score}"]')
        driver.execute_script("arguments[0].click();", score)

    def get_attributes(self):
        self.implicitly_wait(2)
        all_attributes = []

        hotel_block = self.find_element(By.ID, "search_results_table")

        # hotels is every div with that class which represents each hotel's information
        hotels = hotel_block.find_elements(By.CSS_SELECTOR,
                                           'div[class="a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942"]')

        for hotel in hotels:
            # finding the average price per night from finding the string that says how many nights

            name = hotel.find_element(By.CSS_SELECTOR,
                                      'div[data-testid="title"]')

            # each .strip() is to remove the potential for trailing spaces for the cleaned attribute
            cleaned_name = name.get_attribute('innerHTML').strip()

            try:
                price_container = hotel.find_element(By.CSS_SELECTOR,
                                           'div[data-testid="price-and-discounted-price"]')

                discount_and_regular_price = price_container.find_elements(By.TAG_NAME, 'span')

                if len(discount_and_regular_price) == 2:
                    index = 0
                    cleaned_price = ""
                    for price in discount_and_regular_price:
                        if index == 1:
                            cleaned_price = price.get_attribute('innerHTML').strip()
                        index += 1
                else:
                    cleaned_price = discount_and_regular_price[0].get_attribute('innerHTML').strip()
            except NoSuchElementException:
                price_container = hotel.find_element(By.CSS_SELECTOR,
                                                     'span[data-testid="price-and-discounted-price"]')

                cleaned_price = price_container.get_attribute('innerHTML').strip()

            rating_container = hotel.find_element(By.CSS_SELECTOR,
                                        'div[data-testid="review-score"]')
            rating = rating_container.find_element(By. TAG_NAME, 'div')
            cleaned_rating = rating.get_attribute('innerHTML').strip()

            all_attributes.append([cleaned_name, cleaned_price, cleaned_rating])

        return all_attributes

    def display(self):
        time.sleep(2)
        table = PrettyTable(field_names=["Hotel Name", "Hotel Price", "Hotel Rating"])
        table.add_rows(self.get_attributes())
        print(table)

    def next_page(self):
        self.implicitly_wait(2)
        next_page = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next page"]')
        driver.execute_script("arguments[0].click();", next_page)

    def more_pages(self):
        # take from the HTML the amount of leftover properties
        amount_of_properties = driver.find_element(By.CSS_SELECTOR, 'div[class="d8f77e681c"]')
        cleaned_amount_of_properties = amount_of_properties.get_attribute('innerHTML').strip()

        # split the string bc on the page it says the location and : amount of properties, and the number is
        # before the space that separates it from the word 'properties'
        the_number_of_properties = cleaned_amount_of_properties.split(': ')[1].split(' ')[0]
        pages_left = int(the_number_of_properties) - 25
        pages_left_plus_1 = pages_left // 25 + 1
        print(
            f'Would you like to see more hotels? {pages_left} left or {pages_left_plus_1} pages more. Type in a number that\'s {pages_left_plus_1} or fewer.')


driver = Booking()
driver.homepage()
driver.where_to_go("New York")
driver.when_to_go("2022-10-30", "2022-11-05")
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
