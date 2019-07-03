# -*- coding: utf-8 -*-
import math

from functions.print import *
from models.resources import *


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

	def print_lifespan(self):
		return print_months(
			self.get_lifespan()*12
		)

	def print_expense(self):
		return print_money(
			self.get_expense()
		)
	
	def print_expense_operation(self):
		return print_money(
			self.get_expense_operation()
		)
	
	def print_energy_construction(self):
		return print_watt(
			self.get_energy_construction()
		)
	
	def print_energy_operation(self):
		return print_watt(
			self.get_energy_operation()
		)


class Locatable:
	latitude		= 51.7037766
	longitude		= 7.3402764

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

	def get_sonnenstand(self, date=False):
		"""
		Einfallswinkel der Mittagssonne
		Wenn kein Datum angegeben wird das Jahresmittel ausgegeben
		"""
		deklination = 0
		if date:
			day_of_year = date.timetuple().tm_yday
			bogenmass 	= 0.4095*math.sin(0.016906*(day_of_year-80.086))
			deklination = bogenmass*57.29578
		return 90-(self.latitude-deklination)

	def get_altitude(self):
		"""
		Höhenkarte?
		TODO: OpenStreetMap sollte Elevation anbieten (s. OpenTopoMap)
		"""
		return 0
	
	def get_windgeschwindigkeit(self, date=False):
		"""
		Durchschnittliche Windgeschwindigkeit in 80m Höhe 
		(https://www.dwd.de/DE/leistungen/_config/leistungsteckbriefPublication.pdf?view=nasPublication&nn=16102&imageFilePath=1984673719052460620550302552147834994911318791076805607326336086634847969459358946555032055462272638945184535799804022754249241658870336218612364515164241169787346171968215343642867407127803970689474140526989975481747650065031520731391283821&download=true)
		Wenn kein Datum angegeben wird das Jahresmittel ausgegeben
		Gemessen in m/s
		TODO: Globale Karte: (https://www.globalwindatlas.info/)
		"""
		return 5.5
	
	def get_globalstrahlung(self, date=False):
		"""
		Durchschnittliche jährliche Summe in kWh/m2 
		(https://photovoltaiksolarstrom.com/photovoltaiklexikon/solarertrag-berechnen/)
		Deutschlandweit zwischen ca 950 und 1200 
		TODO: Globale Karte: (https://globalsolaratlas.info/) (DNI)
		"""
		return 1075