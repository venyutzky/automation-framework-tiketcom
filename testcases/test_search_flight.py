import sys
import pytest
import softest
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
from automation_framework_tiketcom.pages.HomePage import HomePage
from automation_framework_tiketcom.utilities.utils import Utils
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchFlightAndVerifyFilter(softest.TestCase):
    
    log = Utils.custom_logger()
    
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.in_homepage = HomePage(self.driver)
        self.ut = Utils()
    
    @data(("Padang", "Jakarta", "Choose Sabtu, 25 Februari 2023 as your check-in date. It’s available.", "Langsung"), ("Jakarta", "Padang", "Choose Sabtu, 25 Februari 2023 as your check-in date. It’s available.", "Langsung"))
    @unpack
    def test_search_flight_without_transit(self, depart_from, going_to, depart_date, transit):
        # click plane icon
        search_flight = self.in_homepage.clickPlaneIcon()
        # choose flight type
        search_flight.clickPulangPergiButton()
        search_flight.clickSekaliJalanButton()
        # Search Flight
        search_flight.searchFlights(depart_from, going_to, depart_date)
        # Provide passenger number
        search_flight.clickAddAdultPassengerButton()
        search_flight.clickSubstractAdultPassengerButton()
        search_flight.clickAddChildPassengerButton()
        search_flight.clickSubstractChildPassengerButton()
        search_flight.clickAddBabyPassengerButton()
        search_flight.clickSubstractBabyPassengerButton()
        # Provide cabin type
        search_flight.selectPremiumEkonomiCabin()
        search_flight.selectBisnisCabin()
        search_flight.selectFirstCabin()
        search_flight.selectEkonomiCabin()
        # click on SELESAI butto
        search_flight.clickSelesaiButton()
        # click on flight search button
        search_flight_result = search_flight.clickSearchFlightButton()
        # click on pop up card
        search_flight_result.clickPopUpButton()
        # Filter the flights
        search_flight_result.filterFlightTransit(transit)
        # scroll down page
        search_flight_result.page_scroll()
        # assert filter flight
        filter_by_transit = search_flight_result.getSearchFlightByTransitResult()
        self.log.info(len(filter_by_transit))
        self.ut.assertListItemText(filter_by_transit, transit)
        
   