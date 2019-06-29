# -*- coding: utf-8 -*-

from .energysources import EnergySource


class Photovoltaik(EnergySource):
	co2_intensity				= 120 	# 80-160 (001_Bundestag_Bilanzen)

	nominal_power				= 6		# aka kWp/PNenn
	lifespan					= 20
	expense						= 8000

	ausrichtung					= 'S' 	# (N, NO/NW, O/W, SO/SW, S)
	neigungswinkel				= 30 	# in Grad (0-90)

	def get_energy_construction(self):
		return 10000*self.nominal_power # (005_Quaschning)

	def get_flaechenfaktor(self):
		"""
		Wird berechnet in Prozent und ergibt sich aus Ausrichtung und Neigungswinkel
		Ist je nach Region und Monat unterschiedlich (vmtl. wegen Sonnenstand und -kraft)
		(004_SolaratlasNRW)
		"""
		return 95

	def get_ideal_solarertrag(self):
		"""
		Die Globalstrahlung ist die durchschnittliche jährliche Summe gemessen in kWh/kWp
		Bundesweiter Durchschnitt in den Jahren 2014, 2015, 2016: 967 (002_EnergieExperten)
		"""
		return self.get_globalstrahlung()*(self.get_flaechenfaktor()/100)

	def get_theoretical_solarertrag(self):
		"""
		Die theoretisch aufnehmbare Menge Sonnenenergie pro m2
		(003_PVSolarstrom)
		"""
		return self.nominal_power * self.get_ideal_solarertrag()

	def get_practical_solarertrag(self):
		"""
		Der theoretische Solarertrag verringert um die Verluste 
		Der Multiplikator wird auch PR (Performance Ratio) genannt
		Gute Solaranlagen erreichen dabei einen Wert zwischen 0.75 und 0.85
		(003_PVSolarstrom)
		"""
		return self.get_theoretical_solarertrag()*0.8

	def get_efficiency(self):
		return self.get_practical_solarertrag()/(24*365.25) / (self.nominal_power) * 100
	
	def get_yearly_energy_return(self):
		return self.get_practical_solarertrag()
	
	def energy_payback_time(self):
		"""
		Abhängig von Sonneneinstrahlung am Standort (001_Bundestag_Bilanzen)
		Nordwesten ca. 3.6 Jahre
		Süddeutschland ca. 2.6 Jahre
		"""
		return super().energy_payback_time()
		

# ---------------- Solarzellen-Typen ----------------


class MonokristallineSolarzelle(Photovoltaik):
	pass


class PolykristallineSolarzelle(Photovoltaik):
	def energy_payback_time(self):
		return super().energy_payback_time()
		# Erhofftes Ergebnis: 12 * 1.5-2.5 (001_Bundestag_Bilanzen)


"""
Quellen:
001_Bundestag_Bilanzen: https://www.bundestag.de/resource/blob/406432/70f77c4c170d9048d88dcc3071b7721c/wd-8-056-07-pdf-data.pdf
002_EnergieExperten: https://www.energie-experten.org/erneuerbare-energien/photovoltaik/planung/ertrag.html
003_PVSolarstrom: https://photovoltaiksolarstrom.com/photovoltaiklexikon/solarertrag-berechnen/
004_SolaratlasNRW: https://energietools.ea-nrw.de/_database/_data/datainfopool/Solaratlas2001.pdf
005_Quaschning (Statisiken -> Energieaufwand zur Herstellung regenerativer Anlagen) https://www.volker-quaschning.de/datserv/kev/index.php
"""
