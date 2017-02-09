# 02/06/2017 - Challenge 302 - Spelling with Chemisty
# https://www.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/
#

import sys

elements = {
	"ac": "actinium", "al": "aluminum", "am": "americium", "sb": "antimony",
	"ar": "argon", "as": "arsenic", "at": "astatine", "ba": "barium",
	"bk": "berkelium", "be": "beryllium", "bi": "bismuth", "b": "boron",
	"br": "bromine", "cd": "cadmium", "ca": "calcium", "cf": "californium",
	"c": "carbon", "ce": "cerium", "cs": "cesium", "cl": "chlorine",
	"cr": "chromium", "co": "cobalt", "cu": "copper", "cm": "curium",
	"dy": "dysprosium", "es": "einsteinium", "er": "erbium", "eu": "europium",
	"fm": "fermium", "f": "fluorine", "fr": "francium", "gd": "gadolinium",
	"ga": "gallium", "ge": "germanium", "au": "gold", "hf": "hafnium",
	"he": "helium", "ho": "holmium", "h": "hydrogen", "in": "indium",
	"i": "iodine", "ir": "iridium", "fe": "iron", "kr": "krypton",
	"la": "lanthanum", "lr": "lawrencium", "pb": "lead", "li": "lithium",
	"lu": "lutetium", "mg": "magnesium", "mn": "manganese", "md": "mendelevium",
	"hg": "mercury", "mo": "molybdenum", "nd": "neodymium", "ne": "neon",
	"np": "neptunium", "ni": "nickel", "nb": "niobium", "n": "nitrogen",
	"no": "nobelium", "os": "osmium", "o": "oxygen", "pd": "palladium",
	"p": "phosphorus", "pt": "platinum", "pu": "plutonium", "po": "polonium",
	"k": "potassium", "pr": "praseodymium", "pm": "promethium", "pa": "protactinium",
	"ra": "radium", "rn": "radon", "re": "rhenium", "rh": "rhodium",
	"rb": "rubidium", "ru": "ruthenium", "rf": "rutherfordium", "sm": "samarium",
	"sc": "scandium", "se": "selenium", "si": "silicon", "ag": "silver",
	"na": "sodium", "sr": "strontium", "s": "sulfur", "ta": "tantalum",
	"tc": "technetium", "te": "tellurium", "tb": "terbium", "tl": "thallium",
	"th": "thorium", "tm": "thulium", "sn": "tin", "ti": "titanium",
	"w": "tungsten", "u": "uranium", "v": "vanadium", "xe": "xenon",
	"yb": "ytterbium", "y": "yttrium", "zn": "zinc", "zr": "zirconium"
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

def print_res(pairs):
	names = []
	s = ""
	for pair in res:
		names.append(pair[1])
		s += pair[0].capitalize()
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