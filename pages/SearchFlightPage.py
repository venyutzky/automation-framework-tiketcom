from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from automation_framework_tiketcom.base.base_driver import BaseDriver

class SearchFlightPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    # Locator
    PULANG_PERGI_FIELD = "//label[normalize-space()='Pulang-Pergi']"
    SEKALI_JALAN_FIELD = "//label[normalize-space()='Sekali Jalan']"
    DEPART_FROM_FIELD =  "//input[@placeholder='Kota atau bandara']"
    ALL_DEPART_FROM = "//div[@role='rowgroup']//li"
    GOING_TO_FIELD = "//input[@placeholder='Mau ke mana?']"
    ALL_GOING_TO = "//div[@class='box-airport fadeInDown-enter-done']//div[@class='auto-body']//div[@class='row popular']//div[@class='col-xs-12']//ul//div//div[@aria-label='grid']//div/li"
    ALL_DATES = '//*[@id="formhome"]/div/div/div[1]/div[3]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/table/tbody/tr//td'
    ADD_ADULT_PASSENGER_BUTTON = "//div[@class='col-xs-6 col-passenger']//ul/li[1]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']"
    SUBSTRACT_ADULT_PASSENGER_BUTTON = "//div[@class='col-xs-6 col-passenger']//ul/li[1]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']"
    ADD_CHILD_PASSENGER_BUTTON = "//div[@class='col-xs-6 col-passenger']//ul/li[2]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']"
    SUBSTRACT_CHILD_PASSENGER_BUTTON = "//div[@class='col-xs-6 col-passenger']//ul/li[2]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']"
    ADD_BABY_PASSENGER_BUTTON = "//div[@class='col-xs-6 col-passenger']//ul/li[3]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-plus']"
    SUBSTRACT_BABY_PASSENGER_BUTTON = "//div[@class='col-xs-6 col-passenger']//ul/li[3]//div[@class='col-xs-6 passenger-count right']//button[@class='button-count js-btn-minus']"
    PREMIUM_EKONOMI_CABIN_FIELD = "//label[normalize-space()='Premium Ekonomi']"
    BISNIS_CABIN_FIELD = "//label[normalize-space()='Bisnis']"
    FIRST_CABIN_FIELD = "//label[normalize-space()='First']"
    EKONOMI_CABIN_FIELD = "//label[normalize-space()='Ekonomi']"
    SELESAI_BUTTON_LOCATION = "//button[normalize-space()='SELESAI']"
    FLIGHT_SEARCH_BUTTON_LOCATION = "//button[normalize-space()='CARI PENERBANGAN']"
    
    def getPulangPergiField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PULANG_PERGI_FIELD)
    
    def getSekaliJalanField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEKALI_JALAN_FIELD)
    
    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)
    
    def getAllDepartFrom(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH, self.ALL_DEPART_FROM)
    
    def getGoingToFiled(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)
    
    def getAllGoingTo(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH,self.ALL_GOING_TO)
    
    def getAllDate(self):
       return self.wait_for_presence_of_all_elements_located(By.XPATH, self.ALL_DATES)
   
    def getAddAdultPassengerButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADD_ADULT_PASSENGER_BUTTON)
    
    def getSubstractAdultPassengerButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SUBSTRACT_ADULT_PASSENGER_BUTTON)
    
    def getAddChildPassengerButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADD_CHILD_PASSENGER_BUTTON)
    
    def getSubstractChildPassengerButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SUBSTRACT_CHILD_PASSENGER_BUTTON)
    
    def getAddBabyPassengerButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADD_CHILD_PASSENGER_BUTTON)
    
    def getSubstractBabyPassengerButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SUBSTRACT_CHILD_PASSENGER_BUTTON)
    
    def getPremiumEkonomiCabinField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PREMIUM_EKONOMI_CABIN_FIELD)
    
    def getBisnisCabinField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BISNIS_CABIN_FIELD)
    
    def getFirstCabinField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FIRST_CABIN_FIELD)
    
    def getEkonomiCabinField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EKONOMI_CABIN_FIELD)
    
    def getSelesaiButton(self):
        return self.driver.find_element(By.XPATH, self.SELESAI_BUTTON_LOCATION)
    
    def getSearchFlightButton(self):
        return self.driver.find_element(By.XPATH, self.FLIGHT_SEARCH_BUTTON_LOCATION)
    
    def clickPulangPergiButton(self):
        self.getPulangPergiField().click()

    def clickSekaliJalanButton(self):
        self.getSekaliJalanField().click()

    def enterDepartFromLocation(self, departure_from):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departure_from)
        all_depart_from =  self.getAllDepartFrom()
        for result in all_depart_from:
            if departure_from in result.text:
                result.click()
                break

    def enterGoingToLocation(self, destination_to):
        self.getGoingToFiled().click()
        self.getGoingToFiled().send_keys(destination_to)
        all_going_to = self.getAllGoingTo()
        for result in all_going_to:
            if destination_to in result.text:
                result.click()
                break

    def enterDepartureDate(self, depart_date):
       all_date = self.getAllDate()
       for date in all_date:
           if date.get_attribute("aria-label") == depart_date:
               date.click()
               break
 
    def clickAddAdultPassengerButton(self):
        self.getAddAdultPassengerButton().click()
        
    def clickSubstractAdultPassengerButton(self):
        self.getSubstractAdultPassengerButton().click()

    def clickAddChildPassengerButton(self):
        self.getAddChildPassengerButton().click()

    def clickSubstractChildPassengerButton(self):
        self.getSubstractChildPassengerButton().click()

    def clickAddBabyPassengerButton(self):
        self.getAddBabyPassengerButton().click()

    def clickSubstractBabyPassengerButton(self):
        self.getSubstractBabyPassengerButton().click()

    def selectPremiumEkonomiCabin(self):
        self.getPremiumEkonomiCabinField().click()

    def selectBisnisCabin(self):
        self.getBisnisCabinField().click()

    def selectFirstCabin(self):
        self.getFirstCabinField().click()

    def selectEkonomiCabin(self):
        self.getEkonomiCabinField().click()

    def clickSelesaiButton(self):
        self.getSelesaiButton().click()

    def clickSearchFlightButton(self):
        self.getSearchFlightButton().click()
        
    def searchFlights(self, departure_from, destination_to, depart_date):
        self.enterDepartFromLocation(departure_from)
        self.enterGoingToLocation(destination_to)
        self.enterDepartureDate(depart_date)
        