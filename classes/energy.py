# -*- coding: utf-8 -*-

from globals import *
from functions.print import *


class EnergySource:
	erzeugung_twh_2018 	= 0
	co2_intensity				= 0 # g CO2 per kWh
	co2_initial					= 0 # kWh (int or object of ints)
	lifespan						= 0 # in years

	def total_emissions_in_g(self):
		return self.erzeugung_twh_2018 * 1000 * 1000 * self.co2_intensity
	
	def print_total_emissions(self):
		return print_weight(
			self.total_emissions_in_g()
		)
	
	def get_co2_initial(self):
		if type(self.co2_initial) is dict:
			sum = 0
			for key, value in self.co2_initial.items():
				sum += value
			return sum
		else:
			return self.co2_initial
	
	def print_co2_initial(self):
		return print_watt(
			self.get_co2_initial()
		)
	
	def energy_payback_time(self): # Energie-Rücklaufzeit in Monaten
		return 0


# -------------------- Konventionelle Energieträger -------------

class Braunkohle(EnergySource):
	erzeugung_twh_2018 	= 146
	co2_intensity				= 1000 # 729-1230 (001_Bundestag_Bilanzen)

class Kernenergie(EnergySource):
	erzeugung_twh_2018 	= 76
	co2_intensity				= 32 # (001_Bundestag_Bilanzen)

class Steinkohle(EnergySource):
	erzeugung_twh_2018 	= 83
	co2_intensity				= 850 # 622-1080 (001_Bundestag_Bilanzen)

class Erdgas(EnergySource):
	erzeugung_twh_2018 	= 83
	co2_intensity				= 54 # 428,148,49,-409 (001_Bundestag_Bilanzen)

class Mineraloele(EnergySource):
	erzeugung_twh_2018 	= 5
	co2_intensity				= 890

# -------------------- Erneuerbare Energieträger -------------

class Photovoltaik(EnergySource):
	erzeugung_twh_2018 	= 46.2
	co2_intensity				= 120 # 80-160 (001_Bundestag_Bilanzen)
	lifespan						= 20 # (001_Bundestag_Bilanzen)

	def energy_payback_time(self):
		# Abhängig von Sonneneinstrahlung am Standort (001_Bundestag_Bilanzen)
		# Nordwesten ca. 3.6 Jahre
		# Süddeutschland ca. 2.6 Jahre
		return 12 * 3.2

class Windenergie(EnergySource):
	erzeugung_twh_2018 	= 111.6
	co2_intensity				= 12 # 8-16
	co2_initial					= {
		"3_rotorblaetter": 318000,
		"generator": 799000,
		"gondel": 504000,
		"stahlturm": 1048000,
		"kontrollsystem_und_netzanschluss": 420000,
		"fundament": 375000,
	} # (001_Bundestag_Bilanzen)

	def energy_payback_time(self):
		return 4.5 # 3-6 Monate (001_Bundestag_Bilanzen)

	

class Biomasse(EnergySource):
	erzeugung_twh_2018 	= 51.3
	co2_intensity				= 0

class Wasserkraft(EnergySource):
	erzeugung_twh_2018 	= 16.5
	co2_intensity				= 22 # 4-40 (001_Bundestag_Bilanzen)
	lifespan						= 100 # (001_Bundestag_Bilanzen)




# -------------------- Spezifischer -------------


class EnergieForm:
	nennleistung_kwh 			= 1
	kosten_co2 						= None
	kosten_geld 					= 1
	platzbedarf_sqm				= 1

	location_latitude			= 0
	location_longitude		= 0
	location_altitude			= 0

	einspeiseverguetung_cent 	= 10

	def jahresmittel(self):
		return 1
	
	def ertrag_jahr_kwh(self):
		return self.leistung_kwh() * 24 * 365.25

	def ertrag_jahr_eur(self):
		return (self.ertrag_jahr_kwh() * self.einspeiseverguetung_cent) / 100

	def leistung_kwh(self):
		return self.nennleistung_kwh * self.jahresmittel()
	
	def installationskosten_pro_kwh(self):
		return self.kosten_geld / self.leistung_kwh()



class Windrad(EnergieForm):
	kosten_geld 				= 3500000
	nennleistung_kwh 			= 3000
	platzbedarf_sqm				= 200

	einspeiseverguetung_cent	= 4.38

	def jahresmittel(self):
		return 0.25
	


class Solaranlage(EnergieForm):
	kosten_geld 				= 8000
	nennleistung_kwh 			= 6

	einspeiseverguetung_cent	= 10.64

	def jahresmittel(self):
		return 0.103

	




"""
Quellen:
001_Bundestag_Bilanzen: https://www.bundestag.de/resource/blob/406432/70f77c4c170d9048d88dcc3071b7721c/wd-8-056-07-pdf-data.pdf
"""