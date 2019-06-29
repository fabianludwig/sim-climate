# -*- coding: utf-8 -*-

from functions.print import *


class Location:
	latitude		= 51.7037766
	longitude		= 7.3402764

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

	def get_sonnenstand_sommer(self):
		"""
		Sommersonnenwende (003_MPPSolar)
		Einfallswinkel der Mittagssonnee
		"""
		return 90-(int(self.latitude)-23)

	def get_sonnenstand_winter(self):
		"""
		Wintersonnenwende (003_MPPSolar)
		Einfallswinkel der Mittagssonnee
		"""
		return 90-(int(self.latitude)+23)

	def get_altitude(self):
		return 0
    
	def get_windgeschwindigkeit(self):
		"""
		Jahresmittel der Windgeschwindigkeit in 80m Höhe (002_DeutscherWetterdienst)
		Gemessen in m/s
		"""
		return 5.5
    
	def get_globalstrahlung(self):
		"""
		Durchschnittliche jährliche Summe in kWh/m2 (001_PVSolarstrom)
		Deutschlandweit zwischen ca 950 und 1200 
		"""
		return 1075



class Buildable:
	lifespan	= 0 	# in years
	expense		= 0		# (Errichtungskosten)

	def get_expense(self):
		return self.expense
	
	def print_expense(self):
		return print_money(self.get_expense())



"""
Quellen:
001_PVSolarstrom: https://photovoltaiksolarstrom.com/photovoltaiklexikon/solarertrag-berechnen/
002_DeutscherWetterdienst: https://www.dwd.de/DE/leistungen/_config/leistungsteckbriefPublication.pdf?view=nasPublication&nn=16102&imageFilePath=1984673719052460620550302552147834994911318791076805607326336086634847969459358946555032055462272638945184535799804022754249241658870336218612364515164241169787346171968215343642867407127803970689474140526989975481747650065031520731391283821&download=true
003_MPPSolar: https://www.mpptsolar.com/de/optimale-ausrichtung-dachneigung-solaranlage.html
"""
