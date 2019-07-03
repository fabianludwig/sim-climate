# -*- coding: utf-8 -*-

import os, csv
import pprint

from functions.print import *
from models import energy, geography, mobility, resources




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
	file_path = './data/countries/'+country+'/Kraftwerksliste_CSV.csv'
	if os.path.isfile(file_path):
		with open(file_path, 'r') as file:
			reader = csv.reader(file, delimiter =';')
			for row in reader:
				if not filter or filter in row[10]:
					nominal_power = float(row[16].replace('.', '').replace(',', '.'))*1000
					if nominal_power > 0 and 'Vorläufig Stillgelegt' not in row[9] and 'Endgültig Stillgelegt' not in row[9]:
						output_list.append({
							'name': row[2],
							'betreiber': row[1],
							#'bundesland': row[2],
							'plz': row[3],
							'location': get_location_by_plz(row[3]) if row[3].isdecimal() else {'longitude': None,'latitude': None,},
							#'city': row[4],
							'nominal_power': nominal_power,
							#'fernwarme_leistung': row[6],
							#'inbetriebnahme': row[7],
							#'anlagenart': row[8],
							'type': row[10],
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
		co2 = {
			'by_type': dict(),
			'total': 0
		}
		for automobile in self._automobiles:
			type = automobile.__class__.__name__
			if type not in co2['by_type']:
				co2['by_type'][type] = 0
			co2['by_type'][type] += automobile.get_yearly_emissions()*self._round_automobiles
			co2['total'] += automobile.get_yearly_emissions()*self._round_automobiles
		return co2
	
	def get_energy_co2(self):
		co2 = {
			'by_type': dict(),
			'total': 0
		}
		for source in self._energy_sources:
			type = source.__class__.__name__
			if type not in co2['by_type']:
				co2['by_type'][type] = 0
			co2['by_type'][type] += source.get_yearly_co2_intensity()
			co2['total'] += source.get_yearly_co2_intensity()
		return co2

	def get_energy_return(self):
		kwh = {
			'by_type': dict(),
			'total': 0
		}
		for source in self._energy_sources:
			type = source.__class__.__name__
			if type not in kwh['by_type']:
				kwh['by_type'][type] = 0
			kwh['by_type'][type] += source.get_yearly_energy_return()
			kwh['total'] += source.get_yearly_energy_return()
		return kwh
	
	def get_total_co2(self):
		return self.get_energy_co2()['total']+self.get_mobility_co2()['total']


	# ------------- Prints -------------

	def print_mobility_co2(self):
		mobility_co2 = self.get_mobility_co2()
		for type, sum in mobility_co2['by_type'].items():
			mobility_co2['by_type'][type] = print_weight(sum)
		mobility_co2['total'] = print_weight(mobility_co2['total'])
		return mobility_co2
	
	def print_energy_co2(self):
		energy_co2 = self.get_energy_co2()
		for type, sum in energy_co2['by_type'].items():
			energy_co2['by_type'][type] = print_weight(sum)
		energy_co2['total'] = print_weight(energy_co2['total'])
		return energy_co2
	
	def print_total_co2(self):
		return print_weight(
			self.get_total_co2()
		)
	
	def print_energy_return(self):
		energy_return = self.get_energy_return()
		for type, sum in energy_return['by_type'].items():
			energy_return['by_type'][type] = print_watt(sum)
		energy_return['total'] = print_weight(energy_return['total'])
		return energy_return


scenario = Scenario(
	mobility = {
		'AutomobilePetrol': 30451268,
		'AutomobileDiesel': 15225296,
		'AutomobileElectro': 83175,
		#'AutomobileTruck': 218454,
	},
	_energy_sources = [
		*[getattr(energy.source, 'Braunkohle')(
			nominal_power=source['nominal_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Braunkohle')],

		*[getattr(energy.source, 'Steinkohle')(
			nominal_power=source['nominal_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Steinkohle')],
		
		*[getattr(energy.source, 'Erdgas')(
			nominal_power=source['nominal_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Erdgas')],

		*[getattr(energy.source, 'Kernenergie')(
			nominal_power=source['nominal_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Kernenergie')],

		*[getattr(energy.source, 'Photovoltaik')(
			nominal_power=source['nominal_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Solare Strahlungsenergie')],

		*[getattr(energy.source, 'Windenergie')(
			nominal_power=source['nominal_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Windenergie')],

		*[getattr(energy.source, 'Wasserkraft')(
			nominal_power=source['nominal_power'],
			longitude=source['location']['longitude'],
			latitude=source['location']['latitude'],
		) for source in get_plants(filter='Laufwasser')],

	]
)

pp = pprint.PrettyPrinter(indent=2)

pp.pprint(scenario.print_mobility_co2())
pp.pprint(scenario.print_energy_co2())
pp.pprint(scenario.print_total_co2())
pp.pprint(scenario.print_energy_return())

"""
https://www.kba.de/DE/Statistik/Fahrzeuge/Bestand/b_jahresbilanz.html
https://www.kba.de/DE/Statistik/Fahrzeuge/Bestand/Jahresbilanz/2018/2018_b_barometer.html?nn=2176778
https://www.umweltbundesamt.de/dokument/datenbank-kraftwerke-in-deutschland
"""

