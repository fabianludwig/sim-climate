# -*- coding: utf-8 -*-

from classes.energy.energysources import *
from classes.energy.solarenergy import *
from classes.energy.windenergy import *
from classes.geography import *
from classes.energy.energystorage import *

from crawler.windenergy import WindenergyCrawler

class Olfen(Stadt):
	einwohner 			= 12674 # Wikipedia

	flaeche_sqm			= 52.43 # Wikipedia
	location_altitude	= 48 	# Wikipedia

	
class Germany(Country):
	einwohner 				= 83000000 	# Wikipedia
	haushalte_einzel		= 17263000 	# Statista

	flaeche_sqm				= 357578.17 # Wikipedia

	wind_nennleistung_kw 	= 53000000
	solar_nennleistung_kw	= 46000000

	erzeugung_twh_2018		= {
		'Braunkohle': 146,		# (001_Umweltbundesamt_Stromerzeugung)
		'Kernenergie': 76,		# (001_Umweltbundesamt_Stromerzeugung)
		'Steinkohle': 83,		# (001_Umweltbundesamt_Stromerzeugung)
		'Erdgas': 83,			# (001_Umweltbundesamt_Stromerzeugung)
		'Mineraloele': 5,		# (001_Umweltbundesamt_Stromerzeugung)
		'Photovoltaik': 46.2,	
		'Windenergie': 111.6,
		'Biomasse': 51.3,
		'Wasserkraft': 16.5,
	}




"""
to_check = Germany()
to_check.print_results()
"""

"""
energysources = [
	'Braunkohle',
	'Kernenergie',
	'Steinkohle',
	'Erdgas',
	'Mineraloele',
	'Photovoltaik',
	'Windenergie',
	'Biomasse',
	'Wasserkraft',
]

energystorages = [
	'Pumpspeicherkraftwerke',
	'PowerToGas',
	'Batteriespeicher',
]

for energysource in energysources:
	nennleistung = 3000
	instance = globals()[energysource](nominal_power=nennleistung)
	print(energysource + ' (' + str(nennleistung) + ' kW Nennleistung)')
	print(instance.print_expense() + ' Anschaffungskosten')
	print(instance.print_expense_operation() + ' jährliche Kosten')
	print(instance.print_energy_construction() + ' bei Errichtung')
	print(instance.print_yearly_energy_return() + ' erzeugter Strom')
	print(instance.print_yearly_co2_intensity() + ' im Betrieb')
	print(str(round(instance.get_efficiency(), 2))+" % Effizienz")
	print('Energie-Rücklaufzeit: ' + instance.print_energy_payback_time())
	print('Kosten-Rücklaufzeit: ' + instance.print_expense_payback_time())
	print('')

for energystorage in energystorages:
	instance = globals()[energystorage]()
"""

crawler = WindenergyCrawler()
crawler.crawl_items()


"""
Quellen:
001_Umweltbundesamt_Stromerzeugung: https://www.umweltbundesamt.de/sites/default/files/medien/384/bilder/dateien/3_datentabelle-zur-abb_bruttostromerzeugung-et_2019-02-26.pdf

"""