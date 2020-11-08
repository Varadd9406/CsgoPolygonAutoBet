First install selenium from pip

```bash
pip install selenium
```
Then add a webkit for your preffered browser.Here chrome is being used but you can change in the roulette.py.
```python
#For Chrome
driver = webdriver.Chrome(PATH)
```
```python
#For Firefox
driver = webdriver.Firefox(PATH)
```
Add a .env file with your the following info

```.env
STEAM_USERNAME="yourUsername"
STEAM_PASSWORD="yourPassword"
WEBKIT_PATH = "Absoulute/Path/to/webkit"
```

