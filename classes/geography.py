# -*- coding: utf-8 -*-

import math

from globals import *
from functions.print import *

from .energy.energysources import *
from .consumers import *



class Area(Location):
	einwohner				= 10000
	energysources			= []

	price_per_kwh_wind		= 5.2925	# in cents (006_SWEWindenergie)
	price_per_kwh_solar		= 11.47		# in cents

	def __init__(self, *args, **kwargs):
		self.set_energysources()
		super().__init__(*args, **kwargs)
	
	def set_energysources(self, *args, **kwargs):
		pass


class Geography:
	einwohner 				= 10000
	haushalte_einzel		= 5000

	flaeche_sqm				= 50
	location_latitude		= 0
	location_longitude		= 0
	location_altitude		= 0

	wind_nennleistung_kw 	= 0
	solar_nennleistung_kw 	= 0

	def __init__(self):
		self.haushalt				= Haushalt()
		self.haushalt_einzel		= EinPersonenHaushalt()
		self.haushalt_mehrpersonen	= MehrPersonenHaushalt()
		self.industrie				= Industry()
		self.gewerbe				= Gewerbe()

		self.windenergie			= Windenergie()
		self.photovoltaik			= Photovoltaik()

	def print_results(self):
		print("\
				{} Strom/Jahr \n\
				{} Strom/Jahr für Haushalte	\n\
				\n\
				{} Strom aus Windkraft \n\
				{} Strom aus Solarenergie \n\
				\n\
				{} Kosten für Strom/Jahr \n\
				{} Kosten für Strom/Jahr für Haushalte \n\
				\n\
				{} benötigte Windräder \n\
				{} Windräder noch zu bauen \n\
				{} Kosten für Windräder \n\
				{} Jahre \n\
				\n\
				{} Kosten pro Haushalt \n\
			".format(
				print_watt( self.verbrauch_jahr_kwh() ),
				print_watt( self.verbrauch_haushalte_jahr_kwh() ),
				print_watt( self.wind_leistung_jahr_kw() ),
				print_watt( self.solar_leistung_jahr_kw() ),
				print_money( self.jahreskosten_in_eur() ),
				print_money( self.jahreskosten_haushalte_in_eur() ),
				self.windraeder_benoetigt(),
				self.windraeder_noch_zu_bauen(),
				print_money( self.windraeder_kosten() ),
				self.windraeder_amortisiert_nach(),
				print_money( self.windraeder_kosten_pro_haushalt() ),
			)
		)
	
	def haushalte_mehrpersonen(self):
		return (self.einwohner - self.haushalte_einzel) / self.haushalt_mehrpersonen.persons

	def haushalte(self):
		return self.haushalte_einzel + self.haushalte_mehrpersonen()
	
	def wind_nennleistung_jahr_kw(self):
		return self.wind_nennleistung_kw * 24 * 365.25
	
	def wind_leistung_jahr_kw(self):
		return self.wind_nennleistung_jahr_kw() * self.windenergie.get_efficiency()
	
	def solar_nennleistung_jahr_kw(self):
		return self.solar_nennleistung_kw * 24 * 365.25
	
	def solar_leistung_jahr_kw(self):
		return self.solar_nennleistung_jahr_kw() * self.photovoltaik.get_efficiency()
	
	# -------------- Energie --------------

	def verbrauch_jahr_kwh(self):
		return self.verbrauch_haushalte_jahr_kwh() + self.verbrauch_industrie_jahr_kwh() + self.verbrauch_gewerbe_jahr_kwh()
	
	def jahreskosten_in_eur(self):
		return self.jahreskosten_haushalte_in_eur() + self.jahreskosten_industrie_in_eur() + self.jahreskosten_gewerbe_in_eur()

	def verbrauch_industrie_jahr_kwh(self):
		return self.industrie.verbrauch_jahr_kwh()

	def jahreskosten_industrie_in_eur(self):
		return self.industrie.jahreskosten_in_eur()
	
	def verbrauch_gewerbe_jahr_kwh(self):
		return self.gewerbe.verbrauch_jahr_kwh()

	def jahreskosten_gewerbe_in_eur(self):
		return self.gewerbe.jahreskosten_in_eur()

	def verbrauch_haushalte_jahr_kwh(self):
		haushalte_einzel = self.haushalt_einzel.verbrauch_jahr_kwh() * self.haushalte_einzel
		haushalte_mehrpersonen = self.haushalt_mehrpersonen.verbrauch_jahr_kwh() * self.haushalte_mehrpersonen()
		return haushalte_einzel + haushalte_mehrpersonen

	def jahreskosten_haushalte_in_eur(self):
		haushalte_einzel = self.haushalt_einzel.jahreskosten_in_eur() * self.haushalte_einzel
		haushalte_mehrpersonen = self.haushalt_mehrpersonen.jahreskosten_in_eur() * self.haushalte_mehrpersonen()
		return haushalte_einzel + haushalte_mehrpersonen
	
	def ertrag_erneuerbare_jahr_kw(self):
		return self.wind_leistung_jahr_kw() + self.solar_leistung_jahr_kw()

	# -------------- Windkraft --------------

	def windraeder_benoetigt(self):
		return math.ceil(
			self.verbrauch_jahr_kwh() / self.windenergie.yearly_return()
		)
		
	def windraeder_noch_zu_bauen(self):
		return math.ceil(
			(self.verbrauch_jahr_kwh() - self.ertrag_erneuerbare_jahr_kw()) / self.windenergie.yearly_return()
		)

	def windraeder_kosten(self):
		return self.windraeder_noch_zu_bauen() * self.windenergie.expense
		
	def windraeder_ertrag_jahr_kwh(self):
		return self.windraeder_benoetigt() * self.windenergie.yearly_return()

	def windraeder_amortisiert_nach(self):
		ueberschuss_pro_jahr = self.windraeder_ertrag_jahr_kwh() - self.verbrauch_jahr_kwh()
		einspeiseverguetung_pro_jahr = (ueberschuss_pro_jahr * self.windenergie.einspeiseverguetung_cent) / 100
		return self.windraeder_kosten() / (self.jahreskosten_in_eur()+einspeiseverguetung_pro_jahr)
	
	def windraeder_kosten_pro_haushalt(self):
		prozentsatz = self.verbrauch_haushalte_jahr_kwh() / self.verbrauch_jahr_kwh()
		return (self.windraeder_kosten()*prozentsatz) / self.haushalte()
	


class Stadt(Geography):
	einwohner 			= 10000
	flaeche_sqm			= 50

	location_latitude	= 0
	location_longitude	= 0
	location_altitude	= 0



class Bundesland(Geography):
	einwohner 			= 10000000
	flaeche_sqm			= 50000

	location_latitude	= 0
	location_longitude	= 0
	location_altitude	= 0



class Country(Geography):
	einwohner 			= 10000000
	flaeche_sqm			= 50000

	location_latitude	= 0
	location_longitude	= 0
	location_altitude	= 0

	einspeiseverguetung_cent_windenergie	= 4.38
	einspeiseverguetung_cent_solarenergie	= 10.64