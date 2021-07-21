import sys
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()


def get_price(url):
    driver.get(url)
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, 'html.parser')
    elem = soup.select_one('#udemy > div.main-content-wrapper > div.main-content > div.paid-course-landing-page__container > div.top-container.dark-background > div > div > div.course-landing-page__main-content.course-landing-page__purchase-section__main.dark-background-inner-text-container > div > div > div > div > div.generic-purchase-section--buy-box-main--siIXV > div > div:nth-child(2) > div > div > div > span:nth-child(2) > span')
    price = (elem.text)
    return price


URL = sys.argv[1]
print(get_price(URL))
