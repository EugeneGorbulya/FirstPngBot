from bs4 import BeautifulSoup
from selenium import webdriver
import pandas
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
from urllib.request import urlretrieve

count = 1
def save_images(url):
    global count
    browser.get(url)
    time.sleep(2)
    list = browser.find_elements(By.CLASS_NAME, "_3wkl4")
    i = 1
    c = count
    print(len(list))
    if len(list) > 5:
        for e in list[1::]:
            if c <= 125:
                if i == 1:
                    os.mkdir(f'{count}')
                    print(f"сохранил {count} фото")
                    count += 1
                if i <= 5:
                    src = e.get_attribute('src')
                    #/Users/engorgen/Documents/Dev/ScriptMarket
                    urlretrieve(src, f'/Users/engorgen/Documents/Dev/ScriptMarket/{c}/{i}.png')
                i += 1


options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
j = 1
while count <= 125:
    browser.get(f"https://market.yandex.ru/catalog--nizhnee-bele-dlia-muzhchin/26962870/list?hid=7877999&rs=eJwtUD1Iw1AYTKpoTBEy1hThIQgdRFrjoq0QOwk6FBFclCTEFAotim0nEQIFEaQurg519gcdXKxiHURwcFAQBMEMFQdBHNTBydzhchx3-e7uZaTekZOvZamVnwhRmkuHaL9mQvTbTej348BtKI1PuOYhdLEOLq6gm5tAO34eYpCDG7xBaR2DN87ApSG40g5vH8Eb00Axi15zgPk1ujfkp0AxM4arX_IT5nyhN1i7ZD5cP8X2RW7eZ_IUM3-gBAq4XQOKDF0Z3B9m1xZfscG130x44IuO4Eq75Hf4A-YBNzxReeZVm72C2H-B5Cy_ibA9yrQ9bta55IXtPvkkuPmBFruQvpUVw3C9ZHLUzZbUuKoosiZig0LVuvSeJS_vVIsVyxBSQlL7aMqxXtGpRfTuf5NWilY0JgtZ0_S465SrTtFyndXlatkrWoZVqHilslVZXhHN9_lE3V_QIn_hCaKa&page={j}")
    list = browser.find_elements(By.XPATH, "//a[@href]")
    print(len(list))
    prod = []
    for e in list:
        if "product" in e.get_attribute("href"):
            prod.append(e.get_attribute("href"))
    for i in range(0, len(prod), 2):
        save_images(prod[i])
        if count == 126:
            break
    j += 1
    print(f"{j} страница------------------")

#_3uXo3
#_3wkl4
#/marketfrontSerpLayout/serpLayoutItem_17122202741010682906616029_74069e84
#cia-cs _3VnG9
