from selenium import webdriver
import booking.constants as const
from booking.constants import BASE_URL
from selenium.webdriver.common.keys import Keys


class Booking(webdriver.Chrome):
    def __init__(self, driver_path="C:/Users/p.kontos/Downloads/chromedriver.exe", teardown=False):
        self.driver = webdriver.Chrome(driver_path)

    def land_first_page(self):
        self.driver.get(const.BASE_URL)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('onetrust-accept-btn-handler').click()

    def __exit__(self, *args):
        if self.teardown:
            self.driver.quit()