# -*- coding: utf-8 -*-

from globals import *
from functions.print import *

from helpers.location import Location
from helpers.abstract import Producible


class EnergySource(Location, Producible):
	co2_intensity				= 0 	# in g CO2 per kWh

	nominal_power				= 1		# (Nennleistung in kWh)
	efficiency					= 100	# in % (Wirkungsgrad)

	price_per_kwh				= 25	# in cents

	def __init__(self, **kwargs):
		if 'nominal_power' in kwargs and 'energy_construction' not in kwargs:
			multiplicator = kwargs.get("nominal_power") / self.nominal_power
			self.energy_construction = self.get_energy_construction()*multiplicator
		self.__dict__.update(kwargs)

	def get_efficiency(self):
		"""
		Wirkungsgrad in %
		"""
		return self.efficiency
	
	def get_co2_intensity(self):
		return self.co2_intensity
	
	def energy_payback_time(self):
		"""
		Energie-Rücklaufzeit in Monaten
		(aka "energetische Amortisationszeit")
		Die Dauer bis die für die Erichtung benötigte Energie wieder produziert wurde
		"""
		if self.get_yearly_energy_return() > 0:
			return self.get_energy_construction() / self.get_yearly_energy_return() * 12
		else:
			return None
	
	def expense_payback_time(self):
		if self.get_yearly_return() > 0:
			return self.get_expense() / (self.get_yearly_return()-self.get_expense_operation()) * 12
		else:
			return None

	def get_yearly_return(self):
		"""
		Einnahmen für Strom pro Jahr
		"""
		return self.get_yearly_energy_return()*self.price_per_kwh/100

	def get_yearly_energy_return(self):
		"""
		Erzeugter Strom pro Jahr
		"""
		return self.nominal_power * (self.get_efficiency()/100) * 24 * 365.25

	# ------------- Prints -------------
	
	def print_yearly_co2_intensity(self):
		return print_weight(
			self.get_co2_intensity()*self.get_yearly_energy_return()
		)+' CO2'
	
	def print_yearly_energy_return(self):
		return print_watt(
			self.get_yearly_energy_return()
		)
	
	def print_energy_payback_time(self):
		if self.energy_payback_time():
			return print_months(
				self.energy_payback_time()
			)
		else:
			return 'Nie'
	
	def print_expense_payback_time(self):
		if self.expense_payback_time():
			return print_months(
				self.expense_payback_time()
			)
		else:
			return 'Nie'




# -------------------- Spezifische Energieträger -------------


class Braunkohle(EnergySource):
	co2_intensity				= 979.5 	# 729-1230 (001_Bundestag_Bilanzen)


class Kernenergie(EnergySource):
	# https://de.wikipedia.org/wiki/Liste_der_Kernreaktoren_in_Deutschland
	co2_intensity				= 32 	# (001_Bundestag_Bilanzen)


class Steinkohle(EnergySource):
	co2_intensity				= 850 	# 622-1080 (001_Bundestag_Bilanzen)


class Erdgas(EnergySource):
	co2_intensity				= 54 	# 428,148,49,-409 (001_Bundestag_Bilanzen)


class Mineraloele(EnergySource):
	co2_intensity				= 890	# (001_Bundestag_Bilanzen)
	

class Biomasse(EnergySource):
	# https://de.wikipedia.org/wiki/Liste_von_Biomassekraftwerken_in_Deutschland
	co2_intensity				= 0


class Wasserkraft(EnergySource):
	# https://de.wikipedia.org/wiki/Liste_von_Wasserkraftwerken_in_Deutschland
	co2_intensity				= 22 	# 4-40 (001_Bundestag_Bilanzen)
	lifespan					= 100 	# (001_Bundestag_Bilanzen)




"""
Quellen:
001_Bundestag_Bilanzen: https://www.bundestag.de/resource/blob/406432/70f77c4c170d9048d88dcc3071b7721c/wd-8-056-07-pdf-data.pdf
002_Umweltbundesamt_Emissionsbilanz_EE: https://www.umweltbundesamt.de/sites/default/files/medien/1410/publikationen/2018-10-22_climate-change_23-2018_emissionsbilanz_erneuerbarer_energien_2017_fin.pdf

https://de.wikipedia.org/wiki/Liste_von_fossil-thermischen_Kraftwerken_in_Deutschland
"""