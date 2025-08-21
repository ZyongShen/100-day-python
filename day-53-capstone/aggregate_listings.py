from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill_forms(processed_data, form_url):
    driver = webdriver.Chrome()
    driver.get(form_url)

    time.sleep(2)

    for listing in processed_data:

        short_answer_inputs = driver.find_elements(By.XPATH, "//input[@jsname='YPqjbf']")
        
        short_answer_inputs[0].send_keys(listing["address"])
        short_answer_inputs[1].send_keys(listing["price"])
        short_answer_inputs[2].send_keys(listing["link"])

        submit_button = driver.find_element(By.XPATH, "//div[@aria-label='Submit']")
        submit_button.click()

        time.sleep(1)

        new_submission_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Submit another response")
        new_submission_link.click()

        time.sleep(3)

    driver.quit()

