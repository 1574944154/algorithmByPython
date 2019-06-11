nums, c = input().split()
nums = int(nums)

nums_copy = nums

max_lines = 1

nums_copy-=1

for i in range(3,1001,2):
    if(nums_copy-2*i>=0):
        nums_copy-=2*i
        max_lines=i
    else:
        break

nums_copy = nums

for i in range(max_lines, 0, -2):
    print(" "*int((max_lines-i)*0.5), end="")
    print(c*i)
    nums_copy-=i

for i in range(3, max_lines+1, 2):
    print(" "*int((max_lines-i)*0.5), end="")
    print(c*i)
    nums_copy-=i

print(nums_copy)