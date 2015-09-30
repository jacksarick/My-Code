itemlist = ["RawMithril","MithrilShard","Mithril","MagicHammer","MeteorBucket","MeteorIngot","Reinforcedbone","GoldFeather"]
jsonout = ["{\n\t\"parent\":\"mythical:item/" + itemname + "\",\n\t\"textures\": {\n\t\"layer0\":\"mythical:items/" + itemname + "\"\n\t}\n}" for itemname in itemlist]

i = 0
for item in jsonout:
	newfile = open("./" + itemlist[i] + ".json", "w")
	newfile.write(item)
	newfile.close()
	i += 1