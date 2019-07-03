# -*- coding: utf-8 -*-

from ._base_ import *


# ------------ Kraftstoffe ------------

class Benzin(CombustibleFluid):
	dichte					= 747.5   	# 0,72–0,775 (https://www.chemie.de/lexikon/Benzin.html)
	brennwert				= 12		# (https://www.chemie.de/lexikon/Benzin.html)
	combustion_co2_per_l	= 2360		# (https://www.chemie.de/lexikon/Benzin.html)
	
	expense_per_l			= 1.5


class Autogas(CombustibleFluid):
	brennwert 				= 12.8		# (https://www.chemie.de/lexikon/Autogas.html)
	
	dichte					= 535   	# 0,51-0,56 (https://www.chemie.de/lexikon/Autogas.html)
	combustion_co2_per_l	= 1980		# (https://www.chemie.de/lexikon/Autogas.html)
	
	expense_per_l			= 0.67


class Kerosin(CombustibleFluid):
	brennwert_per_l			= 9.5		# (https://www.chemie.de/lexikon/Kerosin.html)
	combustion_co2_per_g	= 2.76		# (https://www.chemie.de/lexikon/Kerosin.html)
	dichte					= 793.5   	# (https://www.chemie.de/lexikon/Kerosin.html)


class Diesel(CombustibleFluid):
	dichte					= 830		# (https://www.chemie.de/lexikon/Dieselkraftstoff.html)
	combustion_co2_per_l	= 2650		# (https://www.chemie.de/lexikon/Dieselkraftstoff.html)
	brennwert_per_l			= 9.8		# (https://www.chemie.de/lexikon/Dieselkraftstoff.html)
	production_kwh_per_l	= 7			# (https://www.springerprofessional.de/elektromobilitaet/dieselmotor/endenergiebezogene-analyse-diesel-versus-elektromobilitaet/16673694)

	expense_per_l			= 1.25
	

class Biodiesel(Diesel):
	dichte					= 840   	# 0,81–0,87 (https://www.chemie.de/lexikon/Rapsdiesel.html)
	brennwert_per_l			= 9.5		# (https://www.chemie.de/lexikon/Rapsdiesel.html)

	def get_expense(self):
		# (https://www.spritmonitor.de/de/alternative_biodiesel.html)
		return super().get_expense()-0.09 
	
	def get_combustion_co2_per_g(self):
		# (https://www.spritmonitor.de/de/alternative_biodiesel.html)
		return super().get_combustion_co2_per_g()*0.25 


class Erdgas(CombustibleFluid):
	brennwert				= 12		# 10-14 (https://www.chemie.de/lexikon/Erdgas.html)
	combustion_co2_per_g	= 2.79		# (https://www.spritmonitor.de/de/berechnung_co2_ausstoss.html)
	dichte					= 770		# 0,70-0,84 (https://www.chemie.de/lexikon/Erdgas.html)
	
	expense					= 0.7


# ------------ Brennstoffe ------------


class Heizoel(CombustibleFluid):
	brennwert				= 11.86		# (http://www.biobrennstoffhof.de/leistung.htm)
	combustion_co2_per_l	= 2650		# (https://de.wikipedia.org/wiki/Heiz%C3%B6l)
	dichte					= 840		


class Braunkohle(Combustible):
	brennwert				= 5.9		# (https://www.umweltbundesamt.de/sites/default/files/medien/1968/publikationen/co2-emissionsfaktoren_fur_fossile_brennstoffe_korrektur.pdf)
	combustion_co2_per_g	= 2.12		# (https://www.volker-quaschning.de/datserv/CO2-spez/index.php)


class Steinkohle(Combustible):
	brennwert				= 7.0		# (http://www.biobrennstoffhof.de/leistung.htm)
	combustion_co2_per_g	= 2.38		# (https://www.volker-quaschning.de/datserv/CO2-spez/index.php)


class Fluessiggas(CombustibleFluid):
	brennwert				= 12.9		# (https://www.chemie.de/lexikon/Fl%C3%BCssiggas.html)
	dichte					= 540		# (https://www.chemie.de/lexikon/Fl%C3%BCssiggas.html)

	def get_combustion_co2_per_kwh(self):
		# (https://www.volker-quaschning.de/datserv/CO2-spez/index.php)
		return 0.23*1000	



class Holz(Combustible):
	brennwert				= 4.9		# (http://www.biobrennstoffhof.de/leistung.htm)

	def get_combustion_co2_per_kwh(self):
		# (https://www.volker-quaschning.de/datserv/CO2-spez/index.php)
		return 0.39*1000	


class Torf(Combustible):
	def get_combustion_co2_per_kwh(self):
		# (https://www.volker-quaschning.de/datserv/CO2-spez/index.php)
		return 0.38*1000	


class Rohoel(CombustibleFluid):
	def get_combustion_co2_per_kwh(self):
		# (https://www.volker-quaschning.de/datserv/CO2-spez/index.php)
		return 0.26*1000	


class Raffineriegas(CombustibleFluid):
	def get_combustion_co2_per_kwh(self):
		# (https://www.volker-quaschning.de/datserv/CO2-spez/index.php)
		return 0.24*1000	


class Naturgas(CombustibleFluid):
	def get_combustion_co2_per_kwh(self):
		# (https://www.volker-quaschning.de/datserv/CO2-spez/index.php)
		return 0.20*1000	


class Haushaltsmuell(Combustible):
	brennwert				= 2.5		# (http://www.biobrennstoffhof.de/leistung.htm)

