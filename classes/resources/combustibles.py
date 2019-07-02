# -*- coding: utf-8 -*-

from ._base_ import *


# ------------ Kraftstoffe ------------


class Diesel(Combustible, Fluid):
	dichte		= 830   # (009_Chemie_Diesel)

	def get_brennwert(self):
		return 10.4*self.get_dichte()  # (007_Wikipedia_Diesel)

	def get_production_kwh_per_g(self):
		return 7/self.get_dichte()  # (001_Springer)
	
	def get_combustion_co2_per_g(self):
		return 2.64*self.get_dichte()  # (009_Chemie_Diesel)
	
	def get_expense(self):
		return 1.25*self.get_dichte()   # Preis pro Liter ca. 1.25€


class Biodiesel(Diesel):
	dichte		= 880   # (006_Wikipedia_Biodiesel)

	def get_brennwert(self):
		return 11.1*self.get_dichte()  # (006_Wikipedia_Biodiesel)

	def get_expense(self):
		return super().get_expense()-0.09 # (004_Spritmonitor_Biodiesel)
	
	def get_combustion_co2_per_g(self):
		return super().get_combustion_co2_per_g()*0.25 # (004_Spritmonitor_Biodiesel)


class Benzin(Combustible, Fluid):
	dichte		= 750   # (002_Helpster)

	def get_brennwert(self):
		return 9.7*self.get_dichte()  # (008_ErdgasInfo)

	def get_combustion_co2_per_g(self):
		return 2.36*self.get_dichte()  # (003_Spritmonitor)
	
	def get_expense(self):
		return 1.50*self.get_dichte()   # Preis pro Liter ca. 1.50€


class Autogas(Combustible, Fluid):
	dichte		= 570   	# (005_Wikipedia_Autogas)
	brennwert 	= 12.8		# (005_Wikipedia_Autogas)

	def get_combustion_co2_per_g(self):
		return 1.64*self.get_dichte()  # (003_Spritmonitor)
	
	def get_expense(self):
		return 0.67*self.get_dichte()   # Preis pro Liter ca. 60c


class Erdgas(Combustible):
	brennwert		= 0.0119

	def get_combustion_co2_per_g(self):
		return 2.79/1000	# (003_Spritmonitor)
	
	def get_expense(self):
		return 0.7/1000   	# Preis pro Kilogramm ca. 70c


"""
001_Springer: https://www.springerprofessional.de/elektromobilitaet/dieselmotor/endenergiebezogene-analyse-diesel-versus-elektromobilitaet/16673694
002_Helpster: http://www.helpster.de/1-liter-diesel-in-kg-umrechnungstipps_191983
003_Spritmonitor: https://www.spritmonitor.de/de/berechnung_co2_ausstoss.html
004_Spritmonitor_Biodiesel: https://www.spritmonitor.de/de/alternative_biodiesel.html
005_Wikipedia_Autogas: https://de.wikipedia.org/wiki/Autogas
006_Wikipedia_Biodiesel: https://de.wikipedia.org/wiki/Biodiesel
007_Wikipedia_Diesel: https://de.wikipedia.org/wiki/Diesel
008_ErdgasInfo: https://www.erdgas.info/erdgas-mobil/erdgas-als-kraftstoff/reichweite-von-gas-autos/
009_Chemie_Diesel: https://www.chemie.de/lexikon/Dieselkraftstoff.html
"""



# ------------ Brennstoffe ------------


class Holz(Combustible):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.39*1000	


class Torf(Combustible):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.38*1000	


class Braunkohle(Combustible):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.41*1000	


class Steinkohle(Combustible):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.34*1000	


class Heizoel(Combustible, Fluid):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.28*1000


class Rohoel(Combustible, Fluid):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.26*1000	


class Kerosin(Combustible, Fluid):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.26*1000	


class Raffineriegas(Combustible, Fluid):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.24*1000	


class Fluessiggas(Combustible, Fluid):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.23*1000	


class Naturgas(Combustible, Fluid):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.20*1000	



"""
010_Quaschning_C02_Brennstoffe: https://www.volker-quaschning.de/datserv/CO2-spez/index.php
"""