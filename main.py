#!/usr/bin/env python3
from selenium import webdriver
import time

cookies = {
	'auth-token' : '',
	'api_token': '',
	'twilight-user': ''
}

def add_cookies(webdriver: webdriver):
	for key in cookies:
		webdriver.add_cookie({'name': key , 'value': cookies[key]})

if __name__ == '__main__':
	BASE_URL = 'https://www.twitch.tv/'

	streamer = input('Streamer: ')
	
	print('<<TWTICH COOKIES>>')

	cookies['auth-token'] = input('auth-token:')
	cookies['api_token'] = input('api_token:')
	cookies['twilight-user'] = input('twilight-user:')

    
	driver = webdriver.Chrome('../chromeDriver/chromedriver')

	try:
		driver.get(BASE_URL + 'dummy404')
		add_cookies(driver)

		driver.get(BASE_URL + streamer)
	except Exception as e:
		driver.close()
		print(e)


	time.sleep(20)
	while True:
		try:
			driver.find_element_by_class_name('fERWGf').click()
		except Exception as e:
			print(e)

		time.sleep(900)
