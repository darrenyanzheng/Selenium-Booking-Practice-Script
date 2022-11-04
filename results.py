from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from prettytable import PrettyTable
from selenium.webdriver.support.ui import WebDriverWait
import time


    # try except NoSuchElementException used because Booking.com will generate a completely different webpage with
    # different structure at times, using different HTML elements and selectors while retaining the same webpage layout /
    # look

    def stars(self, stars):
        stars = WebDriverWait(self, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'input[name="class={stars}"]')))
        # used javascript click instead of webdriver click because the WebDriver can't click on it
        driver.execute_script("arguments[0].click();", stars)

    def review_score(self, score):
        score = WebDriverWait(self, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'input[value="review_score={score}"]')))
        driver.execute_script("arguments[0].click();", score)

    def get_attributes(self):
        all_attributes = []
        hotel_block = self.find_element(By.ID, "search_results_table")

        # hotels is every div with that class which represents each hotel's information
        hotels = hotel_block.find_elements(By.CSS_SELECTOR,
                                           'div[data-testid="property-card"]')
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
            rating = rating_container.find_element(By.TAG_NAME, 'div')
            cleaned_rating = rating.get_attribute('innerHTML').strip()

            all_attributes.append([cleaned_name, cleaned_price, cleaned_rating])

        return all_attributes

    def display(self):
        time.sleep(2)
        table = PrettyTable(field_names=["Hotel Name", "Hotel Price", "Hotel Rating"])
        table.add_rows(self.get_attributes())
        print(table)

    def next_page(self):
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