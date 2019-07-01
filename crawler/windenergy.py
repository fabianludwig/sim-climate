# -*- coding: utf-8 -*-

from crawler.helpers import *
from crawler.base import ModelCrawler


class WindenergyCrawler(ModelCrawler):
	base_url	   	= 'https://www.wind-turbine-models.com/turbines?manufacturer=&view=table'
	download_folder = './data/windenergy'	
	link_selector   = 'table tbody tr td a'
			
	def _scrape_item(self):
		manufacturer			= self.browser.find_element_by_css_selector('.breadcrumb-bs ol li:nth-child(3) a span').text.rstrip()
		name					= self.browser.find_element_by_css_selector('h1[class="page-header"]').text.rstrip()
		nominal_power		   	= self.browser.find_element_by_css_selector('div[data-tabname="leistung"] table tbody tr:nth-child(1) .rechteSeite').text
		einschaltgeschwindigkeit= self.browser.find_element_by_css_selector('div[data-tabname="leistung"] table tbody tr:nth-child(3) .rechteSeite').text
		nennwindgeschwindigkeit	= self.browser.find_element_by_css_selector('div[data-tabname="leistung"] table tbody tr:nth-child(4) .rechteSeite').text
		abschaltgeschwindigkeit	= self.browser.find_element_by_css_selector('div[data-tabname="leistung"] table tbody tr:nth-child(5) .rechteSeite').text
		nabenhoehe				= self.browser.find_element_by_css_selector('div[data-tabname="turm"] table tbody tr:nth-child(1) .rechteSeite').text
		rotordurchmesser		= self.browser.find_element_by_css_selector('div[data-tabname="rotor"] table tbody tr:nth-child(1) .rechteSeite').text
		rotorflaeche			= self.browser.find_element_by_css_selector('div[data-tabname="rotor"] table tbody tr:nth-child(2) .rechteSeite').text
		blattzahl			   	= self.browser.find_element_by_css_selector('div[data-tabname="rotor"] table tbody tr:nth-child(3) .rechteSeite').text
		
		return ({
			'manufacturer': manufacturer,
			'name': name,
			'classname': save_classname(name), 
			'nominal_power': clean_number(nominal_power), 
			'einschaltgeschwindigkeit': clean_number(einschaltgeschwindigkeit),
			'nennwindgeschwindigkeit': clean_number(nennwindgeschwindigkeit),
			'abschaltgeschwindigkeit': clean_number(abschaltgeschwindigkeit), 
			'nabenhoehe': clean_number_and_get_avg(nabenhoehe), 
			'rotordurchmesser': clean_number(rotordurchmesser), 
			'rotorflaeche': clean_number(rotorflaeche), 
			'blattzahl': clean_number(blattzahl),
		})