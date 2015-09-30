import urllib2

web_data = urllib2.urlopen("http://api.openweathermap.org/data/2.1/find/city?lat=43.693575&lon=-79.404119&cnt=1")

raw_data = []

for line in web_data:
	raw_data = line.split(",")

for i in range(len(raw_data)):
	raw_data[i] = str(raw_data[i]).translate(None, ('"' or "{" or "}" or "[" or "]"))

print raw_data[5][range(5, 11)]