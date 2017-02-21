# 01/02/2017 - Challenge 298 - Too many Parentheses (with bonus)
# https://www.reddit.com/r/dailyprogrammer/comments/5llkbj/2017012_challenge_298_easy_too_many_parentheses/
#

import sys

def check_parentheses(string):
	parens = []
	new_string = ""
	for c in range(len(string)):
		if (len(parens) == 0 and string[c] != "(" and string[c] != ")"):
			new_string += string[c]
		elif (string[c] == "("):
			parens.append(c)
		elif (string[c] == ")"):
			begin = parens.pop() + 1
			if (begin != c and len(parens) == 0):
				s = check_parentheses(string[begin:c])
				if (len(s) == 0): pass
				elif (s[0] == "(" and s[-1] == ")"):
					parens_check = []
					for i in range(len(s)-1):
						if (s[i] == "("): parens_check.append(i)
						elif (s[i] == ")"): parens_check.pop()
					if (parens_check[0] == 0): new_string += s
					else: new_string += "(" + s + ")"
				else: new_string += "(" + s + ")"
	return new_string

print check_parentheses(sys.argv[1])