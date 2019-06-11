
n = int(input())

count = 0

def zou(n):
    global count
    if(n==0):
        count+=1
    # if(n>=3):
    #     zou(n-3)
    if(n>=2):
        zou(n-2)
    if(n>=1):
        zou(n-1)

zou(n)
print(count)