# -*- coding: utf-8 -*-
from helpers.location import Location
from helpers.abstract import Producible

class EnergyStorage(Location, Producible):
	efficiency 				= 0 # in % (Wirkungsgrad)
	capacity				= 0 # in kWh


class Pumpspeicherkraftwerke(EnergyStorage):
	"""
	Wasser wird zwischen zwei Speicherbecken bewegt (oberes & unteres)
	Bei Stromüberfluss: Wasser wird von unten nach oben gepumpt
	Bei Bedarf: Wasser wird runtergelassen und treibt eine Turbine mit Generator an
	Schon lange im Einsatz und technisch gut ausgereift.
	Problem: Große Becken müssen künstlich angelegt werden.
	"""
	efficiency	= 80 # (001_Quaschning)

class PowerToGas(EnergyStorage):
	"""
	Wasser und Kohlendioxid wird zu Wasserstoff und Methan.
	Methan kann in Biogasanlagen verstromt werden. Wasserstoff mithilfe von Brennstoffzellen.
	1. Schritt: Elektrolyse erzeugt mit Strom aus Wasser -> Wasserstoff
	2. Methanisierung: mit Kohlendioxid wird Methan erzeugt
	Methan ist direkt kompatibel mit Erdgas (vorhandene Infrastruktur nutzbar [Gasspeicher, Gaskraftwerke])
	Wird für saisonale Speicherung eingesetzt werden (Verwendung: 1-3 Mal im Jahr)
	"""
	efficiency 	= 42.5 # 35-50 (001_Quaschning)

class Batteriespeicher(EnergyStorage):
	"""
	Dezentrale Batteriespeicher werden in Häusern verbaut 
	(Auch Elektroautos können als dezentraler Batteriespeicher dienen)
	Sie ermöglichen eine Zwischenspeicherung für den Bedarf über mehrere Stunden.
	Können optimal mit PV-Anlagen gekoppelt werden.
	"""
	efficiency 	= 99 # (002_PV-Magazin)


"""
Quellen:
001_Quaschning: https://www.youtube.com/watch?v=CE-6jsWCATk
002_PV-Magazin: https://www.pv-magazine.de/2017/11/21/antworten-zum-webinar-effizienz-bei-batteriespeichern-ist-mehr-als-der-wirkungsgrad/

"""