# -*- coding: utf-8 -*-

from classes import energy, geography, mobility, resources

from crawler.windenergy import WindenergyCrawler


"""
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
	instance = energy[energysource](nominal_power=nennleistung)
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
	instance = energy[energystorage]()

"""



"""
mobilities = [
	'AutomobileElectro',
	'AutomobileDiesel',
	'AutomobilePetrol',
]

for mobility in mobilities:
	instance = mobility[mobility]()
	print(mobility)
	print(instance.print_emission_per_km() + ' / 100km')
	instance.get_kwh_per_km()
	print('')
"""

nennleistung = 3000
energysource = energy.Windenergie(nominal_power=nennleistung)
print('')
print('Windenergie (' + str(nennleistung) + ' kW Nennleistung)')
print(energysource.print_expense() + ' Anschaffungskosten')
print(energysource.print_expense_operation() + ' jährliche Kosten')
print(energysource.print_energy_construction() + ' bei Errichtung')
print(energysource.print_yearly_energy_return() + ' erzeugter Strom')
print(energysource.print_yearly_co2_intensity() + ' im Betrieb')
print(str(round(energysource.get_efficiency(), 2))+" % Effizienz")
print('Energie-Rücklaufzeit: ' + energysource.print_energy_payback_time())
print('Kosten-Rücklaufzeit: ' + energysource.print_expense_payback_time())

print('')

print('Diesel: '+resources.Diesel().print_co2_per_kwh())
print('Biodiesel: '+resources.Biodiesel().print_co2_per_kwh())
print('Benzin: '+resources.Benzin().print_co2_per_kwh())
print('Autogas: '+resources.Autogas().print_co2_per_kwh())
print('Erdgas: '+resources.Erdgas().print_co2_per_kwh())
print('Kerosin: '+resources.Kerosin().print_co2_per_kwh())
print('Heizoel: '+resources.Heizoel().print_co2_per_kwh())
print('Braunkohle: '+resources.Braunkohle().print_co2_per_kwh())
print('Steinkohle: '+resources.Steinkohle().print_co2_per_kwh())

print('')

print('Holz: '+resources.Holz().print_co2_per_kwh())
print('Torf: '+resources.Torf().print_co2_per_kwh())
print('Rohoel: '+resources.Rohoel().print_co2_per_kwh())
print('Raffineriegas: '+resources.Raffineriegas().print_co2_per_kwh())
print('Fluessiggas: '+resources.Fluessiggas().print_co2_per_kwh())
print('Haushaltsmuell: '+resources.Haushaltsmuell().print_co2_per_kwh())

print('')

print('Benziner: '+mobility.AutomobilePetrol().print_emission_per_km())
print('Diesel: '+mobility.AutomobileDiesel().print_emission_per_km())
print('Elektro: '+mobility.AutomobileElectro().print_emission_per_km())


"""
crawler = WindenergyCrawler()
crawler.crawl_items()
"""

"""
Quellen:
001_Umweltbundesamt_Stromerzeugung: https://www.umweltbundesamt.de/sites/default/files/medien/384/bilder/dateien/3_datentabelle-zur-abb_bruttostromerzeugung-et_2019-02-26.pdf

"""