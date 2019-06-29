# -*- coding: utf-8 -*-

from .energysources import EnergySource


class Windenergie(EnergySource):
	co2_intensity				= 12 # 8-16
	energy_construction			= {
		"3_rotorblaetter": 318000,
		"generator": 799000,
		"gondel": 504000,
		"stahlturm": 1048000,
		"kontrollsystem_und_netzanschluss": 420000,
		"fundament": 375000,
	} # (001_Bundestag_Bilanzen)

	nominal_power 				= 3050		# (002_Enercon_Datenblatt_E-101)
	expense 					= 3500000
	lifespan					= 20 		# in years (002_Enercon_Datenblatt_E-101)

	nabenhoehe					= 99		# in m (002_Enercon_Datenblatt_E-101)
	rotordurchmesser			= 101		# in m (002_Enercon_Datenblatt_E-101)
	abschaltgeschwindigkeit		= 34		# in m/s (002_Enercon_Datenblatt_E-101)

	def get_energy_construction(self):
		return 6500*self.nominal_power 	# (005_Quaschning)

	def get_efficiency(self):
		"""
		(004_WindTurbine_Leistungskurven)
		Verallgemeinerung
		Unterscheidet sich eigentlich noch nach individuellen Faktoren
		"""
		auslastung 	= 	(7/6)*self.get_windgeschwindigkeit()*self.get_windgeschwindigkeit() \
						- (25/6)*self.get_windgeschwindigkeit()

		if self.get_windgeschwindigkeit() > self.abschaltgeschwindigkeit:
			return 0
		elif auslastung < 0:
			return 0
		elif auslastung > 100:
			return 100
		else:
			return auslastung
	
	def get_expense(self):
		"""
		Die Kosten werden pro Kilowatt Leistung berechnet
		(003_EEWindenergie)
		"""
		if self.nominal_power < 1000:
			return self.nominal_power * 735
		else:
			return self.nominal_power * 900



"""
Quellen:
001_Bundestag_Bilanzen: https://www.bundestag.de/resource/blob/406432/70f77c4c170d9048d88dcc3071b7721c/wd-8-056-07-pdf-data.pdf
002_Enercon_Datenblatt_E-101: https://www.enercon.de/fileadmin/Redakteur/Medien-Portal/broschueren/pdf/EC_Datenblaetter_WEA_de_052019.pdf
003_EEWindenergie: http://www.erneuerbare-energie-windenergie.de/windenergie-kosten
004_WindTurbine_Leistungskurven: https://www.wind-turbine-models.com/powercurves
005_Quaschning (Statisiken -> Energieaufwand zur Herstellung regenerativer Anlagen) https://www.volker-quaschning.de/datserv/kev/index.php
"""