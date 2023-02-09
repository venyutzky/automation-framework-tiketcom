from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
import pytest
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
from automation_framework_tiketcom.pages.HomePage import HomePage
from automation_framework_tiketcom.pages.SearchFlightPage import SearchFlightPage
from automation_framework_tiketcom.pages.FlightSearchResultPage import FlightSearchResultPage


@pytest.mark.usefixtures("setup")
class TestSearchFlight():
    
    def test_search_flight(self):
        
        # setup
        
        # click plane icon
        in_homepage = HomePage(self.driver, self.wait)
        in_homepage.click_plane_icon()
        
        # choose flight type
        in_searchflightpage = SearchFlightPage(self.driver, self.wait)
        in_searchflightpage.select_flight_type()

        # select going from location
        in_searchflightpage.select_depart_from("Jakarta")

        # select going to location
        in_searchflightpage.select_going_to("Padang")
        
        # select date
        in_searchflightpage.select_depart_date("Choose Sabtu, 11 Februari 2023 as your check-in date. It’s available.")
        
        # Provide passenger number
        in_searchflightpage.select_number_of_passenger()
        
        # Provide cabin type
        in_searchflightpage.select_cabin_type()

        # click on SELESAI button
        in_searchflightpage.click_selesai_button()
        
        # click on flight search button
        in_searchflightpage.click_search_flight_button()
        
        # click on pop up card
        in_flightsearchresult_page = FlightSearchResultPage(self.driver, self.wait)
        in_flightsearchresult_page.click_popup()
        
        # scroll down page
        in_flightsearchresult_page.page_scroll()
        
        in_flightsearchresult_page.filter_flight()
        
        all_airplanes = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='section-box-content']/div/div[@class='wrapper-flight-list']/div[@class='row relative']/div[@class='col-xs-6 relative']/div[@class='row']/span[@class='text-marketing-airline']")))
        for airplane in all_airplanes:
            print("The Airplane is : " + airplane.text)
            assert airplane.text == "Batik Air"
            print("assert pass")
        
        

        