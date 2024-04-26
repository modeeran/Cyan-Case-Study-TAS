from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    login_link_text = "Form Authentication"
    username_element_id = "username"
    password_element_id = "password"
    login_button_element = "#login button.radius"
    login_success_message_element = "#flash-messages .success"
    login_warning_message_element = "#flash-messages .error"

    def navigate_login_page(self):
        element = self.driver.find_element(By.LINK_TEXT, self.login_link_text)
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

    def check_success_message(self,expected_success_msg_text):
        element = self.driver.find_element(By.CSS_SELECTOR, self.login_success_message_element)
        assert element, "The success message element could not be found."
        return self.driver.page_source.__contains__(expected_success_msg_text)

    def check_warning_message(self,expected_warning_text):
        element = self.driver.find_element(By.CSS_SELECTOR, self.login_warning_message_element)
        assert element, "The warning message element could not be found."
        return self.driver.page_source.__contains__(expected_warning_text)
