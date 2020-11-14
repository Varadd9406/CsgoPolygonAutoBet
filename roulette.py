from selenium import webdriver
import time
from optionsRoulette import Roulette
from dotenv import load_dotenv
from os import getenv
from login import login_polygon_steam

driver = login_polygon_steam()
n = int(input())
if n == 1:
	pass
else:
	quit()
game = Roulette(driver)
finalBase = 1
base = finalBase
cnt = 0
while True:
	if cnt >= 5:
		driver.refresh()
		cnt = 0
	if game.reponsive():
		initial = game.findBalance()
	else:
		time.sleep(20)
		driver.refresh()
		continue
	if game.reponsive():
		game.placeBet(base)
	else:
		time.sleep(20)
		driver.refresh()
		continue
	time.sleep(1)
	if game.reponsive():
		if game.bettedAmount() == 0:
			time.sleep(8)
			cnt += 1
			continue
	else:
		time.sleep(20)
		driver.refresh()
		continue
	time.sleep(34)
	while not game.reponsive():
		time.sleep(20)
		driver.refresh()
	final = game.findBalance()
	if final > initial:
		print('Won')
		base = finalBase
		cnt = 0
	elif final < initial:
		base *= 2
		cnt = 0
		print('Trust the algo:', base)
	else:
		cnt += 1
