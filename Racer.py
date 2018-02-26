import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys

path = (os.path.dirname(os.path.realpath(__file__)))
path.replace('\\','/')

executable_path = path+"/chromedriver.exe"

chrome_options = Options()

# To use my default extension
chrome_options.add_argument('--load-extension='+path+'/1.13.4_0')

driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

driver.get('http://play.typeracer.com')
def racer():
	delay = float(input("Enter Delay: "))
	while True:
		try:
			driver.find_element_by_class_name("gameStatusLabel")
			if driver.find_element_by_class_name("gameStatusLabel").text != 'The race is about to start!' and driver.find_element_by_class_name("gameStatusLabel").text != 'Waiting for more people...':
				break
			
			print(driver.find_element_by_class_name("gameStatusLabel").text, flush=True)
			time.sleep(.5)
		except NoSuchElementException:
			print('waiting', flush=True)
			time.sleep(1)	
		
	text = driver.find_element(By.XPATH, '//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table').text

	finalText = text[text.rfind('wpm')+4 : text.find('change display format')]
	print(finalText)

	#focus the input box
	input_box = driver.find_element_by_class_name("txtInput")
	input_box.send_keys('')

	# start typing!
	for word in finalText:
		time.sleep(delay)
		try:
			input_box.send_keys(word)
		except:
			print("done")
	ans = input("Run Racer Again (Y/N): ")
	if(ans == 'y'):
		racer()
	else:
		driver.quit()
racer()

