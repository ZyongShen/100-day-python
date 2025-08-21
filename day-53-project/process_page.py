from bs4 import BeautifulSoup
import requests


def find_all_listings():
    url = "https://appbrewery.github.io/Zillow-Clone/"
    response = requests.get(url)
    page_html = response.text

    b_soup = BeautifulSoup(page_html, 'html.parser')

    all_listings = b_soup.find_all(class_='StyledPropertyCardDataWrapper')
    
    return all_listings

def process_listings(all_listings):
    # listing link: data-test=property-card-link
    # address: data-test=property-card-addr
    # prices: data-test=property-card-price

    processed_listings_data = []

    for listing in all_listings:
        parser = BeautifulSoup(str(listing), 'html.parser')
        listing_link_parser = parser.find(attrs={"data-test": "property-card-link"})
        address_parser = parser.find(attrs={"data-test": "property-card-addr"})
        price_parser = parser.find(attrs={"data-test": "property-card-price"})

        listing_link = listing_link_parser.get('href')
        listing_address = address_parser.text.strip()
        listing_price = price_parser.text.strip()

        processed_listings_data.append({
            "link": listing_link,
            "address": listing_address,
            "price": listing_price
        })

    return processed_listings_data




        
        

