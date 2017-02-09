# 02/06/2017 - Challenge 302 - Spelling with Chemisty
# https://www.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/
#

import sys

elements = {
	("actinium", "ac", 227), ("aluminum", "al", 26.9815), ("americium", "am", 243),
	("antimony", "sb", 121.75), ("argon", "ar", 39.948), ("arsenic", "as", 74.9216),
	("astatine", "at", 210), ("barium", "ba", 137), ("berkelium", "bk", 247),
	("beryllium", "be", 9.0122), ("bismuth", "bi", 208.98), ("boron", "b", 10.81),
	("bromine", "br", 79.904), ("cadmium", "cd", 112.4), ("calcium", "ca", 40.08),
	("californium", "cf", 251), ("carbon", "c", 12.011), ("cerium", "ce", 140.12),
	("cesium", "cs", 132.9054), ("chlorine", "cl", 35.453), ("chromium", "cr", 51.996),
	("cobalt", "co", 58.9332), ("copper", "cu", 63.546), ("curium", "cm", 247),
	("dysprosium", "dy", 162.5), ("einsteinium", "es", 254), ("erbium", "er", 167.26),
	("europium", "eu", 151.96), ("fermium", "fm", 257), ("fluorine", "f", 18.9984),
	("francium", "fr", 223), ("gadolinium", "gd", 157.25), ("gallium", "ga", 69.72),
	("germanium", "ge", 72.59), ("gold", "au", 196.966), ("hafnium", "hf", 178.49),
	("helium", "he", 4.0026), ("holmium", "ho", 164.93), ("hydrogen", "h", 1.0079),
	("indium", "in", 114.82), ("iodine", "i", 126.904), ("iridium", "ir", 192.22),
	("iron", "fe", 55.847), ("krypton", "kr", 83.8), ("lanthanum", "la", 138.905),
	("lawrencium", "lr", 256), ("lead", "pb", 207.2), ("lithium", "li", 6.941),
	("lutetium", "lu", 174.97), ("magnesium", "mg", 24.305), ("manganese", "mn", 54.938),
	("mendelevium", "md", 258), ("mercury", "hg", 200.59), ("molybdenum", "mo", 95.94),
	("neodymium", "nd", 144.24), ("neon", "ne", 20.179), ("neptunium", "np", 237.048),
	("nickel", "ni", 58.7), ("niobium", "nb", 92.9064), ("nitrogen", "n", 14.0067),
	("nobelium", "no", 255), ("osmium", "os", 190.2), ("oxygen", "o", 15.9994),
	("palladium", "pd", 106.4), ("phosphorus", "p", 30.9738), ("platinum", "pt", 195.09),
	("plutonium", "pu", 244), ("polonium", "po", 210), ("potassium", "k", 39.098),
	("praseodymium", "pr", 140.908), ("promethium", "pm", 147), ("protactinium", "pa", 231.036),
	("radium", "ra", 226.025), ("radon", "rn", 222), ("rhenium", "re", 186.207),
	("rhodium", "rh", 102.906), ("rubidium", "rb", 85.4678), ("ruthenium", "ru", 101.07),
	("rutherfordium", "rf", 261), ("samarium", "sm", 150.4), ("scandium", "sc", 44.9559),
	("selenium", "se", 78.96), ("silicon", "si", 28.086), ("silver", "ag", 107.868),
	("sodium", "na", 22.9898), ("strontium", "sr", 87.62), ("sulfur", "s", 32.06),
	("tantalum", "ta", 180.948), ("technetium", "tc", 98.9062), ("tellurium", "te", 127.6),
	("terbium", "tb", 158.925), ("thallium", "tl", 204.37), ("thorium", "th", 232.038),
	("thulium", "tm", 168.934), ("tin", "sn", 118.69), ("titanium", "ti", 47.9),
	("tungsten", "w", 183.85), ("uranium", "u", 238.029), ("vanadium", "v", 50.9414),
	("xenon", "xe", 131.3), ("ytterbium", "yb", 173.04), ("yttrium", "y", 88.9059),
	("zinc", "zn", 65.38), ("zirconium", "zr", 91.22)
}

def build(word):
	if (word == ''):
		return []
	try:
		el = word[0:1]
		name = elements[el]
		res = build(word[1:])
		if (type(res) is list):
			res.insert(0, (el, name))	
			return res
	except KeyError:
		pass
	if (len(word) < 2):
		return 0
	try:
		el = word[0:2]
		name = elements[el]
		res = build(word[2:])
		if (type(res) is list):
			res.insert(0, (el, name))
			return res
	except KeyError:
		pass
	return 0

def print_res(tuples):
	names = []
	s = ""
	for t in tuples:
		names.append(t[1])
		s += t[0].capitalize()
	print s,
	s = "("
	for i in range(len(names)-1):
		s += names[i] + ", "
	s += names[len(names)-1] + ")"
	print s

res = build(sys.argv[1].lower())
if (type(res) is int):
	print "Unable to build a word"
	sys.exit()
print_res(res)