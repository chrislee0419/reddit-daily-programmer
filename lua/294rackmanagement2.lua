-- 12/07/2016 - Challenge 294 - Rack Management 2
-- https://www.reddit.com/r/dailyprogrammer/comments/5h40ml/20161207_challenge_294_intermediate_rack/
--
-- 100k output result:
-- total: 	4 hrs 36 mins 18 seconds
-- average:	0.16854659 s
-- max:		0.28099999999904 s
-- min: 	0.07799999999952 s
--
-- optimizations:
-- sort dictionary by word value and then length
-- remove words from dictionary that are too long
-- modified_highest() stops searching on first result

num_of_tests = 20
points = {
	a = 1, b = 3, c = 3, d = 2, e = 1, f = 4, g = 2,
	h = 4, i = 1, j = 8, k = 5, l = 1, m = 3, n = 1,
	o = 1, p = 3, q = 10, r = 1, s = 1, t = 1, u = 1,
	v = 4, w = 4, x = 8, y = 4, z = 10
}

function test_word(alpha_table, word)
	local p = 0
	for ch=#word, 1, -1 do
		local c = word:sub(ch, ch)
		if not alpha_table[c] or alpha_table[c] == 0 then
			if not alpha_table["?"] or alpha_table["?"] == 0 then return 0
			else alpha_table["?"] = alpha_table["?"] - 1 end
		else
			alpha_table[c] = alpha_table[c] - 1
			p = p + ch * points[c]
		end
	end
	return p
end

function highest(filename, rack)
	local alpha_table = {}
	for c in rack:gmatch(".") do
		if not alpha_table[c] then alpha_table[c] = 1
		else alpha_table[c] = alpha_table[c] + 1 end
	end
	local word, points = "", 0
	for line in io.lines(filename) do
		local alpha = {}
		for k, v in pairs(alpha_table) do alpha[k] = v end
		local p = test_word(alpha, line)
		if p > points then
			word = line
			points = p
		end
	end
	return word, points
end

-- returns first match (only works with preprocessed dictionary)
function modified_highest(filename, rack)
	for line in io.lines(filename) do
		local p = test_word(rack, line)
		if p > 0 then return line, p end
	end
end

function perform_test(filename, test_func)
	os.execute("cat /dev/urandom | tr A-Z eeeeeaaaaiiiooonnrrttlsudg | tr 0-9 ? | tr -dc a-z? | fold -w 20 | head -n " .. tostring(num_of_tests) .. " > 294randomizedracks.txt")
	local total_time, max_time, min_time = 0, 0, 5
	local start_time, end_time, time = 0, 0, 0
	for line in io.lines("294randomizedracks.txt") do
		start_time = os.clock()
		local word, p = test_func(filename, line)
		end_time = os.clock()
		time = end_time - start_time
		total_time = total_time + time
		if max_time < time then max_time = time
		elseif min_time > time then min_time = time end
	end
	print("Results:")
	print("- Total time:", total_time)
	print("- Average time:", total_time/num_of_tests)
	print("- Max time:", max_time)
	print("- Min time:", min_time)
	os.execute("rm 294randomizedracks.txt")
end

function word_list_processing()
	print("Creating preprocessed dictionary...")
	local start_time = os.clock()
	local res = {}
	for line in io.lines("../enable1.txt") do
		if #line < 21 then table.insert(res, line) end
	end
	table.sort(res, function(a,b)
		local score_a = 0
		local score_b = 0
		for i=1, #a do
			score_a = score_a + i * points[a:sub(i,i)]
		end
		for j=1, #b do
			score_b = score_b + j * points[b:sub(j,j)]
		end
		if (score_a == score_b) then return #a < #b
		else return score_a > score_b end
	end)
	local file = io.open("294preprocesseddictionary.txt", "w")
	for _, l in ipairs(res) do file:write(l, "\n") end
	io.close(file)
	print("Time to generate preprocessed dictionary:", tostring(os.clock()-start_time))
end

if (arg[1]) then
	if (arg[2]) then
		local start_time, end_time = 0, 0
		if (arg[1] == "1") then
			start_time = os.clock()
			print(highest("../enable1.txt", arg[2]))
			end_time = os.clock()
		elseif (arg[1] == "2") then
			start_time = os.clock()
			print(highest("294preprocesseddictionary.txt", arg[2]))
			end_time = os.clock()
		elseif (arg[1] == "3") then
			start_time = os.clock()
			print(modified_highest("294preprocesseddictionary.txt", arg[2]))
			end_time = os.clock()
		end
		print("Time taken:", tostring(end_time - start_time))
	elseif (arg[1] == "1") then
		print("Running 100k preprocessed test with modified function...")
		num_of_tests = 100000
		perform_test("294preprocesseddictionary.txt", modified_highest)
	else word_list_processing() end
else
	print("Number of trials: " .. tostring(num_of_tests))
	print("Running baseline test...")
	perform_test("../enable1.txt", highest)
	print("Running preprocessed test...")
	perform_test("294preprocesseddictionary.txt", highest)
	print("Running preprocessed test (with modified function)...")
	perform_test("294preprocesseddictionary.txt", modified_highest)
end