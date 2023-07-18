import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Page:
    def __init__(self, url="https://www.google.com/", browser="chrome"):
        self.url = url

        match browser:
            case "chrome":
                self.driver = webdriver.Chrome()
            case "chromium":
                chromium = Service('/usr/bin/chromedriver')
                self.driver = webdriver.Chrome(service=chromium)


    def open(self, sleep=180):
        self.driver.get(self.url)
        time.sleep(sleep)
        self.driver.quit()
