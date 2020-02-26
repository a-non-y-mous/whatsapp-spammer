from selenium import webdriver
import requests
from random import randint
from time import sleep
browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com')
sleep(20)
text_box = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1ccjW _39ZZK app-wrapper-web font-fix']/div[@class='app _1Jzz1 two']/div[@class='_10V4p _1jxtm']/div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej _14Mgc copyable-area']/div[@class='_13mgZ']/div[@class='_3FeAD _1PRhq']/div[@class='_3u328 copyable-text selectable-text']")
while True:
	try:
		for cnt in range(1000):
			text_box.send_keys("_yare yare daze_")
			sendButton = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1ccjW _39ZZK app-wrapper-web font-fix']/div[@class='app _1Jzz1 two']/div[@class='_10V4p _1jxtm']/div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej _14Mgc copyable-area']/div[@class='hnQHL']/button[@class='_3M-N-']")
			webdriver.common.action_chains.ActionChains(browser).move_to_element_with_offset(sendButton, 0, 6).click().perform()
			cnt=cnt+1
		raise SystemExit
	except Exception as e:
			print(e)
			pass
	sleep(0.2) 