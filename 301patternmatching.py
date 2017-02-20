# 02/02/2017 - Challenge 301 - Looking for Patterns
# https://www.reddit.com/r/dailyprogrammer/comments/5rlpz1/20170202_challenge_301_easyintemerdiate_looking/
# 

def create_pattern(string):
	pattern = ""
	char_list = []
	for c in string:
		exists = 0
		for i in range(len(char_list)):
			if (c == char_list[i]):
				exists = 1
				pattern += str(i)
				break
		if (not exists):
			char_list.append(c)
			pattern += str(len(char_list) - 1)
	return pattern

dic = None
with open("301dictionary.txt") as f:
	dic = [line.rstrip("\n") for line in f]
pattern = create_pattern(raw_input())
for word in dic:
	for i in range(len(word) - len(pattern) + 1):
		if (pattern == create_pattern(word[i:i + len(pattern)])):
			print word
			break