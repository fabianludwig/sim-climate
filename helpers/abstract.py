# -*- coding: utf-8 -*-
from functions.print import *
from classes.resources import *


class Producible:
	name 				= ''
	manufacturer		= ''
	
	lifespan			= 0		# in years
	expense				= 0		# (Produktionskosten exkl. Komponenten)
	energy_construction	= 0		# in kWh (int or object of ints)

	components			= []	# List of classes (must be of type Producible)
	used_resources		= {}	# Dict of resources in g, key: named by class of type Resource (excluding components)

	def __init__(self, *args, **kwargs):
		self.__dict__.update(kwargs)
		self.set_components()

	def set_components(self):
		pass

	def set_used_resources(self):
		pass

	def get_lifespan(self):
		return self.lifespan

	def get_expense(self):
		"""
		Kosten der Herstellung (addiert die Kosten der Komponenten zu den spezifischen Kosten)
		"""
		expense = self.expense
		for component in self.components:
			expense += component.get_expense(component)
		return expense
	
	def get_expense_operation(self):
		"""
		Jährliche Wartungskosten
		"""
		return 0

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
	
	def get_energy_operation(self):
		"""
		Jährlicher Energieaufwand für die Wartung
		"""
		return 0

	# ------------- Prints -------------

	def print_expense(self):
		return print_money(self.get_expense())
	
	def print_expense_operation(self):
		return print_money(self.get_expense_operation())
	
	def print_energy_construction(self):
		return print_watt(
			self.get_energy_construction()
		)