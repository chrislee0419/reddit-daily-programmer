# 03/06/17 - Challenge 305 - Permutation Base
# https://www.reddit.com/r/dailyprogrammer/comments/5xu7sz/20170306_challenge_305_easy_permutation_base/
#
# Usage: (base) [inv] (value)
#

import sys
import math

def index_to_value(base, index):
	length = 1
	i = 1
	while index >= math.pow(base, i):
		index -= int(math.pow(base, i))
		length += 1
		i += 1
	string = ""
	while (index > 0):
		string = str(index % base) + string
		index -= index % base
		index /= base
	string = "0" * int(length - len(string)) + string
	print string

def value_to_index(base, value):
	index = 0
	for j in range(len(value)-1):
		index += int(math.pow(base, j+1))
	i = 0
	while (len(value) > 0):
		index += int(value[-1]) * int(math.pow(base, i))
		value = value[:-1]
		i += 1
	print index
	
if (int(sys.argv[1]) > 1 and int(sys.argv[1]) < 11):
	if (len(sys.argv) == 3):
		index_to_value(int(sys.argv[1]), int(sys.argv[2]))
	elif (len(sys.argv) == 4 and sys.argv[2] == "inv"):
		value_to_index(int(sys.argv[1]), sys.argv[3])