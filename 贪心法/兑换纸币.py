
x = int(input())

moneys = [100,50,20,10,5,1]

for i in range(6):
    print("需要"+str(moneys[i])+"纸币"+str(int(x/moneys[i]))+"张")
    x = x%moneys[i]