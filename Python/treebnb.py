cities = {}

with open("new_data.csv") as f:

	for line in f:
		datum = line.split(",")
		# print datum
		if not cities.has_key(datum[1].title()):
			cities[datum[1].title()] = []

		cities[datum[1].title()].append(int(datum[3]))

# average: sum(cities[x])/len(cities[x])
# spread: max(cities[x]) - min(cities[x])

def diff(x):
	mid = sorted(x)[len(x)/2]
	return mid - (sum(x)/len(x))


cities = {x:diff(cities[x]) for x in cities}
cities = sorted(cities.items(), key=lambda x: x[1])
print cities[:10]