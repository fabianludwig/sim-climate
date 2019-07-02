# -*- coding: utf-8 -*-

import os, csv

from functions.print import *
from classes import energy, geography, mobility, resources




def get_location_by_plz(plz, country='germany'):
	# https://launix.de/launix/launix-gibt-plz-datenbank-frei/
	file_path = './data/countries/'+country+'/plz.csv'
	if os.path.isfile(file_path):
		with open(file_path, 'r') as file:
			reader = csv.reader(file, delimiter =';', quotechar ='"')
			for row in reader:
				if int(row[0]) == int(plz):
					location = {
						'longitude': row[2],
						'latitude': row[3],
					}
					return location
	return {'longitude': None,'latitude': None,}

def get_plants(country='germany', filter={}):
	output_list = []
	file_path = './data/countries/'+country+'/plants_100MW+.csv'
	if os.path.isfile(file_path):
		with open(file_path, 'r') as file:
			reader = csv.reader(file, delimiter =';')
			for row in reader:
				if not filter or filter in row[9]:
					output_list.append({
						'name': row[0],
						'betreiber': row[1],
						#'bundesland': row[2],
						'plz': row[3],
						'location': get_location_by_plz(row[3]) if row[3] else {'longitude': None,'latitude': None,},
						#'city': row[4],
						'brutto_power': float(row[5].replace(',', '.'))*1000,
						#'fernwarme_leistung': row[6],
						#'inbetriebnahme': row[7],
						#'anlagenart': row[8],
						'type': row[9],
					})
	return output_list



class Scenario:
	mobility = {}
	energy_sources = {}

	_energy_sources = []
	_automobiles = []
	_round_automobiles	= 10000

	def __init__(self, *args, **kwargs):
		self.__dict__.update(kwargs)
		self.set_mobility()
		self.set_energy()
	
	# ------------- Setters -------------

	def set_mobility(self):
		for type, num in self.mobility.items():
			for i in range(int(num/self._round_automobiles)):
				self._automobiles.append(
					getattr(mobility, type)()
				)

	def set_energy(self):
		for type, num in self.energy_sources.items():
			for i in range(num):
				self._energy_sources.append(
					getattr(energy.source, type)()
				)
	
	# ------------- Getters -------------

	def get_mobility_co2(self):
		co2 = 0
		for automobile in self._automobiles:
			co2 += automobile.get_yearly_emissions()
		return co2*self._round_automobiles
	
	def get_energy_co2(self):
		co2 = 0
		for source in self._energy_sources:
			co2 += source.get_yearly_co2_intensity()
		return co2

	def get_total_co2(self):
		return self.get_energy_co2()+self.get_mobility_co2()

	def get_total_energy_return(self):
		kwh = 0
		for source in self._energy_sources:
			kwh += source.get_yearly_energy_return()
		return kwh

	# ------------- Prints -------------

	def print_mobility_co2(self):
		return print_weight(
			self.get_mobility_co2()
		)
	
	def print_energy_co2(self):
		return print_weight(
			self.get_energy_co2()
		)
	
	def print_total_co2(self):
		return print_weight(
			self.get_total_co2()
		)
	
	def print_total_energy_return(self):
		return print_watt(
			self.get_total_energy_return()
		)


scenario = Scenario(
	mobility = {
		'AutomobilePetrol': 30451268,
		'AutomobileDiesel': 15225296,
		'AutomobileElectro': 83175,
	},
	_energy_sources = [
		*[getattr(energy.source, 'Braunkohle')(
			nominal_power=source['brutto_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Braunkohle')],

		*[getattr(energy.source, 'Steinkohle')(
			nominal_power=source['brutto_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Steinkohle')],
		
		*[getattr(energy.source, 'Erdgas')(
			nominal_power=source['brutto_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Erdgas')],

		*[getattr(energy.source, 'Windenergie')(
			nominal_power=source['brutto_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Wind')],

		*[getattr(energy.source, 'Wasserkraft')(
			nominal_power=source['brutto_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Wasser')],

		*[getattr(energy.source, 'Kernenergie')(
			nominal_power=source['brutto_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Uran')],

		*[getattr(energy.source, 'Photovoltaik')(
			nominal_power=source['brutto_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Licht')],

	]
)

print(scenario.print_mobility_co2())
print(scenario.print_energy_co2())
print(scenario.print_total_co2())
print(scenario.print_total_energy_return())

"""
https://www.kba.de/DE/Statistik/Fahrzeuge/Bestand/b_jahresbilanz.html
https://www.kba.de/DE/Statistik/Fahrzeuge/Bestand/Jahresbilanz/2018/2018_b_barometer.html?nn=2176778
https://www.umweltbundesamt.de/dokument/datenbank-kraftwerke-in-deutschland
"""

