import requests as rq
import base64
import json
from findNumberFromString import findNumberFromString


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
	return num
