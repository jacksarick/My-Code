require "list"
require "point"

require "dev"

line = function (p1, p2)
	line = {}
	setmetatable(line, metalist)
	d = p1 ^ p2
	print(dump(d))

	-- Draw the line by the greatest change
	if d.y > d.x then
		steep = true
		p1 = #p1
		p2 = #p2
	end

	-- Draw line left to right
	if p1.x > p2.x then
		p1, p2 = p2, p1
	end

	for x = p1.x, p2.x do
		t = (x - p1.x)/(p2.x - p1.x)
		y = p1.y*(1 - t) + p2.y*t

		if steep then
			line = line .. {y, x}
		else
			line = line .. {x, y}
		end
	end

	return line
end

sp1 = point(10, 10)
sp2 = point(20, 200)
sp3 = point(30, 30)

printd(line(sp1, sp2))

love.load = function ()
	shape = line(sp1, sp2)
	printd(shape)
end

love.draw = function ()
	-- love.graphics.points(shape)
	-- love.graphics.print(dump(shape), 100, 100)
	-- print(dump(sp1 ^ sp2))
end