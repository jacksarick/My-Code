
# def intersection(ray, test):
#     l1 = line(cameraPos, ray)
#     l2 = line(*test)

#     D  = l1[0] * l2[1] - l1[1] * l2[0]
#     Dx = l1[2] * l2[1] - l1[1] * l2[2]
#     Dy = l1[0] * l2[2] - l1[2] * l2[0]
#     if D != 0:
#         x = Dx / D
#         y = Dy / D
#         return x,y
#     else:
#         return False

# def intersect(self, ray):
#     vert = self.vertices()
#     lines = [(vert[0],vert[1]), (vert[0],vert[2]), (vert[1],vert[3]), (vert[2],vert[3])]
#     return list(set([intersection(ray.get(), line) for line in lines]))

# def vertices(self):
#     return [
#         (self.x, self.y), (self.x+self.n, self.y),
#         (self.x, self.y+self.n), (self.x+self.n, self.y+self.n)
#     ]

# def line(p1, p2):
#     A = (p1[1] - p2[1])
#     B = (p2[0] - p1[0])
#     C = (p1[0]*p2[1] - p2[0]*p1[1])
#     return A, B, -C



def castSingleRay(x, y, angle) {
	right = (rayAngle > twoPI * 0.75 || rayAngle < twoPI * 0.25)

	sin = math.sin(angle)
	cos = math.cos(angle)
	var dist = 0
	# The x and y coord of where the ray hit the block
	xHit = 0
	yHit = 0
	# The (x,y) map coords of the block
	wallX = 0
	wallY = 0


	# The slope of the straight line made by the ray
	slope = sin / cos
	dX = right ? 1 : -1
	dY = dX * slope

	x = right ? ceil(player.x) : floor(player.x)
	y = player.y + (x - player.x) * slope

	while (x >= 0 && x < mapWidth && y >= 0 && y < mapHeight) {
		wallX = floor(x + (right ? 0 : -1))
		wallY = floor(y)

		# Is this point inside a wall block?
		if (map[wallY][wallX] > 0) {
			distX = x - player.x
			distY = y - player.y
			# The distance from the player to this point, squared
			dist = distX*distX + distY*distY

			# Save the coordinates of the hit. We only really
			# use these to draw the rays on minimap
			xHit = x
			yHit = y
			break
		}
		x += dX
		y += dY
	}
	return (xHit, yHit)
}