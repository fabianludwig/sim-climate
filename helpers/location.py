# -*- coding: utf-8 -*-
import math

from functions.print import *


class Location:
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

			print(day_of_year, deklination)
		return 90-(self.latitude-deklination)

	def get_altitude(self):
		"""
		Höhenkarte?
		TODO: OpenStreetMap sollte Elevation anbeiten (s. OpenTopoMap)
		"""
		return 0
    
	def get_windgeschwindigkeit(self, date=False):
		"""
		Durchschnittliche Windgeschwindigkeit in 80m Höhe (002_DeutscherWetterdienst)
		Wenn kein Datum angegeben wird das Jahresmittel ausgegeben
		Gemessen in m/s
		TODO: Globale Karte: (005_GlobalWindAtlas)
		"""
		return 5.5
    
	def get_globalstrahlung(self, date=False):
		"""
		Durchschnittliche jährliche Summe in kWh/m2 (001_PVSolarstrom)
		Deutschlandweit zwischen ca 950 und 1200 
		TODO: Globale Karte: (006_GlobalSolarAtlas) (DNI)
		"""
		return 1075



"""
Quellen:
001_PVSolarstrom: https://photovoltaiksolarstrom.com/photovoltaiklexikon/solarertrag-berechnen/
002_DeutscherWetterdienst: https://www.dwd.de/DE/leistungen/_config/leistungsteckbriefPublication.pdf?view=nasPublication&nn=16102&imageFilePath=1984673719052460620550302552147834994911318791076805607326336086634847969459358946555032055462272638945184535799804022754249241658870336218612364515164241169787346171968215343642867407127803970689474140526989975481747650065031520731391283821&download=true
005_GlobalWindAtlas: https://www.globalwindatlas.info/
006_GlobalSolarAtlas: https://globalsolaratlas.info/

"""
