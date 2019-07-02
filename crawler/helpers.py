import re

def clean_number(string):
	string = string.replace('.', '')
	string = string.replace(',', '.')
	string = "".join([c for c in string if c.isdecimal() or c=='.'])
	if len(string) > 0:
		return float(string)
	else:
		return None

def save_classname(string):
	string = "".join([c for c in string if c.isalpha() or c.isdecimal()])
	return string[0].upper() + string[1:]

def clean_number_and_get_avg(string):
	numbers = [float("".join([c for c in s if c.isdecimal() or c=='.'])) for s in re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", string)]
	if len(numbers) > 0:
		return float(sum(numbers))/len(numbers)
	else:
		return None