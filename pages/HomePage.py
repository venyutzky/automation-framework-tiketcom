from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver
    
    def click_plane_icon(self):
        plane_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index_header_inner__ZgIbg']/div[@class='index_content__k_CP2 index_desktop_only__ss43k']//div[@class='SearchForm_verticalIcons__7QwNj']//div[@class='VerticalIcons_listIcon__rGlIP']//div[@class='VerticalIcons_wrapper__4jHIR']//ul[@class='VerticalIcons_lastGrid__93rXJ']//li[1]//a[1]")))
        plane_icon.click()
        time.sleep(1)
    
    
