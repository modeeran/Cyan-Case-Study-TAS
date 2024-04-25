from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    login_option_link_text = "Form Authentication"
    username_element_id = "username"
    password_element_id = "password"
    login_button_element = "#login button.radius"

    def navigate_login_page(self):
        element = self.driver.find_element(By.LINK_TEXT, self.login_option_link_text)
        element.click()

    def set_username(self, username):
        element = self.driver.find_element(By.ID, self.username_element_id)
        element.clear()
        element.send_keys(username)
        assert element.get_attribute('value') == username

    def set_password(self, password):
        element = self.driver.find_element(By.ID, self.password_element_id)
        element.clear()
        element.send_keys(password)
        assert element.get_attribute('value') == password

    def click_login_button(self):
            element = self.driver.find_element(By.CSS_SELECTOR, self.login_button_element)
            element.click()

    def display_status_of_warning_message(self,expected_warning_text):
       pass


