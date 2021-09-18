import sys
from selenium import webdriver
import os

import asyncio
from pyppeteer import launch


driver = webdriver.Chrome()


def get_price(url):
    asyncio.get_event_loop().run_until_complete(main(url))


async def main(url):
    browser = await launch(ignoreHTTPSErrors=True,
                           headless=True,
                           slowMo=0,
                           args=[
                               "--no-sandbox",
                               "--disable-setuid-sandbox",
                               "--disable-gpu",
                               "--disable-dev-shm-usage",
                               '--proxy-server="direct://"',
                               "--proxy-bypass-list=*"
                           ])
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot({"path": "headful_without_stealth.png", "fullPage": True})
    os.remove("headful_without_stealth.png")
    element = await page.querySelector('#udemy > div.main-content-wrapper > div.main-content > div.paid-course-landing-page__container > div.sidebar-container-position-manager > div > div > div > div.course-landing-page_sidebar-container > div > div:nth-child(1) > div.sidebar-container--purchase-section--17KRp > div > div.generic-purchase-section--buy-box-main--siIXV > div > div:nth-child(2) > div > div > div > span:nth-child(2) > span')
    value = await page.evaluate('(element) => element.textContent', element)
    print((value))
    await browser.close()


URL = sys.argv[1]
(get_price(URL))
