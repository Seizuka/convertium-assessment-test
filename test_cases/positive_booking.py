from selenium import webdriver
from booking.booking_pages import BookingPage
from selenium.webdriver.chrome.service import Service
import time 
import json

def run ():
    with open('data/booking_data.json', 'r') as f:
        data = json.load(f)

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    driver.get("https://qa.cplwebops.com/book-a-test-drive/")

    booking_page = BookingPage(driver)
    booking_page.select_preferred_contact(data['preferred_contact'])
    booking_page.fill_form(
        data['first_name'],
        data['last_name'],
        data['email'],
        data['phone_number']
    )
    booking_page.fill_preferred_date(data['preferred_date'])
    booking_page.select_preferred_time(data['preferred_time'])
    booking_page.select_pax(data['pax'])
    booking_page.select_preferred_models_1(data['preferred_models_1'])
    booking_page.select_preferred_models_2(data['preferred_models_2'])
    booking_page.select_test_drive(data['test_drive'])
    booking_page.click_consent()
    booking_page.verify_submit_enabled()
    time.sleep(5)
    driver.quit()