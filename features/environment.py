from selenium import webdriver

def before_scenario(context,driver):
    tag_list = context.tags
    if 'login' in tag_list or 'status' in tag_list:
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
        context.driver.get("https://the-internet.herokuapp.com/")


def after_scenario(context,driver):
    tag_list = context.tags
    if 'login' in tag_list or 'status' in tag_list:
        context.driver.quit()
