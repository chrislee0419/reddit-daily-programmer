-- 01/04/2017 - Challenge 298 - Too many or too few parentheses
-- https://www.reddit.com/r/dailyprogrammer/comments/5m034l/20170104_challenge_298_intermediate_too_many_or/
--

local stack = {}
local index = -1

for i=1, #arg[1] do
	local c = arg[1]:sub(i,i)
	if c == '(' then
		table.insert(stack, i)
	elseif c == ')' then
		if #stack == 0 then
			index = i
			break
		else
			table.remove(stack)
		end
	end
end
if #stack ~= 0 then index = stack[#stack] end
if index == -1 then print(arg[1])
else
	local s = ""
	for i=1, #arg[1] do
		if i == index then s = s .. "*" .. arg[1]:sub(i,i) .. "*"
		else s = s .. arg[1]:sub(i,i) end
	end
	print(s)
end