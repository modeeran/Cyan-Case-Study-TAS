from selenium.webdriver.common.by import By
import requests


class StatusPage:

    def __init__(self,driver):
        self.driver = driver

    status_option_link_text = "Status Codes"

    def navigate_status_code_page(self):
        element = self.driver.find_element(By.LINK_TEXT, self.status_option_link_text)
        element.click()

    def select_status_code_link(self, link):
        element = self.driver.find_element(By.LINK_TEXT, link)
        element.click()

    def collect_http_status_code(self, statuscode):
        response = requests.get(self.driver.current_url)
        return response.status_code.__eq__(statuscode)
