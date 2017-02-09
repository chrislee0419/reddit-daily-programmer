# 11/15/2016 - Challenge 292 - Increasing range parsing
# https://www.reddit.com/r/dailyprogrammer/comments/5d1l7v/20161115_challenge_292_easy_increasing_range/
#

import sys

def split_string(str):
	tokens = []
	s = ''
	for i in range(len(str)):
		if (str[i] == ','):
			tokens.append(s)
			s = ''
		else:
			s += str[i]
	tokens.append(s)
	return tokens

def digest(tok):
	if ('-' in tok):
		sep = '-'
	elif (':' in tok):
		sep = ':'
	elif ('..' in tok):
		sep = '..'
	else:
		return [tok, tok, 1]
	p = tok.find(sep)
	first = tok[0:p]
	second = tok[p+len(sep):]
	third = 1
	if (sep in second):
		p = tok.find(sep)
		third = int(second[p+len(sep):])
		second = second[0:p]
	return [first, second, third]

def print_from_token(num, token):
	r = digest(token)
	while (len(str(num)) < len(r[0])):
		num += 1
	while (r[0] != str(num)[len(str(num))-len(r[0]):]):
		num += 1
	while (r[1] != str(num)[len(str(num))-len(r[1]):]):
		print str(num),
		for i in range(r[2]-1):
			num += 1
			if (r[1] == str(num)[len(str(num))-len(r[1]):]):
				return num + 1
		num += 1
	print str(num),
	return num + 1

ranges = split_string(sys.argv[1])
num = 0
for r in ranges:
	num = print_from_token(num, r)