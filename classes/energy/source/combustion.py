# -*- coding: utf-8 -*-

from ._base_ import EnergySource
from helpers.abstract import Producible


class Braunkohle(EnergySource):
	co2_intensity				= 979.5 	# 729-1230 (001_Bundestag_Bilanzen)


class Kernenergie(EnergySource):
	# https://de.wikipedia.org/wiki/Liste_der_Kernreaktoren_in_Deutschland
	co2_intensity				= 32 	# (001_Bundestag_Bilanzen)


class Steinkohle(EnergySource):
	co2_intensity				= 850 	# 622-1080 (001_Bundestag_Bilanzen)


class Erdgas(EnergySource):
	co2_intensity				= 54 	# 428,148,49,-409 (001_Bundestag_Bilanzen)


class Mineraloele(EnergySource):
	co2_intensity				= 890	# (001_Bundestag_Bilanzen)
	

class Biomasse(EnergySource):
	# https://de.wikipedia.org/wiki/Liste_von_Biomassekraftwerken_in_Deutschland
	co2_intensity				= 0


"""
Quellen:
001_Bundestag_Bilanzen: https://www.bundestag.de/resource/blob/406432/70f77c4c170d9048d88dcc3071b7721c/wd-8-056-07-pdf-data.pdf
002_Umweltbundesamt_Emissionsbilanz_EE: https://www.umweltbundesamt.de/sites/default/files/medien/1410/publikationen/2018-10-22_climate-change_23-2018_emissionsbilanz_erneuerbarer_energien_2017_fin.pdf

https://de.wikipedia.org/wiki/Liste_von_fossil-thermischen_Kraftwerken_in_Deutschland
"""