love.load = function ()
	shape = line(sp1, sp2)
	printd(shape)
end

love.draw = function ()
	-- love.graphics.points(shape)
	-- love.graphics.print(dump(shape), 100, 100)
	-- print(dump(sp1 ^ sp2))
end