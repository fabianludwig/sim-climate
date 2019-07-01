# -*- coding: utf-8 -*-

from .energysources import EnergySource
from helpers.abstract import Producible


# -------------- Komponenten --------------

class PVModul(Producible):
	expense 	= 5000		# (006_EnergieHeld_Kosten) (bei 6 kWp)

class Wechselrichter(Producible):
	expense 	= 1400		# (006_EnergieHeld_Kosten) (bei 6 kWp)
	lifespan	= 15

class Stromspeicher(Producible):
	expense 	= 8000		# (006_EnergieHeld_Kosten) (bei 6 kWp)

class KleinteileZubehoer(Producible):
	expense 	= 1800		# (006_EnergieHeld_Kosten) (bei 6 kWp)



class Photovoltaik(EnergySource):
	co2_intensity				= 120 	# 80-160 (001_Bundestag_Bilanzen)

	nominal_power				= 6		# aka kWp/PNenn
	lifespan					= 25	# (006_EnergieHeld_Kosten)
	expense						= 8000

	ausrichtung					= 'S' 	# (N, NO/NW, O/W, SO/SW, S)
	neigungswinkel				= 30 	# in Grad (0-90)
	m2_per_kwp					= 7

	price_per_kwh				= 11.47	# in cents

	def set_components(self):
		self.components	= [
			PVModul(), 
			Wechselrichter(), 
			#Stromspeicher(), 
			KleinteileZubehoer(),
		]

	def get_energy_construction(self):
		return 10000*self.nominal_power # (005_Quaschning)
	
	def get_expense(self):
		"""
		(006_EnergieHeld_Kosten)
		"""
		if self.nominal_power < 10:
			formula = lambda x : (2/15)*(x*x)-(7/3)*x+23.2
			price_per_kwp = formula(min(self.nominal_power,8.75))*100
		elif self.nominal_power < 40:
			price_per_kwp = 1100
		elif self.nominal_power < 500:
			price_per_kwp = 1000
		else:
			price_per_kwp = 950
		return price_per_kwp*self.nominal_power
	
	def get_flaeche(self): # in m2
		return self.nominal_power*self.m2_per_kwp

	def get_expense_operation(self):
		return self.get_expense()*0.015/self.lifespan

	def get_flaechenfaktor(self):
		"""
		Wird berechnet in Prozent und ergibt sich aus Ausrichtung und Neigungswinkel
		Ist je nach Region und Monat unterschiedlich (vmtl. wegen Sonnenstand und -kraft)
		(004_SolaratlasNRW)
		"""
		return 110

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
			

# ---------------- Solarzellen-Typen ----------------


class MonokristallineSolarzelle(Photovoltaik):
	m2_per_kwp					= 6 	# (007_SolaranlageRatgeber_Dimensionierung)
	wirkungsgrad				= 17	# 14-20 (008_SolaranlagenPortal)


class PolykristallineSolarzelle(Photovoltaik):
	m2_per_kwp					= 8 	# (007_SolaranlageRatgeber_Dimensionierung)
	wirkungsgrad				= 14	# 12-16 (008_SolaranlagenPortal)


class DuennschichtModul(Photovoltaik):
	wirkungsgrad				= 8		# 6-10 (008_SolaranlagenPortal)


"""
Quellen:
001_Bundestag_Bilanzen: https://www.bundestag.de/resource/blob/406432/70f77c4c170d9048d88dcc3071b7721c/wd-8-056-07-pdf-data.pdf
002_EnergieExperten: https://www.energie-experten.org/erneuerbare-energien/photovoltaik/planung/ertrag.html
003_PVSolarstrom: https://photovoltaiksolarstrom.com/photovoltaiklexikon/solarertrag-berechnen/
004_SolaratlasNRW: https://energietools.ea-nrw.de/_database/_data/datainfopool/Solaratlas2001.pdf
005_Quaschning (Statisiken -> Energieaufwand zur Herstellung regenerativer Anlagen) https://www.volker-quaschning.de/datserv/kev/index.php
006_EnergieHeld_Kosten: https://www.energieheld.de/solaranlage/photovoltaik/kosten
007_SolaranlageRatgeber_Dimensionierung: https://www.solaranlage-ratgeber.de/photovoltaik/photovoltaik-planung/photovoltaikanlage-dimensionierung
008_SolaranlagenPortal: https://www.solaranlagen-portal.com/solarmodule/systeme/vergleich

https://de.wikipedia.org/wiki/Liste_von_Solarkraftwerken_in_Deutschland
"""
