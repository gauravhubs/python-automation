#Python code for playing 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

for i in range(100):
	htmlElem.send_keys(Keys.DOWN)
	htmlElem.send_keys(Keys.LEFT)
	htmlElem.send_keys(Keys.RIGHT)
	htmlElem.send_keys(Keys.LEFT)


browser.quit()

###Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT