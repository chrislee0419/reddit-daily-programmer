# 02/08/2017 - Challenge 302 - Proper ASCII Histogram
# https://www.reddit.com/r/dailyprogrammer/comments/5t7l07/20170210_challenge_302_hard_ascii_histogram_maker/
#
# Usage:
# (x_min) (x_max) (y_min) (y_max)
# (x_interval_size)
# (#_of_entries)
# (x_value) (count)
#

import sys

def create_histogram(bounds, data):
	rows = []
	for i in range(bounds[3]-bounds[2]+1):
		rows.append([str(bounds[2]+i), bounds[2]+i])
		while (len((rows[i])[0]) < len(str(bounds[3]))):
			(rows[i])[0] = " " + (rows[i])[0]
	rows.insert(0, [" " * len(str(bounds[3])) + str((data[0])[0]), -1])
	for d in data:
		(rows[0])[0] += " " + str(d[1])
		for r in range(1, len(rows)):
			(rows[r])[0]  += " " * len(str(d[0]))
			if ((rows[r])[1] <= d[2]):
				(rows[r])[0] += "*"
			else:
				(rows[r])[0] += " "
	final_strings = []
	for r in range(len(rows)):
		final_strings.append((rows.pop())[0])
	return final_strings

def get_ranges(num, x_start, x_stop, interval):
	value_list = []
	for i in range(num):
		value = raw_input().split(" ", 2)
		value[0] = int(value[0])
		value[1] = int(value[1])
		if (value[0] >= x_start and value[0] <= x_stop):
			value_list.append(value)
	value_list.sort(key=lambda x: x[0])
	range_list = [[x_start, x_start + interval, 0]]
	length = len(value_list)
	while ((value_list[0])[0] < x_start):
		value_list.pop(0)
	for i in range(length):
		value = value_list.pop(0)
		if (value[0] >= x_stop):
			break
		while (value[0] >= (range_list[0])[1]):
			start = (range_list[0])[1]
			end = start + interval
			if (start >= x_stop):
				sys.exit()
			range_list.insert(0, [start, end, 0])
		(range_list[0])[2] += value[1]
	while ((range_list[0])[0] + interval < x_stop):
		range_list.insert(0, [(range_list[0])[0] + interval, (range_list[0])[0] + 2*interval, 0])
	range_list.reverse()
	return range_list

bounds = raw_input().split(" ", 4)
for i in range(4):
	bounds[i] = int(bounds[i])
interval = int(raw_input())
data = get_ranges(int(raw_input()), bounds[0], bounds[1], interval)
strings = create_histogram(bounds, data)
print ""
for s in strings:
	print s