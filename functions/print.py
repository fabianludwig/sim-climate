def print_watt(menge_in_kw):
	if menge_in_kw > (1000*1000*1000):
		return "{} TWh".format(
			round(menge_in_kw/(1000*1000*1000), 2)
		)
	
	if menge_in_kw > (1000*1000):
		return "{} GWh".format(
			round(menge_in_kw/(1000*1000), 2)
		)

	if menge_in_kw > 1000:
		return "{} MWh".format(
			round(menge_in_kw/1000, 2)
		)
	
	return "{} kWh".format(
		round(menge_in_kw, 2)
	)


def print_money(euro):
	if euro > (1000*1000*1000):
		return "{} Mrd. €".format(
			round(euro/(1000*1000*1000), 2)
		)
	
	if euro > (1000*1000):
		return "{} Mio. €".format(
			round(euro/(1000*1000), 2)
		)

	if euro > 1000:
		return "{} Tsd. €".format(
			round(euro/1000, 2)
		)
	
	return "{} €".format(
		round(euro, 2)
	)


def print_weight(gramm):
	if gramm > (1000*1000*1000*1000):
		return "{} Mio. t".format(
			round(gramm/(1000*1000*1000*1000), 2)
		)

	if gramm > (1000*1000*1000):
		return "{} Tsd. t".format(
			round(gramm/(1000*1000*1000), 2)
		)
  
	if gramm > (1000*1000):
		return "{} t".format(
			round(gramm/(1000*1000), 2)
		)

	if gramm > 1000:
		return "{} kg".format(
			round(gramm/1000, 2)
		)
	
	return "{} g".format(
		round(gramm, 2)
	)


def print_months(months):
	years 	= int(months/12)
	months 	= months%12

	string = ''

	if years > 0:
		string += str(years)+' Jahre'
		if months > 0:
			string += ', '
	
	if months > 1:
		string += str(round(months))+' Monate'
	else:
		string += str(round(months))+' Monat'

	return string