# -*- coding: utf-8 -*-

from classes.energy import *
from classes.geography import *


class Olfen(Stadt):
	einwohner 			= 12674 # Wikipedia

	flaeche_sqm			= 52.43 # Wikipedia
	location_altitude	= 48 # Wikipedia

	
class Germany(Country):
	einwohner 				= 83000000 # Wikipedia
	haushalte_einzel		= 17263000 # Statista

	flaeche_sqm				= 357578.17 # Wikipedia

	wind_nennleistung_kw 	= 53000000
	solar_nennleistung_kw	= 46000000




"""
to_check = Germany()
to_check.print_results()
"""

braunkohle = Braunkohle()
print(braunkohle.print_total_emissions()+" Braunkohle")
print(braunkohle.print_co2_initial())

kernenergie = Kernenergie()
print(kernenergie.print_total_emissions()+" Kernenergie")
print(kernenergie.print_co2_initial())

steinkohle = Steinkohle()
print(steinkohle.print_total_emissions()+" Steinkohle")
print(steinkohle.print_co2_initial())

erdgas = Erdgas()
print(erdgas.print_total_emissions()+" Erdgas")
print(erdgas.print_co2_initial())

mineraloele = Mineraloele()
print(mineraloele.print_total_emissions()+" Mineralöle")
print(mineraloele.print_co2_initial())


photovoltaik = Photovoltaik()
print(photovoltaik.print_total_emissions()+" Photovoltaik")
print(photovoltaik.print_co2_initial())

windenergie = Windenergie()
print(windenergie.print_total_emissions()+" Windenergie")
print(windenergie.print_co2_initial())

biomasse = Biomasse()
print(biomasse.print_total_emissions()+" Biomasse")
print(biomasse.print_co2_initial())

wasserkraft = Wasserkraft()
print(wasserkraft.print_total_emissions()+" Wasserkraft")
print(wasserkraft.print_co2_initial())