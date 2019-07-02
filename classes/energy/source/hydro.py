# -*- coding: utf-8 -*-

from ._base_ import EnergySource
from helpers.abstract import Producible


class Wasserkraft(EnergySource):
	# https://de.wikipedia.org/wiki/Liste_von_Wasserkraftwerken_in_Deutschland
	co2_intensity				= 22 	# 4-40 (001_Bundestag_Bilanzen)
	lifespan					= 100 	# (001_Bundestag_Bilanzen)