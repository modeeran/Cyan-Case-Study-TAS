from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options as Options

#driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(driver_version="2.26",chrome_type=ChromeType.CHROMIUM).install()))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.python.org")
driver.close()