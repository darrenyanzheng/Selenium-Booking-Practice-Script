from booking import Booking
from search import Search
from results import Results
driver = Booking()
driver.homepage()

search = Search(driver)
search.where_to_go("New York")
search.when_to_go("2022-11-30", "2022-12-05")
search.toggle_guests()
search.increase_adults()
search.increase_rooms()
search.submit()

results = Results(driver)
results.stars(4)
results.review_score(80)
results.display()
# results.more_pages()
# pages_to_see = int(input())
# for x in range(pages_to_see):
#     results.next_page()
#     results.display()
