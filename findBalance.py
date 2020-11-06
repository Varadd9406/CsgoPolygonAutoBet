import pytesseract, time, pyautogui, cv2
from findNumberFromString import findNumberFromString
import base64
from visionApiCall import visionApi


def findBalance():
	img = pyautogui.screenshot('photo.png', region=(1011, 536, 1170 - 1011, 564 - 536
													))
	with open('photo.png', 'rb') as image_file:
		my_string = base64.b64encode(image_file.read())
		my_string = str(my_string)
		my_string = my_string[2:]
		my_string = my_string[:len(my_string) - 1]
		return visionApi(my_string)
