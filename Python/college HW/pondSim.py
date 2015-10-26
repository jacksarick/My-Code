################################################################
# Pond Spill Simulator | Project flow of spill between ponds.  #
# For: No particular reason			    					   #
# Author: Jack Sarick				     					   #
# Created: October 25, 2015								 	   #
# Modified: October 25, 2015								   #
# Language: Python 3.5										   #
################################################################

# Gather world rules
RATE_OF_FLOW = .005
MAX_POLLUTANT = float(input("Max pollutant\n>"))
RATE_OF_LEAK = float(input("Rate the pollutant is leaking\n>"))
TOTAL_TIME = float(input("Amount of time to simulate\n>"))

# Generate world
ponds = {1:{"hist":0,"now":0}, 2:{"hist":0,"now":0}, 3:{"hist":0,"now":0}}

