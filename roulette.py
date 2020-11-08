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
time.sleep(3)
load_dotenv()
STEAM_USER = getenv("STEAM_USERNAME")
STEAM_PASS = getenv("STEAM_PASSWORD")
driver.find_element_by_id("steamAccountName").send_keys(STEAM_USER)
driver.find_element_by_id("steamPassword").send_keys(STEAM_PASS)
driver.find_element_by_id("imageLogin").click()
n = int(input())
if n == 1:
	pass
else:
	quit()
game = Roulette(driver)
finalBase = 3
base = finalBase
while True:
	initial = game.findBalance()
	game.placeBet(base)
	time.sleep(35)
	final = game.findBalance()
	if final == initial:
		continue
	elif final > initial:
		print('Won')
		base = finalBase
	elif final < initial:
		base *= 2
		print('Trust the algo:', base)
