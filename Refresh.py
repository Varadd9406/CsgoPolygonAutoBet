import pyautogui, time


def refresh():
	pyautogui.click(x=1202, y=33, button='left')
	pyautogui.click(x=1197, y=73, button='left')
	address = 'https://csgopolygon.com/'
	for i in address:
		pyautogui.press(i)
	time.sleep(10)
	pyautogui.press('enter')
	pyautogui.click(x=1169, y=33, button='left')
	pyautogui.click(x=1862, y=365, button='left')
	time.sleep(10)
