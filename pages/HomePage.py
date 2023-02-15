from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from automation_framework_tiketcom.base.base_driver import BaseDriver


class HomePage(BaseDriver):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator
    PLANE_ICON_LOCATION =  "//div[@class='index_header_inner__ZgIbg']/div[@class='index_content__k_CP2 index_desktop_only__ss43k']//div[@class='SearchForm_verticalIcons__7QwNj']//div[@class='VerticalIcons_listIcon__rGlIP']//div[@class='VerticalIcons_wrapper__4jHIR']//ul[@class='VerticalIcons_lastGrid__93rXJ']//li[1]//a[1]"
    
    def getPlaneIconLocation(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PLANE_ICON_LOCATION)
    
    def clickPlaneIcon(self):
        self.getPlaneIconLocation().click()
     
        
    
    
