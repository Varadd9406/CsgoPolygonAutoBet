import pytesseract, time, pyautogui, cv2
from findNumberFromString import findNumberFromString
import requests as rq
import base64
import json


def visionApi(image):
	API_KEY = "AIzaSyBG0Y7znwmqN22Gpxn96vfdUIS9xut_ddU"
	url = f"https://vision.googleapis.com/v1/images:annotate?key={API_KEY}"
	data = {
		'requests': [
			{
				"image": {
					"content": image
				},
				"features": [
					{
						"type": "DOCUMENT_TEXT_DETECTION"
					}
				]
			}

		]
	}
	s = json.dumps(data)
	postreq = rq.post(url, data=s, headers={'Content-Type': 'application/json'})
	output = json.loads(postreq.content)
	num = output["responses"][0]["textAnnotations"][0]["description"]
	num = (findNumberFromString(num))
	print(num)
	return num


def set50inFull():
	time.sleep(4)
	pyautogui.click(x=1419, y=503, button='left')


def findBalance():
	img = pyautogui.screenshot('photo.png', region=(1703, 170, 1763 - 1703, 235 - 170))
	with open('photo.png', 'rb') as image_file:
		my_string = base64.b64encode(image_file.read())
		my_string = str(my_string)
		my_string = my_string[2:]
		my_string = my_string[:len(my_string) - 1]
		visionApi(my_string)


findBalance()
