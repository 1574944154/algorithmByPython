
num = int(input())

max = "2014/05/12"
min = "1814/09/06"

data = []

for i in range(num):
    data.append(input())

filterd_data = list(filter((lambda x:x.split(" ")[1]>=min and x.split(" ")[1]<=max), data))


sorted_data = sorted(filterd_data, key=lambda x:x.split(" ")[1])

print(len(sorted_data), sorted_data[0].split(" ")[0], sorted_data[-1].split(" ")[0])