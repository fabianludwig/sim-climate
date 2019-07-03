
# -*- coding: utf-8 -*-

from functions.print import *
from .._base_ import Producible


class Vehicle(Producible):
	km_per_year			= 10000
	
	def get_energy_operation(self):
		"""
		Zu bedenken: Ersatzteile, Ölwechsel
		"""
		return 0
	
	def get_emission_per_km(self):
		return 100

	def get_kwh_per_km(self):
		return 0

	def get_yearly_emissions(self):
		return self.get_emission_per_km()*self.km_per_year

	# ------------- Prints -------------

	def print_emission_per_km(self):
		return print_weight(
			self.get_emission_per_km()
		)
	
	def print_kwh_per_km(self):
		return print_watt(
			self.get_kwh_per_km()
		)

	def print_yearly_emissions(self):
		return print_weight(
			self.get_yearly_emissions()
		)
