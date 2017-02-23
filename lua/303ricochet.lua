-- 02/21/2017 - Challenge 303 - Ricochet (with bonus)
-- https://www.reddit.com/r/dailyprogrammer/comments/5vb1wf/20170221_challenge_303_easy_ricochet/
-- 
-- Usage:
-- (height_of_box) (width_of_box) (height_of_particle) (width_of_particle) (speed)
--

local vert, hori = 0, 0
local dy, dx = tonumber(arg[1]) - tonumber(arg[3]), tonumber(arg[2]) - tonumber(arg[4])
local left, up = true, true
while true
do
	if vert < hori then
		vert = vert + dy
		up = not up
	else
		hori = hori + dx
		left = not left
	end
	if vert == hori then
		local c = left and "LL" or up and "UR" or "LR"
		print(c, hori/dx + vert/dy - 2, vert / tonumber(arg[5]))
		return
	end
end