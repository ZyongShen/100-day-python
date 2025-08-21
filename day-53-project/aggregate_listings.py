from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill_forms(processed_data):
    driver = webdriver.Chrome()
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfhbI3cDLxOobzzloCQT91Xp9DkxeKwMRIhiHSsCvaziSvsVg/viewform")

    time.sleep(1)

    for listing in processed_data:

        short_answers_input = driver.find_elements(By.CLASS_NAME, "whsOnd zHQkBf")

        print(short_answers_input)

        # short_answers_input[0].send_keys(listing["address"])
        # short_answers_input[1].send_keys(listing["price"])
        # short_answers_input[2].send_keys(listing["link"])

        # submit_button = driver.find_elements(By.CLASS_NAME, "NPEfkd RveJvd snByac")
        # submit_button.click()

        time.sleep(5)

    
    driver.quit()