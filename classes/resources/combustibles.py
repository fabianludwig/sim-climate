# -*- coding: utf-8 -*-

from ._base_ import *


# ------------ Kraftstoffe ------------

class Diesel(CombustibleFluid):
	dichte					= 830		# (https://www.chemie.de/lexikon/Dieselkraftstoff.html)
	combustion_co2_per_l	= 2650		# (https://www.chemie.de/lexikon/Dieselkraftstoff.html)
	brennwert_per_l			= 9.8		# (https://www.chemie.de/lexikon/Dieselkraftstoff.html)

	expense_per_l			= 1.25

	def get_production_kwh_per_g(self):
		return 7/self.get_dichte()/1000	# (001_Springer)
	

class Biodiesel(Diesel):
	dichte					= 880   	# (006_Wikipedia_Biodiesel)
	brennwert_per_l			= 11.1

	def get_expense(self):
		return super().get_expense()-0.09 # (004_Spritmonitor_Biodiesel)
	
	def get_combustion_co2_per_g(self):
		return super().get_combustion_co2_per_g()*0.25 # (004_Spritmonitor_Biodiesel)


class Benzin(CombustibleFluid):
	dichte					= 750   	# (002_Helpster)
	brennwert_per_l			= 9.7		# (008_ErdgasInfo)
	combustion_co2_per_l	= 2360		# (003_Spritmonitor)
	
	expense_per_l			= 1.5		# Preis pro Liter ca. 1.50€


class Autogas(CombustibleFluid):
	brennwert 				= 12.8		# (005_Wikipedia_Autogas)
	
	dichte					= 570   	# (005_Wikipedia_Autogas)
	combustion_co2_per_l	= 1640		# (003_Spritmonitor)
	
	expense_per_l			= 0.67


class Erdgas(Combustible):
	brennwert				= 10.83		# (010_Biobrennstoffhof)
	combustion_co2_per_g	= 2.79		# (003_Spritmonitor)

	expense					= 0.7


class Kerosin(CombustibleFluid):
	brennwert_per_l			= 9.5		# (008_ErdgasInfo)
	combustion_co2_per_g	= 2.76		# (https://www.chemie.de/lexikon/Kerosin.html)
	dichte					= 800   	# (https://de.wikipedia.org/wiki/Kerosin)


# ------------ Brennstoffe ------------


class Heizoel(CombustibleFluid):
	brennwert				= 11.86		# (010_Biobrennstoffhof)
	combustion_co2_per_l	= 2650		# (https://de.wikipedia.org/wiki/Heiz%C3%B6l)
	
	dichte					= 840		



class Braunkohle(Combustible):
	brennwert				= 5.3		# (010_Biobrennstoffhof)
	combustion_co2_per_g	= 2.12		# (010_Quaschning_C02_Brennstoffe)


class Steinkohle(Combustible):
	brennwert				= 7.0		# (010_Biobrennstoffhof)
	combustion_co2_per_g	= 2.38		# (010_Quaschning_C02_Brennstoffe)





class Holz(Combustible):
	brennwert				= 4.9		# (010_Biobrennstoffhof)

	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.39*1000	


class Torf(Combustible):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.38*1000	


class Rohoel(CombustibleFluid):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.26*1000	


class Raffineriegas(CombustibleFluid):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.24*1000	


class Fluessiggas(CombustibleFluid):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.23*1000	


class Naturgas(CombustibleFluid):
	def get_co2_per_kwh(self):
		# (010_Quaschning_C02_Brennstoffe)
		return 0.20*1000	


class Haushaltsmuell(Combustible):
	brennwert				= 2.5		# (010_Biobrennstoffhof)





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
010_Quaschning_C02_Brennstoffe: https://www.volker-quaschning.de/datserv/CO2-spez/index.php
010_Biobrennstoffhof: http://www.biobrennstoffhof.de/leistung.htm
"""