# 02/08/2017 - Challenge 302 - ASCII Bar Chart
# https://www.reddit.com/r/dailyprogrammer/comments/5st2so/20170208_challenge_302_intermediate_ascii/
#
# Usage:
# (x_min) (x_max) (y_min) (y_max)
# (#_of_entries)
# (lower_range) (upper_range) (value) [for each entry] 
#

import sys

def create_histogram(bounds, data):
	rows = []
	for i in range(bounds[3]-bounds[2]+1):
		rows.append([str(bounds[2]+i), bounds[2]+i])
		while (len((rows[i])[0]) < len(str(bounds[3]))):
			(rows[i])[0] = " " + (rows[i])[0]
	rows.insert(0, [" " * len(str(bounds[3])), -1])
	prev = (data[0])[1]
	for d in data:
		if (d[0] != prev):
			(rows[0])[0] = (rows[0])[0] + str(d[0]) + " " + str(d[1])
		else:
			(rows[0])[0] = (rows[0])[0] + " " + str(d[1])
		for r in range(1, len(rows)):
			(rows[r])[0] = (rows[r])[0] + " " * len(str(d[0]))
			if ((rows[r])[1] <= d[2]):
				(rows[r])[0] = (rows[r])[0] + "*"
			else:
				(rows[r])[0] = (rows[r])[0] + " "
		prev = d[1]
	final_strings = []
	for r in range(len(rows)):
		final_strings.append((rows.pop())[0])
	return final_strings

def get_ranges(num, x_start, x_stop):
	range_list = []
	for i in range(num):
		data = raw_input().split(" ", 3)
		for j in range(3):
			data[j] = int(data[j])
		if (data[0] < x_start or data[0] > x_stop or data[1] < x_start or data[1] > x_stop):
			sys.exit()
		for r in range_list:
			if (data[0] >= r[0] and data[0] < r[1]):
				sys.exit()
			elif (data[1] > r[0] and data[1] < r[1]):
				sys.exit()
		range_list.append(data)
	range_list.sort(key=lambda x: x[0])
	return range_list

bounds = raw_input().split(" ", 4)
for i in range(4):
	bounds[i] = int(bounds[i])
data = get_ranges(int(raw_input()), bounds[0], bounds[1])
strings = create_histogram(bounds, data)
print ""
for s in strings:
	print s