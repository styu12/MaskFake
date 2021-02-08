from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import urllib.request

# keyword = '남친룩'
# url = 'https://www.instagram.com/explore/tags/{}'.format(keyword)
url = 'https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl'
# nurl = input('검색할 태그를 입력해주세요: ')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--start-fullscreen')
driver = webdriver.Chrome('chromedriver', options=options)


driver.get(url)

time.sleep(3)
searchbox = driver.find_element_by_css_selector("input.gLFyf.gsfi")
searchbox.send_keys('홍현희 마스크')
time.sleep(2)
driver.find_element_by_css_selector(".Tg7LZd").click()
time.sleep(2)

# time.sleep(1)
# driver.find_element_by_css_selector("img.list_smallimg_coordi").click()
# elem = driver.find_element_by_css_selector("#email")
# elem.send_keys("01074182293")
# pw = driver.find_element_by_css_selector("#pass")
# pw.send_keys("akdrhahd5*")
# driver.find_element_by_css_selector("#loginbutton").click()
# time.sleep(6)
# driver.find_element_by_css_selector(".aOOlW.HoLwm").click()
# time.sleep(1)
# search = driver.find_element_by_css_selector(".XTCLo.x3qfX") 
# search.send_keys("워크웨어룩")
# time.sleep(2)
# driver.find_element_by_css_selector(".yCE8d").click()    

SCROLL_PAUSE_TIME = 1
# last_height = driver.execute_script("return document.body.scrollHeight")

# num = 1
# while num < 3:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)
    # new_height = driver.execute_script("return document.body.scrollHeight")
    # num = num + 1
    # if new_height == last_height:
    #     try:
    #         driver.find_element_by_css_selector(".mye4qd").click()
    #     except:
    #         break
    # last_height = new_height


images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
count = 1
for image in images: 
    try:
        imgUrl = image.get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count + 1
    except:
        pass

# html = driver.page_source
# soup = BeautifulSoup(features="html.parser")

# insta = soup.select('.FFVAD')

# print(insta)
driver.close()
