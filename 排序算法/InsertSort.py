
data = "5 3 4 7 2 8 6 9 1"

a = list(map(int, data.split()))

for i in range(1, len(a)):
    for j in range(i - 1, -1, -1):
        if (a[j] > a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
        else:
            break

print(a)











# def InsertSort(a):
#
#     for i in range(1,len(a)):
#         for j in range(i-1, -1, -1):
#             if(a[j]>a[j+1]):
#                 a[j],a[j+1] = a[j+1],a[j]
#
# InsertSort(data)
#
# print(data)