print [(((x not in [3*i for i in range(1000)]) and (x not in [5*i for i in range(1000)]*10)) * str(x)) + ((x in [3*i for i in range(1000)]) * "Fizz") + ((x in [5*i for i in range(1000)]*10) * "Buzz") for x in range(1000)]