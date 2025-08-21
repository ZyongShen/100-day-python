from process_page import *
from aggregate_listings import *

if __name__ == "__main__":
    found_listings = find_all_listings()

    processed_listings = process_listings(found_listings)

    form_url = input("Provide the form URL: ")
    fill_forms(processed_listings, form_url)

