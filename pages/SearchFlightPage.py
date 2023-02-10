from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from automation_framework_tiketcom.base.base_driver import BaseDriver

class SearchFlightPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def select_flight_type(self):
        pulang_pergi_button = self.wait_until_element_is_clickable(By.XPATH, "//label[normalize-space()='Pulang-Pergi']")
        pulang_pergi_button.click()
        time.sleep(1)
        sekali_jalan_button = self.wait_until_element_is_clickable(By.XPATH, "//label[normalize-space()='Sekali Jalan']")
        sekali_jalan_button.click()
        time.sleep(1)
        
    def select_depart_from(self, departure_from):
        depart_from = self.wait_until_element_is_clickable(By.XPATH, "//input[@placeholder='Kota atau bandara']")
        depart_from.click()
        depart_from.send_keys(departure_from)
        all_depart_from = self.wait_for_presence_of_all_elements_located(By.XPATH, "//div[@role='rowgroup']//li")
        for result in all_depart_from:
            if "Jakarta" in result.text:
                time.sleep(1)
                result.click()
                break 
        time.sleep(2)
    
    def select_going_to(self, destination_to):
        going_to = self.wait_until_element_is_clickable(By.XPATH, "//input[@placeholder='Mau ke mana?']")  
        going_to.click()
        going_to.send_keys(destination_to)
        all_going_to = self.wait_for_presence_of_all_elements_located(By.XPATH,"//div[@class='box-airport fadeInDown-enter-done']//div[@class='auto-body']//div[@class='row popular']//div[@class='col-xs-12']//ul//div//div[@aria-label='grid']//div/li")
        for result in all_going_to:
            if "Padang" in result.text:
                time.sleep(1)
                result.click()
                break
        time.sleep(2)
        
    def select_depart_date(self, depart_date):
        select_date = self.wait_for_presence_of_all_elements_located(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/table/tbody/tr//td')
        for date in select_date:
            if date.get_attribute("aria-label") == depart_date:
                date.click()
                break
        time.sleep(1)
        
    def add_adult_passenger_number(self):
        add_adult_passenger = self.wait_until_element_is_clickable(By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[1]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']")
        add_adult_passenger.click()
        time.sleep(1)
        
    def subtract_adult_passenger_number(self):
        subtract_adult_passenger = self.wait_until_element_is_clickable(By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[1]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']")
        subtract_adult_passenger.click()
        time.sleep(1)
    
    def add_child_passenger_number(self):
        add_child_passenger = self.wait_until_element_is_clickable(By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[2]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']")
        add_child_passenger.click()
        time.sleep(1)
        
    def subtract_child_passenger_number(self):
        subtract_child_passenger = self.wait_until_element_is_clickable(By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[2]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']")
        subtract_child_passenger.click()
        time.sleep(1)
    
    def add_baby_passenger_number(self):    
        add_baby_passenger = self.wait_until_element_is_clickable(By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[3]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']")
        add_baby_passenger.click()
        time.sleep(1)
    
    def subtract_baby_passenger_number(self):
        subtract_baby_passenger = self.wait_until_element_is_clickable(By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[3]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']")
        subtract_baby_passenger.click()
        time.sleep(1)
    
    def select_premium_ekonomi_cabin(self):
        kabin_premium_ekonomi = self.wait_until_element_is_clickable(By.XPATH, "//label[normalize-space()='Premium Ekonomi']")
        kabin_premium_ekonomi.click()
        time.sleep(1)
    
    def select_bisnis_cabin(self):    
        kabin_bisnis = self.wait_until_element_is_clickable(By.XPATH, "//label[normalize-space()='Bisnis']")
        kabin_bisnis.click()
        time.sleep(1)
        
    def select_first_cabin(self):    
        kabin_first = self.wait_until_element_is_clickable(By.XPATH, "//label[normalize-space()='First']")
        kabin_first.click()
        time.sleep(1)
    
    def select_ekonomi_cabin(self):    
        kabin_ekonomi = self.wait_until_element_is_clickable(By.XPATH, "//label[normalize-space()='Ekonomi']")
        kabin_ekonomi.click()
        time.sleep(1)
    
    def click_selesai_button(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='SELESAI']").click()
        time.sleep(1)
        
    def click_search_flight_button(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='CARI PENERBANGAN']").click()
        time.sleep(1)