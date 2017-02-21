# 02/06/2017 - Challenge 302 - Spelling with Chemisty (with bonus)
# https://www.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/
#

import sys

elements = {
	"ac": ("actinium", 227), "al": ("aluminum", 26.9815), "am": ("americium", 243),
	"sb": ("antimony", 121.75), "ar": ("argon", 39.948), "as": ("arsenic", 74.9216),
	"at": ("astatine", 210), "ba": ("barium", 137), "bk": ("berkelium", 247),
	"be": ("beryllium", 9.0122), "bi": ("bismuth", 208.98), "b": ("boron", 10.81),
	"br": ("bromine", 79.904), "cd": ("cadmium", 112.4), "ca": ("calcium", 40.08),
	"cf": ("californium", 251), "c": ("carbon", 12.011), "ce": ("cerium", 140.12),
	"cs": ("cesium", 132.9054), "cl": ("chlorine", 35.453), "cr": ("chromium", 51.996),
	"co": ("cobalt", 58.9332), "cu": ("copper", 63.546), "cm": ("curium", 247),
	"dy": ("dysprosium", 162.5), "es": ("einsteinium", 254), "er": ("erbium", 167.26),
	"eu": ("europium", 151.96), "fm": ("fermium", 257), "f": ("fluorine", 18.9984),
	"fr": ("francium", 223), "gd": ("gadolinium", 157.25), "ga": ("gallium", 69.72),
	"ge": ("germanium", 72.59), "au": ("gold", 196.966), "hf": ("hafnium", 178.49),
	"he": ("helium", 4.0026), "ho": ("holmium", 164.93), "h": ("hydrogen", 1.0079),
	"in": ("indium", 114.82), "i": ("iodine", 126.904), "ir": ("iridium", 192.22),
	"fe": ("iron", 55.847), "kr": ("krypton", 83.8), "la": ("lanthanum", 138.905),
	"lr": ("lawrencium", 256), "pb": ("lead", 207.2), "li": ("lithium", 6.941),
	"lu": ("lutetium", 174.97), "mg": ("magnesium", 24.305), "mn": ("manganese", 54.938),
	"md": ("mendelevium", 258), "hg": ("mercury", 200.59), "mo": ("molybdenum", 95.94),
	"nd": ("neodymium", 144.24), "ne": ("neon", 20.179), "np": ("neptunium", 237.048),
	"ni": ("nickel", 58.7), "nb": ("niobium", 92.9064), "n": ("nitrogen", 14.0067),
	"no": ("nobelium", 255), "os": ("osmium", 190.2), "o": ("oxygen", 15.9994), "pd": ("palladium", 106.4),
	"p": ("phosphorus", 30.9738),  "pt": ("platinum", 195.09), "pu": ("plutonium", 244),
	"po": ("polonium", 210), "k": ("potassium", 39.098), "pr": ("praseodymium", 140.908),
	"pm": ("promethium", 147), "pa": ("protactinium", 231.036), "ra": ("radium", 226.025),
	"rn": ("radon", 222), "re": ("rhenium", 186.207), "rh": ("rhodium", 102.906),
	"rb": ("rubidium", 85.4678), "ru": ("ruthenium", 101.07), "rf": ("rutherfordium", 261),
	"sm": ("samarium", 150.4), "sc": ("scandium", 44.9559), "se": ("selenium", 78.96),
	"si": ("silicon", 28.086), "ag": ("silver", 107.868), "na": ("sodium", 22.9898),
	"sr": ("strontium", 87.62), "s": ("sulfur", 32.06), "ta": ("tantalum", 180.948),
	"tc": ("technetium", 98.9062), "te": ("tellurium", 127.6), "tb": ("terbium", 158.925),
	"tl": ("thallium", 204.37), "th": ("thorium", 232.038), "tm": ("thulium", 168.934),
	"sn": ("tin", 118.69), "ti": ("titanium", 47.9), "w": ("tungsten", 183.85),
	"u": ("uranium", 238.029), "v": ("vanadium", 50.9414), "xe": ("xenon", 131.3),
	"yb": ("ytterbium", 173.04), "y": ("yttrium", 88.9059), "zn": ("zinc", 65.38),
	"zr": ("zirconium", 91.22)
}

def build(word):
	if (word == ''):
		return [[], 0]
	res = 0
	two = 0
	one = 0
	if (len(word) > 1):
		try:
			el = word[0:2]
			name = (elements[el])[0]
			weight = (elements[el])[1]
			two = build(word[2:])
			if (type(two) is list):
				two[0].insert(0, (el, name))
				two[1] += weight
		except KeyError:
			pass
	try:
		el = word[0:1]
		name = (elements[el])[0]
		weight = (elements[el])[1]
		one = build(word[1:])
		if (type(one) is list):
			one[0].insert(0, (el, name))
			one[1] += weight
	except KeyError:
		pass
	if (type(two) is list and type(one) is list):
		if (one[1] > two[1]):
			res = one
			del two
		else:
			res = two
			del one
	elif (type(two) is list):
		res = two
	else:
		res = one
	return res

def print_res(res):
	tuples = res[0]
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
	print s,
	print "[" + str(res[1]) + "]"

res = build(sys.argv[1].lower())
if (type(res) is int):
	print "Unable to build a word"
	sys.exit()
print_res(res)