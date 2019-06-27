def print_watt(menge_in_kw):
	if menge_in_kw > (1000*1000*1000):
		return "{} TW".format(
			round(menge_in_kw/(1000*1000*1000), 2)
		)
	
	if menge_in_kw > (1000*1000):
		return "{} GW".format(
			round(menge_in_kw/(1000*1000), 2)
		)

	if menge_in_kw > 1000:
		return "{} MW".format(
			round(menge_in_kw/1000, 2)
		)
	
	return "{} KW".format(
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
	if gramm > (1000*1000*1000):
		return "{} Mio. t".format(
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