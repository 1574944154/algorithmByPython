import math
a,b = map(int, input().split())

def isSu(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True

l = list(filter(isSu, [i for i in range(2,105000)]))

l = l[a-1:b]

for i in range(0,len(l),10):
    print(" ".join(list(map(str, l[i:i+10]))))