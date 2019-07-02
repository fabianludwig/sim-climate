# -*- coding: utf-8 -*-

from functions.print import *


class Resource:
	production_kwh_per_g	= 0 # in kWh
	production_co2_per_g	= 0 # in g

	expense					= 0 # in EUR pro g
	dichte				  	= 1000 # in kg pro m3

	def __init__(self, *args, **kwargs):
		self.__dict__.update(kwargs)

	def get_expense(self):
		return self.expense
	
	def get_dichte(self):
		return self.dichte
	
	def get_production_kwh_per_g(self):
		return self.production_kwh_per_g
	
	def get_production_co2_per_g(self):
		return self.production_co2_per_g
	

class Fluid(Resource):
	def get_dichte(self):
		return self.dichte/1000


class Combustible(Resource):
	combustion_co2_per_g	= 0 # in g
	brennwert			   	= 0 # in kWh pro kg

	def get_brennwert(self):
		return self.brennwert
	
	def get_brennwert_per_g(self):
		return self.get_brennwert()/1000
	
	def get_combustion_co2_per_g(self):
		return self.combustion_co2_per_g

	def get_co2_per_kwh(self):
		return (1/self.get_brennwert())*self.get_combustion_co2_per_g()*1000
	
	def print_co2_per_kwh(self):
		return print_weight(
			self.get_co2_per_kwh()
		)