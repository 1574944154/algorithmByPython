x = int(input())

a = b = 1

for i in range(3, x+1):
    a,b = b,a+b

print(b)