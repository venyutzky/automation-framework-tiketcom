from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from automation_framework_tiketcom.base.base_driver import BaseDriver

class FlightSearchResultPage(BaseDriver):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    # Locator
    POPUP_BUTTON_LOCATION = "//div[@class='comp-info-box']//div[@class='v3-btn v3-btn__blue list-horizontal__middle btn-action']"
    ALL_AIRPLANE_AIRLINES_FIELD = "//div[@class='section-box-content']/div/div[@class='wrapper-flight-list']/div[@class='row relative']/div[@class='col-xs-6 relative']/div[@class='row']/span[@class='text-marketing-airline']"
    FILTER_LANGSUNG_FIELD = "//label[normalize-space()='Langsung']"
    FILTER_1_TRANSIT_FIELD = "//label[normalize-space()='1 Transit']"
    FILTER_2_TRANSIT_FIELD = "//label[normalize-space()='2+ Transit']"
    
    # def click_popup(self):
    #     self.driver.find_element(By.XPATH, "//div[@class='comp-info-box']//div[@class='v3-btn v3-btn__blue list-horizontal__middle btn-action']").click()
    #     time.sleep(1)
        
    def getPopUpButtonLocation(self):
        return self.driver.find_element(By.XPATH, self.POPUP_BUTTON_LOCATION)
    
    def getAllAirplaneAirlinesField(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH, self.ALL_AIRPLANE_AIRLINES_FIELD)
    
    def getFilterLangsungField(self):
        return self.driver.find_element(By.XPATH, self.FILTER_LANGSUNG_FIELD)
    
    def getOneTransitField(self):
        return self.driver.find_element(By.XPATH, self.FILTER_1_TRANSIT_FIELD)
    
    def getTwoTransitField(self):
        return self.driver.find_element(By.XPATH, self.FILTER_2_TRANSIT_FIELD)
    
    def clickPopUpButton(self):
        self.getPopUpButtonLocation().click()
    
    def filterAirplaneAirlines(self):
        time.sleep(3)
        all_airplane_airlines = self.getAllAirplaneAirlinesField()
        print(len(all_airplane_airlines))
        
    def filterFlightTransit(self, filter_transit):
        if filter_transit == "Langsung":
            self.getFilterLangsungField().click()
            print("Selected flights without transit")
        elif filter_transit == "1 Transit":
            self.getOneTransitField().click()
            print("Selected flights with 1 transit")
        elif filter_transit == "2+ transit":
            self.getTwoTransitField().click()
            print("Selected flights with 2 or more transit")
