from selenium import webdriver
import time
from optionsRoulette import Roulette
from dotenv import load_dotenv
from os import getenv

PATH = '/home/varad/Scripts/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get("https://www.csgopolygon.com")
signin = driver.find_element_by_class_name("window_steam_button")
signin.click()
time.sleep(2)
load_dotenv()
STEAM_USER = getenv("STEAM_USERNAME")
STEAM_PASS = getenv("STEAM_PASSWORD")
driver.find_element_by_id("steamAccountName").send_keys(STEAM_USER)
driver.find_element_by_id("steamPassword").send_keys(STEAM_PASS)
driver.find_element_by_id("imageLogin").click()
n = int(input())
if n == 1:
	game = Roulette(driver)
	print(game.findBalance())
	game.betAmount(10)
	time.sleep(1)
	print(game.bettedAmount())
else:
	quit()
