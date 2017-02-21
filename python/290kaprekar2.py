# 10/31/2016 - Challenge 290 - Kaprekar Numbers
# https://www.reddit.com/r/dailyprogrammer/comments/5aemnn/20161031_challenge_290_easy_kaprekar_numbers/
#

import sys

if (len(sys.argv) != 3):
	print "Did not receive two arguments (" + str(len(sys.argv)) + ")"
	sys.exit()

for i in range(int(sys.argv[1]), int(sys.argv[2])):
	sq = str(i**2)
	if (int(sq) == i):
		print i,
		continue
	for j in range(1, len(sq)):
		if (int(sq[:j]) + int(sq[j:]) == i and int(sq[j:]) != 0):
			print i,
			break
