from selenium import webdriver
import time
from dotenv import load_dotenv
from os import getenv


def login_polygon_steam():
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
