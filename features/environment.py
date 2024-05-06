from selenium import webdriver
import os

def before_scenario(context,driver):
    tag_list = context.tags
    if 'login' in tag_list or 'status' in tag_list:

        executor = os.getenv("SELENIUM_EXECUTOR", "")

        if executor == "hub":
            options = webdriver.ChromeOptions()
            context.driver = webdriver.Remote(command_executor="http://localhost:4444", options=options)

        elif executor == "" or executor == "local":
            context.driver = webdriver.Chrome()

        context.driver.maximize_window()
        context.driver.get("https://the-internet.herokuapp.com/")


def after_scenario(context,driver):
    tag_list = context.tags
    if 'login' in tag_list or 'status' in tag_list:
        context.driver.quit()
