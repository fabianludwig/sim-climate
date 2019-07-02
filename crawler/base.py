# -*- coding: utf-8 -*-

import os, csv, sys
from selenium import webdriver

from crawler.helpers import *



headless_browser = True

class ModelCrawler():
	base_url	   	= 'https://www.wind-turbine-models.com/turbines?manufacturer=&view=table'
	link_selector   = 'table tbody tr td a'
	download_folder = './data'
	filename		= 'models'

	_errors			= []

	def __init__(self):
		self.set_browser()

	def set_browser(self):
		options = webdriver.ChromeOptions()
		if headless_browser:
			options.add_argument('headless')
		self.browser = webdriver.Chrome(options=options)
		self.browser.set_page_load_timeout(45)
		
	def crawl_items(self):
		crawled_urls = self._get_crawled_urls()

		# Delete old file
		if os.path.isfile(self.download_folder+'/'+self.filename+'.csv') and len(crawled_urls) == 0:
			os.remove(self.download_folder+'/'+self.filename+'.csv')

		self.browser.get(self.base_url)
		items = self.browser.find_elements_by_css_selector(self.link_selector)
		item_urls = []

		for item in items:
			item_urls.append(item.get_attribute('href'))
		
		print("{} items to scrape! ({} already done!)".format(len(item_urls), len(crawled_urls)))

		counter = 0
		for item_url in item_urls:
			counter += 1
			if not item_url in crawled_urls:
				self.browser.get(item_url)
				try:
					item = self._scrape_item()

					with open(self.download_folder+'/'+self.filename+'.csv', 'a') as file:
						writer = csv.writer(file)
						writer.writerow(item.values())
					
					with open(self.download_folder+'/.'+self.filename+'_temp.csv', 'a') as file:
						writer = csv.writer(file)
						writer.writerow([item_url])
					
					print("({}/{}) {}".format(counter, len(item_urls), item))
				except:
					self._errors.append(item_url)
					print("{} resulted in an error!".format(item_url), sys.exc_info()[1])
		
		self.clean_up()
	
	def _get_crawled_urls(self):
		if os.path.isfile(self.download_folder+'/.'+self.filename+'_temp.csv'):
			with open(self.download_folder+'/.'+self.filename+'_temp.csv', 'r') as file:
				reader = csv.reader(file)
				your_list = list(reader)
				return [url[0] for url in your_list]
		else:
			return []

	def clean_up(self):
		if len(self._errors) == 0:
			if os.path.isfile(self.download_folder+'/.'+self.filename+'_temp.csv'):
				os.remove(self.download_folder+'/.'+self.filename+'_temp.csv')
		
	def _scrape_item(self):
		return {}