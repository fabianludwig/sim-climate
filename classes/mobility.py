# -*- coding: utf-8 -*-

from functions.print import *

from helpers.abstract import Producible
from classes.resources import *


# -------------- Komponenten --------------

class LithiumBattery(Producible):
	capacity_in_kwh		 = 0
	yearly_charge_cycles	= 5

	_possible_charge_cycles = 640

	def get_energy_construction(self):
		return self.capacity_in_kwh*(125000)	# (001_Quaschning_Elektroauto)
	
	def get_lifespan(self):
		return self._possible_charge_cycles / self.yearly_charge_cycles



# -------------- Automobiles --------------

class Automobile(Producible):
	km_per_year			= 30000 # wieviele Km fährt das Auto pro Jahr?
	
	def get_energy_operation(self):
		"""
		Zu bedenken: Ersatzteile, Ölwechsel
		"""
		return 0
	
	def get_emission_per_km(self):
		return 100

	def get_kwh_per_km(self):
		return 0

	def print_emission_per_km(self):
		return print_weight(
			self.get_emission_per_km()
		)


class AutomobileFuel(Automobile):
	l_per_100km			= 6.5
	fuel_type			= Benzin()

	def get_emission_per_km(self):
		return (self.l_per_100km/100)/(self.fuel_type.get_dichte()) * self.fuel_type.get_combustion_co2_per_g() * 1000

	def get_kwh_per_km(self):
		return (self.l_per_100km/100)*self.fuel_type.get_brennwert()/self.fuel_type.get_dichte()


class AutomobileElectro(Automobile):
	kwh_per_100km		= 20	# in kWh
	battery_capacity	= 50	# in kWh

	lifespan			= 13

	def set_components(self):
		self.components = [
			LithiumBattery(
				yearly_charge_cycles	= ((self.km_per_year/100)*self.kwh_per_100km)/self.battery_capacity,
				capacity_in_kwh			= self.battery_capacity,
			)
		]
	
	def get_emission_per_km(self):
		"""
		Abhängig von der Stromquelle 
		Kohlestrom: 165g
		Strommix DE: 80g 
		EE: 0g
		(001_Quaschning_Elektroauto)
		"""
		return 80
	
	def get_kwh_per_km(self):
		return self.kwh_per_100km/100


class AutomobileDiesel(AutomobileFuel):
	fuel_type			= Diesel()
	l_per_100km			= 7		# (003_Statista)

class AutomobilePetrol(AutomobileFuel):
	fuel_type			= Benzin()
	l_per_100km			= 7.8 	# (003_Statista)


"""
001_Quaschning_Elektroauto: https://www.youtube.com/watch?v=BBdJSfGQibA
002_Springer: https://www.springerprofessional.de/elektromobilitaet/dieselmotor/endenergiebezogene-analyse-diesel-versus-elektromobilitaet/16673694
003_Statista: https://de.statista.com/statistik/daten/studie/484054/umfrage/durchschnittsverbrauch-pkw-in-privaten-haushalten-in-deutschland/
"""