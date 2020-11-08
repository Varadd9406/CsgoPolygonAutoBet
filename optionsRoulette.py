from selenium.webdriver.common.action_chains import ActionChains


class Roulette:
	def __init__(self, driver):
		self.driver = driver
		self.actions = ActionChains(self.driver)

	def findBalance(self):  # DONE
		return int(self.driver.find_element_by_id("balance_p").text)

	def placeBet(self, value):
		self.driver.find_element_by_class_name("bet_clean_button").click()
		self.driver.find_element_by_id("roulette_amount").send_keys(str(value))
		self.driver.find_element_by_class_name("red_button").click()

	def bettedAmount(self):
		return int(self.driver.find_element_by_class_name("mytotal").text)
