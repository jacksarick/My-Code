minstotime = lambda mins: list(str(mins / 60) + str(mins % 60)) if mins >= 780 else time(mins-780)