data = input()

data = list(map(int, list(data)))

len = len(data)

if(len>2):
    print(data[0]*"B", end="")

if(len>1):
    print(data[1]*"S", end="")

if(len>0):
    print(int("".join(list(map(str, range(1,data[2]+1))))), end="")