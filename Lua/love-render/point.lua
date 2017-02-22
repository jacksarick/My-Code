metapoint = {}

point = function (x, y)
	p = {x = x, y = y}
	setmetatable(p, metapoint)
	return p
end

-- Summing points
function metapoint.__add(p1, p2)
	return point((p1.x + p2.x), (p1.y + p2.y))
end

-- Finding difference, NOT power
function metapoint.__pow(p1, p2)
	return point(math.abs(p1.x - p2.x), math.abs(p1.y - p2.y))
end

-- Flip a point, NOT find it's length (that's always two)
function metapoint.__len(p)
	return point(p.y, p.x)
end