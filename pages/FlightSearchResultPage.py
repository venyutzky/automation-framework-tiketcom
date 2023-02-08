from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from automation_framework_tiketcom.base.base_driver import BaseDriver

class FlightSearchResultPage(BaseDriver):
    
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait
    
    def click_popup(self):
        self.driver.find_element(By.XPATH, "//div[@class='comp-info-box']//div[@class='v3-btn v3-btn__blue list-horizontal__middle btn-action']").click()
        time.sleep(1)