# -*- coding: utf-8 -*-

from ._base_ import EnergySource
from ..._base_ import Producible


# -------------- Komponenten --------------

class Rotorblatt(Producible):
	energy_construction = 106000	# (001_Bundestag_Bilanzen)

class Generator(Producible):
	energy_construction = 799000	# (001_Bundestag_Bilanzen)

class Gondel(Producible):
	energy_construction = 504000	# (001_Bundestag_Bilanzen)

class Stahlturm(Producible):
	energy_construction = 1048000	# (001_Bundestag_Bilanzen)

class KontrollsystemUndNetzanschluss(Producible):
	energy_construction = 420000	# (001_Bundestag_Bilanzen)

class Fundament(Producible):
	energy_construction = 375000 	# (001_Bundestag_Bilanzen)



class Windenergie(EnergySource):
	co2_intensity				= 12 # 8-16

	nominal_power 				= 3050		# (002_Enercon_Datenblatt_E-101)
	lifespan					= 20 		# in years (002_Enercon_Datenblatt_E-101)

	nabenhoehe					= 99		# in m (002_Enercon_Datenblatt_E-101)
	rotordurchmesser			= 101		# in m (002_Enercon_Datenblatt_E-101)
	abschaltgeschwindigkeit		= 34		# in m/s (002_Enercon_Datenblatt_E-101)
	blattzahl					= 3

	price_per_kwh				= 5.2925	# in cents (006_SWEWindenergie)

	def set_components(self):
		for i in range(self.blattzahl):
			self.components.append(
				Rotorblatt(),
			)
		self.components.append(
			Generator(),
			Gondel(),
			Stahlturm(),
			KontrollsystemUndNetzanschluss(),
			Fundament(),
		)

	def get_energy_construction(self):
		return 6500*self.nominal_power 	# (005_Quaschning)

	def get_efficiency(self):
		"""
		(004_WindTurbine_Leistungskurven)
		Verallgemeinerung
		Unterscheidet sich eigentlich noch nach individuellen Faktoren
		"""
		windgeschwindigkeit = self.get_windgeschwindigkeit()

		auslastung 	= 	(7/6)*windgeschwindigkeit*windgeschwindigkeit \
						- (25/6)*windgeschwindigkeit

		if windgeschwindigkeit > self.abschaltgeschwindigkeit:
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
006_SWEWindenergie: https://www.swe-windenergie.de/unternehmen/vergutungssatze-windkraftanlagen.html


https://de.wikipedia.org/wiki/Liste_der_gr%C3%B6%C3%9Ften_deutschen_Onshore-Windparks
https://de.wikipedia.org/wiki/Liste_der_Offshore-Windparks
https://de.wikipedia.org/wiki/Liste_der_deutschen_Offshore-Windparks
"""