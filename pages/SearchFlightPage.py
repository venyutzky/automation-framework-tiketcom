from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from automation_framework_tiketcom.base.base_driver import BaseDriver

class SearchFlightPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait
    
    def select_flight_type(self):
        pulang_pergi_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Pulang-Pergi']")))
        pulang_pergi_button.click()
        time.sleep(1)
        sekali_jalan_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Sekali Jalan']")))
        sekali_jalan_button.click()
        time.sleep(1)
        
    def select_depart_from(self, departure_from):
        depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Kota atau bandara']")))
        depart_from.click()
        depart_from.send_keys(departure_from)
        all_depart_from = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='rowgroup']//li")))
        for result in all_depart_from:
            if "Jakarta" in result.text:
                time.sleep(1)
                result.click()
                break 
        time.sleep(2)
    
    def select_going_to(self, destination_to):
        going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Mau ke mana?']")))
        going_to.click()
        going_to.send_keys(destination_to)
        all_going_to = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='box-airport fadeInDown-enter-done']//div[@class='auto-body']//div[@class='row popular']//div[@class='col-xs-12']//ul//div//div[@aria-label='grid']//div/li")))
        for result in all_going_to:
            if "Padang" in result.text:
                time.sleep(1)
                result.click()
                break
        time.sleep(2)
        
    def select_depart_date(self, depart_date):
        select_date = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/table/tbody/tr//td')))
        for date in select_date:
            if date.get_attribute("aria-label") == depart_date:
                date.click()
                break
        time.sleep(1)
        
    def select_number_of_passenger(self):
        plus_penumpang_dewasa = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[1]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']")))
        plus_penumpang_dewasa.click()
        time.sleep(1)
        minus_penumpang_dewasa = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[1]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']")))
        minus_penumpang_dewasa.click()
        time.sleep(1)
        
        plus_penumpang_anak = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[2]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']")))
        plus_penumpang_anak.click()
        time.sleep(1)
        minus_penumpang_anak = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[2]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']")))
        minus_penumpang_anak.click()
        time.sleep(1)
        
        add_penumpang_bayi = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[3]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']")))
        add_penumpang_bayi.click()
        time.sleep(1)
        minus_penumpang_bayi = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[3]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']")))
        minus_penumpang_bayi.click()
        time.sleep(1)
    
    def select_cabin_type(self):
        kabin_premium_ekonomi = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Premium Ekonomi']")))
        kabin_premium_ekonomi.click()
        time.sleep(1)
        kabin_bisnis = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Bisnis']")))
        kabin_bisnis.click()
        time.sleep(1)
        kabin_first = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='First']")))
        kabin_first.click()
        time.sleep(1)
        kabin_ekonomi = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Ekonomi']")))
        kabin_ekonomi.click()
        time.sleep(1)
    
    def click_selesai_button(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='SELESAI']").click()
        time.sleep(1)
        
    def click_search_flight_button(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='CARI PENERBANGAN']").click()
        time.sleep(1)