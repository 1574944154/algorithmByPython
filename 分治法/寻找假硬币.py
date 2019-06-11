import random


coins = [6 for i in range(11)]

coins[random.randint(0,9)] = 5

left = 0
right = len(coins)

while(left<right-1):
    mid = int((right+left)/2)
    if(sum(coins[left:mid])/(mid-left)>sum(coins[mid:right])/(right-mid)):
        left = mid
    else:
        right = mid

print(left, right)