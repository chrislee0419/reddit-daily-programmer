# 10/10/2016 - Challenge 287 - Kaprekar's Routine
# https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/
#

import sys

def check(num):
	if (num < 0 or num > 9999):
		print "Did not receive a positive number with at most 4 digits"
		return 0
	else: return 1

def concat_zeroes(num):
	if (num < 10): return "000" + str(num)
	elif (num < 100): return "00" + str(num)
	elif (num < 1000): return "0" + str(num)
	else: return str(num)

def largest_digit(num):
	num = str(num)

	res = 0
	for i in range(0, len(num)):
		if (int(num[i]) > res): res = int(num[i])
	return res

def desc_digits(num):
	num = concat_zeroes(num)

	l = [num[0], num[1], num[2], num[3]]
	l.sort()
	l.reverse()
	return int(''.join(l))

def kaprekar(num):
	count = 0
	desc = desc_digits(num)
	desc_str = concat_zeroes(desc)
	asc = int(desc_str[3] + desc_str[2] + desc_str[1] + desc_str[0])
	prev = 0

	while (desc - asc != prev and num != 6174):
		count += 1
		prev = num
		num = desc - asc
		desc = desc_digits(num)
		desc_str = str(desc)
		asc = int(desc_str[3] + desc_str[2] + desc_str[1] + desc_str[0])
	return count

def max_iter_kaprekar():
	it = 0
	for i in range(0, 10000):
		k = kaprekar(i)
		if (k > it): it = k
	return it

num = int(sys.argv[1])
if (not check(num)): sys.exit()
print "Largest Digit:", largest_digit(num)
print "Descending Order:", desc_digits(num)
print "Kaprekar Iterations:", kaprekar(num)
print "\nMost Kaprekar Iterations:", max_iter_kaprekar()

