-- 12/05/2016 - Challenge 294 - Rack Management 1 (with bonuses)
-- https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/
-- 

points = {
	a = 1, b = 3, c = 3, d = 2, e = 1, f = 4, g = 2,
	h = 4, i = 1, j = 8, k = 5, l = 1, m = 3, n = 1,
	o = 1, p = 3, q = 10, r = 1, s = 1, t = 1, u = 1,
	v = 4, w = 4, x = 8, y = 4, z = 10
}

function scrabble(rack, word)
	local alpha = {}
	local p = 0
	for c in rack:gmatch(".") do
		if not alpha[c] then alpha[c] = 1
		else alpha[c] = alpha[c] + 1 end
	end
	for c in word:gmatch(".") do
		if not alpha[c] or alpha[c] == 0 then
			if not alpha["?"] or alpha["?"] == 0 then return false, 0
			else alpha["?"] = alpha["?"] - 1 end
		else
			alpha[c] = alpha[c] - 1
			p = p + points[c]
		end
	end
	return true, p
end

function longest(rack)
	if #rack > 20 then return "" end
	local max_length = 0
	local word = ""
	for line in io.lines("../enable1.txt") do
		if scrabble(rack, line) and max_length < #line then
			word = line
			max_length = #line
		end
	end
	return word
end

function highest(rack)
	if #rack > 20 then return "" end
	local max_points = 0
	local word = ""
	for line in io.lines("../enable1.txt") do
		local sc, p = scrabble(rack, line)
		if sc and max_points < p then
			word = line
			max_points = p
		end
	end
	return word
end

local s = scrabble(arg[1], arg[2])
print("scrabble:", s)
print("longest:", longest(arg[1]))
print("highest:", highest(arg[1]))