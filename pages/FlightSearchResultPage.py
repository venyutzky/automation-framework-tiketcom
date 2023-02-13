from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from automation_framework_tiketcom.base.base_driver import BaseDriver

class FlightSearchResultPage(BaseDriver):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def click_popup(self):
        self.driver.find_element(By.XPATH, "//div[@class='comp-info-box']//div[@class='v3-btn v3-btn__blue list-horizontal__middle btn-action']").click()
        time.sleep(1)
        
    def filter_flight(self):
        time.sleep(1)
        all_airplanes = self.wait_for_presence_of_all_elements_located(By.XPATH, "//div[@class='section-box-content']/div/div[@class='wrapper-flight-list']/div[@class='row relative']/div[@class='col-xs-6 relative']/div[@class='row']/span[@class='text-marketing-airline']")
        print(len(all_airplanes))
        time.sleep(1)