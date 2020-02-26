from selenium import webdriver
import requests
from time import sleep
browser = webdriver.Chrome()   #opens an automated test Chrome window, your chrome driver MUST ABSOLUTELY match the chrome version (type "chrome://version" in search bar of chrome without the quotes to see your version and download the reqd. chromedriver
browser.get('https://web.whatsapp.com')#yes
sleep(20) #buys you enough time to set up whatsapp web on the automated window
text_box = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1ccjW _39ZZK app-wrapper-web font-fix']/div[@class='app _1Jzz1 two']/div[@class='_10V4p _1jxtm']/div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej _14Mgc copyable-area']/div[@class='_13mgZ']/div[@class='_3FeAD _1PRhq']/div[@class='_3u328 copyable-text selectable-text']")#gets the text area
while True:
	try:
		for cnt in range(1000): #the no of messages goes here
			text_box.send_keys("_yare yare daze_") #type your message to be spammed
			sendButton = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1ccjW _39ZZK app-wrapper-web font-fix']/div[@class='app _1Jzz1 two']/div[@class='_10V4p _1jxtm']/div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej _14Mgc copyable-area']/div[@class='hnQHL']/button[@class='_3M-N-']") #gets the send button
			webdriver.common.action_chains.ActionChains(browser).move_to_element_with_offset(sendButton, 0, 6).click().perform() #actually clicks the send button
			cnt=cnt+1 #yes
		raise SystemExit #exits the script safely, if you want to use sys.exit() then import sys
	except Exception as e:
			print(e)
			pass
	sleep(0.2) #i just wanted the script to run at moderate speed, remove this to increase the speed
	
	#xpath is actually the directory type url to get any element on the webpage - you can derive it by going to developers tools and observing the element's hierarchy
