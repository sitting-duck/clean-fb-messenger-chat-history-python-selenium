from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import logging

from time import sleep

def main():
	print("henlo")

class Request:
	# logger is simply a version of pythons print() that logs to stderr. You may ignore it. 
	logger = logging.getLogger('django.project.requests')

	# selenium retries variable will help us keep track of the number of times a selenium request failed. 
	# If you are dealing with Facebook and/or TikTok this will be crucial. 
	selenium_retries = 0

	def __init__(self, url):
		self.url = url

	def get_selenium_res(self, class_name):
		try: 
			software_names = [SoftwareName.CHROME.value]
			operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

			# set up for automatically obtaining a random user agent for each selenium call we make
			# A user agent looks like this: 
			# Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36
			# basically this is an identifier for a user
			user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
			user_agent = user_agent_rotator.get_random_user_agent()

			# options for Chrome. We will use this later after we declare a selenium browser instance. 
			chrome_options = Options()

			# makes it so that Chrome won't physically open on your machine, reduces CPU load, but you may want to play with
			# turning this option on and off. It can help your machine stay cool while scraping, but can make you more likely
			# to get flagged as a scraper. SysAdmins can spot a headless request with ease.
			chrome_options.add_argument("--headless")

			# Only way to get chromedriver to open headlessly. If you are using Firefox you may ignore this. 
			chrome_options.add_argument('--no-sandbox')

			# make the window size large so that the HTML DOM returned has a decent amount of stuff in it. All browsers
			# just return as much as needed to allow the user to view the website, so sometimes you need to enlarge the 
			# window or scroll around to get your desired content to be loaded. 
			chrome_options.add_argument('--window-size=1420,1080')
			
			# Apparently only needed on Windows machines. 
			chrome_options.add_argument('disable-gpu')
			chrome_options.add_argument(f'user-agent={user_agent}')

			### How to Use a Proxy ###
			PROXY = "http://gate.smartproxy.com:7000"		

			if not IS_GAE_PRODUCTION_ENV:
				chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

			prox = Proxy()
			prox.proxy_type = ProxyType.MANUAL
			prox.autodetect = False

if __name__ == "__main__":
	main()