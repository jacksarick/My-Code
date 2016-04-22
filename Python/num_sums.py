def nums(x): return nums(sum(map(int, list(str(x))))) if len(str(x)) != 1 else x
print map(nums, [n for n in range(1,10000)])