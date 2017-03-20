-- 03/10/2017 - Challenge 305 - Numbers For Sale
-- https://www.reddit.com/r/dailyprogrammer/comments/5yoo87/20170310_challenge_305_hard_numbers_for_sale/
--

-- generate a list of digits that add up to 69
-- 0 0 0 0 0 0 0 2 9 9 9 9 9 9 9
-- 0 0 0 0 0 0 0 3 8 9 9 9 9 9 9
-- 0 0 0 0 0 0 0 3 9 8 9 9 9 9 9
-- 0 0 0 0 0 0 0 3 9 9 8 9 9 9 9

-- 0 0 0 0 0 0 0 3 9 9 9 9 9 9 8
-- 0 0 0 0 0 0 0 4 7 9 9 9 9 9 9
-- 0 0 0 0 0 0 0 4 8 8 9 9 9 9 9
-- 0 0 0 0 0 0 0 4 8 9 8 9 9 9 9
-- 0 0 0 0 0 0 0 4 8 9 9 8 9 9 9
-- 0 0 0 0 0 0 0 4 8 9 9 9 8 9 9
-- 0 0 0 0 0 0 0 4 8 9 9 9 9 8 9
-- 0 0 0 0 0 0 0 4 8 9 9 9 9 9 8
-- 0 0 0 0 0 0 0 4 9 7 9 9 9 9 9

-- 0 0 0 0 0 0 0 4 9 9 9 9 9 9 7

-- 0 0 0 0 0 0 0 9 9 9 9 9 9 9 2
-- 0 0 0 0 0 0 1 1 9 9 9 9 9 9 9
-- 0 0 0 0 0 0 1 2 8 9 9 9 9 9 9
-- 0 0 0 0 0 0 1 2 9 8 9 9 9 9 9

-- 0 0 0 0 0 0 1 2 9 9 9 9 9 9 8
-- 0 0 0 0 0 0 1 3 7 9 9 9 9 9 9
-- 0 0 0 0 0 0 1 3 8 8 9 9 9 9 9
-- 0 0 0 0 0 0 1 3 8 9 8 9 9 9 9

-- 0 0 0 0 0 0 1 3 8 9 9 9 9 9 8
-- 0 0 0 0 0 0 1 3 9 7 9 9 9 9 9
-- 0 0 0 0 0 0 1 3 9 8 8 9 9 9 9

-- 0 0 0 0 0 0 1 3 9 8 9 9 9 9 8
-- 0 0 0 0 0 0 1 3 9 9 7 9 9 9 9
-- 0 0 0 0 0 0 1 3 9 9 8 8 9 9 9

-- 0 0 0 0 0 0 1 3 9 9 9 9 9 9 7
-- 0 0 0 0 0 0 1 4 8 9 9 9 9 9 8
-- 0 0 0 0 0 0 1 4 6 9 9 9 9 9 9

-- starting from 000000029999999
-- from right to left
-- - find digit to increment and decrement the digit to the right
-- - if can't decrement digit to the right (past last digit),
--   increment last digit and right most non-nine digit,
--   then decrement digit to the right of that non-nine digit
-- - if can't do the above steps,
--   increment digit left of leftmost non-zero digit

function brute_force()
	local sum = 0
	local total = 0
	local i = 69999999
	while i < 1000000000000000 do
		local str = tostring(i)
		local digit_sum = 0
		for j = 1, #str do
			digit_sum = digit_sum + tonumber(str:sub(j,j))
		end
		if digit_sum == 69 then
			sum = sum + i
			total = total + 1
			print(i)
		end
		i = i + 1
	end
	print(sum)
	print(total)
end

function table_to_number(digits)
	str = ""
	for _, v in pairs(digits) do
		str = str .. tostring(v)
	return tonumber(str)
end

function find_non_nine(digits, index)
	for i=index, 0, -1 do
		if digits[i] ~= 9 then return i, digits[i] end
	end
	return 0, 0
end

function algorithm()
	local digits = {0, 0, 0, 0, 0, 0, 0, 6, 9, 9, 9, 9, 9, 9, 9}
	local sum, total = 0, 0
	x = true
	while x do
		sum = sum + table_to_number()
		total = total + 1
		for i=15, 0, -1 do
			local d = digits[i]
			if d ~= 9 then
				if i ~= 15 then
					digits[i] = digits[i] + 1
					digits[i+1] = digits[i+1] - 1
				else
					for j=14, 0, -1 do

					digits[i]
				end
			end
		end
	end
end

brute_force()

