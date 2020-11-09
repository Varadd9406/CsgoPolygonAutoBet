from selenium import webdriver
import time
from optionsRoulette import Roulette
from dotenv import load_dotenv
from os import getenv

load_dotenv()
STEAM_USER = getenv("STEAM_USERNAME")
STEAM_PASS = getenv("STEAM_PASSWORD")
PATH = getenv("WEBKIT_PATH")
driver = webdriver.Chrome(PATH)
driver.get("https://www.csgopolygon.com")
signin = driver.find_element_by_class_name("window_steam_button")
signin.click()
time.sleep(3)
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
cnt = 0
while True:
	if cnt >= 5:
		driver.refresh()
		cnt = 0
	initial = game.findBalance()
	game.placeBet(base)
	time.sleep(1)
	if game.bettedAmount() == 0:
		time.sleep(8)
		cnt += 1
		continue
	time.sleep(34)
	final = game.findBalance()
	if final > initial:
		cnt = 0
		print('Won')
		base = finalBase
	elif final < initial:
		cnt = 0
		base *= 2
		print('Trust the algo:', base)
	
