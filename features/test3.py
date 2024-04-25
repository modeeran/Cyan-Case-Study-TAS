from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService


def before_scenario(context, driver):
    tag_list = context.tags
    if 'login2' in tag_list or 'status' in tag_list:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")  # This is important for some versions of Chrome
        chrome_options.add_argument("--remote-debugging-port=9222")  # This is recommended

        # Set path to Chrome binary
        chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"

        # Set path to ChromeDriver
        chrome_service = ChromeService(executable_path="/opt/chromedriver/chromedriver-linux64/chromedriver")

        # Set up driver
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


def after_scenario(context, driver):
    tag_list = context.tags
    if 'login2' in tag_list or 'status' in tag_list:
        context.driver.quit()

