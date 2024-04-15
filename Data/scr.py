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

count = 251
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
            if c <= 375:
                if i == 1:
                    os.makedirs(f'/Users/engorgen/Documents/Dev/FirstPngBotP/Data/{count}')
                    print(f"сохранил {count} фото")
                    count += 1
                if i <= 5:
                    src = e.get_attribute('src')
                    #/Users/engorgen/Documents/Dev/ScriptMarket

                    urlretrieve(src, f'/Users/engorgen/Documents/Dev/FirstPngBotP/Data/{c}/{i}.png')
                i += 1


options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
j = 1
while count <= 375:
    browser.get(f"https://market.yandex.ru/catalog--aksessuary-dlia-muzhchin/55679/list?hid=7812166&rs=eJxNkD1LA0EYhHfNIedB4EAQiYVbWFiIeldE1FWWgIVW_gHJJiRWguJXfYVgZSNWFuGCsbNQxCLx6xqbdIJgu41io7_BmynEZhie953Z9y4-KazLFynS3aVcs43HXN2bzjX5gNphkNTDNPm-h86AJK-L4CvgtgMv-g_QG2br4KoKYsrwYo2-x2kXPa4Lkhyx-Z1ZD5rVFzCdhrfjaHbHIFkFWXcHVXvP8HO8-RY72Rf5OTbNNjuLT-g8AzeFZbRpvnvKm9ljW8jaHRDXBhENen5Fdon99AedIiA3zPq89pr3dHp4dxX_xIzw3UNepXnPFRrsBDc_kUov-Aem6EtI2bbuSz-aLc83a1Fc0cFY4PsyVKNF5YWDpaFGc7N2sLVfjZWYFH9DqeT_YYRhOPALMryWEw%2C%2C&page={j}")
    list = browser.find_elements(By.XPATH, "//a[@href]")
    prod = []
    for e in list:
        if "product" in e.get_attribute("href"):
            prod.append(e.get_attribute("href"))
    for i in range(0, len(prod), 3):
        save_images(prod[i])
        if count == 376:
            break
    j += 1
    print(f"{j} страница------------------")

#_3uXo3
#_3wkl4
#/marketfrontSerpLayout/serpLayoutItem_17122202741010682906616029_74069e84
#cia-cs _3VnG9
