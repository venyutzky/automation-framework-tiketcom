import time


class BaseDriver():
    
    def __init__(self, driver):
        self.driver = driver
        
    def page_scroll(self, speed=8):
        current_scroll_position, new_height= 0, 1
        while current_scroll_position <= new_height:
            current_scroll_position += speed
            self.driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = self.driver.execute_script("return document.body.scrollHeight")
                           
        time.sleep(4)