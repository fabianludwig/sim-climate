# -*- coding: utf-8 -*-

class Energiespeicher:
	wirkungsgrad 	= 0 # in %
	kapazitaet		= 0 # in kWh
	kosten_eur		= 0	
	kosten_co2		= 0 # in Gramm


class Pumpspeicherkraftwerke(Energiespeicher):
	wirkungsgrad	= 0

class PowerToGas(Energiespeicher):
	wirkungsgrad 	= 42.5 # 35-50 (001_Quaschning)

class Batteriespeicher(Energiespeicher):
	pass


"""
Quellen:
001_Quaschning: https://www.youtube.com/watch?v=CE-6jsWCATk

"""