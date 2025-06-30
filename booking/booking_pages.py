import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BookingPage:
    def __init__ (self, driver):
        self.driver = driver
        self.first_name = (By.ID, "input_1_1_3")
        self.last_name = (By.ID, "input_1_1_6")
        self.preferred_contact = (By.ID, "input_1_11")
        self.email = (By.ID, "input_1_2")
        self.phone_number = (By.ID, "input_1_5")
        self.preferred_date = (By.ID, "input_1_13")
        self.preferred_time = (By.ID, "input_1_12")
        self.pax = (By.ID, "input_1_22")
        self.preferred_models_1 = (By.ID, "label_1_17_5")
        self.preferred_models_2 = (By.ID, "label_1_17_7")
        self.test_drive = (By.ID, "input_1_19")
        self.consent = (By.ID, "label_1_20_1")
        self.submit = (By.ID, "gform_submit_button_1")

    def fill_form(self, first_name, last_name, email, phone_number):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.phone_number).send_keys(phone_number)
    
    def select_preferred_contact(self, preferred_contacts: str):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.preferred_contact)
        )
        select_contact = Select(self.driver.find_element(*self.preferred_contact))
        select_contact.select_by_visible_text(preferred_contacts)

    def fill_preferred_date(self, date_value: str):
        date_field = self.driver.find_element(*self.preferred_date)
        date_field.clear()
        date_field.send_keys(date_value)

    def select_preferred_time(self, preferred_time: str):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.preferred_time)
        )
        select_time = Select(self.driver.find_element(*self.preferred_time))
        select_time.select_by_visible_text(preferred_time)
        try:
            self.driver.find_element(By.XPATH, "//body").click()
        except:
            pass
    
    def select_pax(self, pax):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.pax)
        )
        input_pax = Select(self.driver.find_element(*self.pax))
        input_pax.select_by_visible_text(str(pax))
    
    def select_preferred_models_1(self, model_name):
        choose_models = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(self.preferred_models_1)
        )
         # Scroll down to find the element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", choose_models)

        # click using javascript to avoid intercept
        self.driver.execute_script("arguments[0].click();", choose_models)

    def select_preferred_models_2(self, model_name):
        choose_models = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(self.preferred_models_2)
        )
         # Scroll down to find the element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", choose_models)

        # click using javascript to avoid intercept
        self.driver.execute_script("arguments[0].click();", choose_models)

    def select_test_drive(self, test_drive: str):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.test_drive)
        )
        input_test_drive = Select(self.driver.find_element(*self.test_drive))
        input_test_drive.select_by_visible_text(test_drive)
    
    def click_consent(self):
        consent_element = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(self.consent)
        )
         # Scroll down to find the element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", consent_element)

        # click using javascript to avoid intercept
        self.driver.execute_script("arguments[0].click();", consent_element)
    
    def verify_submit_enabled(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.submit)
        )
        assert submit_button.is_enabled(), "Submit button is disabled"
        print("Submit button is enabled.")

