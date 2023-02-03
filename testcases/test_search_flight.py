from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
from tiketcom.pages.HomePage import HomePage



class TestSearchFlight:
    
    def test_search_flight(self):
        
        # setup
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['Enable-logging'])
        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.tiket.com/")
        time.sleep(1)
        
        # click plane icon
        # plane_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index_header_inner__ZgIbg']/div[@class='index_content__k_CP2 index_desktop_only__ss43k']//div[@class='SearchForm_verticalIcons__7QwNj']//div[@class='VerticalIcons_listIcon__rGlIP']//div[@class='VerticalIcons_wrapper__4jHIR']//ul[@class='VerticalIcons_lastGrid__93rXJ']//li[1]//a[1]")))
        # plane_icon.click()
        # time.sleep(1)
        
        click_icon = HomePage(self.driver)
        click_icon.click_plane_icon()
        
        # choose flight type
        pulang_pergi_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Pulang-Pergi']")))
        pulang_pergi_button.click()
        time.sleep(1)
        sekali_jalan_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Sekali Jalan']")))
        sekali_jalan_button.click()
        time.sleep(1)
        
        # select going from location
        depart_from = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Kota atau bandara']")))
        depart_from.click()
        depart_from.send_keys("jak")
        all_depart_from = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='rowgroup']//li")))
        
        for result in all_depart_from:
            if "Jakarta" in result.text:
                result.click()
                break
            
        time.sleep(2)
        
        # select going to location
        going_to = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Mau ke mana?']")))
        going_to.click()
        going_to.send_keys("pad")
        
        all_going_to = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='box-airport fadeInDown-enter-done']//div[@class='auto-body']//div[@class='row popular']//div[@class='col-xs-12']//ul//div//div[@aria-label='grid']//div/li")))
        
        for result in all_going_to:
            if "Padang" in result.text:
                result.click()
                break
            
        time.sleep(2)
        
        # select date
        select_date = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/table/tbody/tr//td')))
        
        for date in select_date:
            if date.get_attribute("aria-label") == "Choose Sabtu, 11 Februari 2023 as your check-in date. It’s available.":
                date.click()
                break
        time.sleep(1)
        
        # Provide passenger number
        plus_penumpang_dewasa = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[1]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']")))
        plus_penumpang_dewasa.click()
        time.sleep(1)
        minus_penumpang_dewasa = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[1]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']")))
        minus_penumpang_dewasa.click()
        time.sleep(1)
        
        plus_penumpang_anak = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[2]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']")))
        plus_penumpang_anak.click()
        time.sleep(1)
        minus_penumpang_anak = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[2]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']")))
        minus_penumpang_anak.click()
        time.sleep(1)
        
        add_penumpang_bayi = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[3]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']")))
        add_penumpang_bayi.click()
        time.sleep(1)
        minus_penumpang_bayi = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xs-6 col-passenger']//ul/li[3]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']")))
        minus_penumpang_bayi.click()
        time.sleep(1)
        
        # Provide cabin type
        kabin_premium_ekonomi = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Premium Ekonomi']")))
        kabin_premium_ekonomi.click()
        time.sleep(1)
        kabin_bisnis = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Bisnis']")))
        kabin_bisnis.click()
        time.sleep(1)
        kabin_first = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='First']")))
        kabin_first.click()
        time.sleep(1)
        kabin_ekonomi = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Ekonomi']")))
        kabin_ekonomi.click()
        time.sleep(1)
        
        # click on SELESAI button
        driver.find_element(By.XPATH, "//button[normalize-space()='SELESAI']").click()
        time.sleep(1)
        
        # click on flight search button
        driver.find_element(By.XPATH, "//button[normalize-space()='CARI PENERBANGAN']").click()
        time.sleep(1)
        
        # click on pop up card
        driver.find_element(By.XPATH, "//div[@class='comp-info-box']//div[@class='v3-btn v3-btn__blue list-horizontal__middle btn-action']").click()
        time.sleep(1)
        
        # scroll down page
        pageLength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match =  False
        while (match == False):
            lastCount = pageLength
            time.sleep(1)
            pageLength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True
                           
        time.sleep(4)
        
        

search_flight = TestSearchFlight()
search_flight.test_search_flight()
        