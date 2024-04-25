from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service('/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def before_scenario(context,driver):
    tag_list = context.tags
    if 'login2' in tag_list or 'status' in tag_list:
        context.driver = webdriver.Chrome(service=service, options=options)
        #context.driver = webdriver.Chrome()
        context.driver.maximize_window()
        context.driver.get("https://the-internet.herokuapp.com/")


def after_scenario(context,driver):
    tag_list = context.tags
    if 'login2' in tag_list or 'status' in tag_list:
        context.driver.quit()


