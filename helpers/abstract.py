# -*- coding: utf-8 -*-
from functions.print import *


class Producible:
	lifespan			= 0		# in years
	expense				= 0		# (Produktionskosten)
	energy_construction	= 0		# in kWh (int or object of ints)

	components			= []	# List of classes (must be of type Producible)
	used_resources		= {}	# Dict of resources in g, key: named by class of type Resource (excluding components)

	def get_expense(self):
		"""
		Kosten der Herstellung (addiert die Kosten der Komponenten zu den spezifischen Kosten)
		"""
		expense = self.expense
		for component in self.components:
			expense += component.get_expense(component)
		return expense

	def get_used_resources(self):
		"""
		Liste der insgesamt verbauchen Rohstoffe in Gramm
		"""
		resources = {}

		for component in self.components:
			used_resources = component.get_used_resources(component)
			for key, value in used_resources.items():
				if not key in resources:
					resources[key] = 0
				resources[key] += value
		
		for key, value in self.used_resources.items():
			if not key in resources:
				resources[key] = 0
			resources[key] += value

		return resources

	def get_energy_construction(self):
		"""
		Kumulierter Energieaufwand für die Erstellung
		"""
		energy_construction = self.energy_construction
		for component in self.components:
			energy_construction += component.get_energy_construction()
		return energy_construction

	# ------------- Prints -------------

	def print_expense(self):
		return print_money(self.get_expense())
	
	def print_energy_construction(self):
		return print_watt(
			self.get_energy_construction()
		)