import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)


def test_chromium():
    music = "https://www.youtube.com/watch?v=TbvWnJh9e-g&t=902s&ab_channel=RealScience"

    driver.get('https://automatetheboringstuff.com')
    # driver.get(music)
    time.sleep(17)
    driver.quit()