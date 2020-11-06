import pyautogui, time
from findBalance import findBalance
from Refresh import refresh

def clickbetAmount(clicks=1):
	pyautogui.click(x=1051, y=484, button='left', clicks=clicks)


def clickPlaceBet(clicks=1):
	pyautogui.click(x=1588, y=679, button='left', clicks=clicks)


def clearInput():
	clickPlaceBet(2)
	pyautogui.press('backspace')


finalBase = 2
base = finalBase
while True:
	initial = findBalance()
	clearInput()
	clickPlaceBet()
	for i in str(base):
		pyautogui.press(i)
	click1to7()
	time.sleep(5)
	final = findBalance()
	if final == initial:
		print('fail')
		refresh()
		continue
	elif final > initial:
		print('Won')
		base = finalBase
	elif final < initial:
		base *= 2
		print('Trust the algo:', base)
