
nums = "2 2 0 0 0 3 0 0 1 0"

nums = sorted(list(map(int, nums.split(" "))))

min = list(filter(lambda x:x>0, set(nums)))[0]

nums.remove(min)
nums.insert(0, min)

print(int("".join(map(str, nums))))