
data = input()

data = list(map(int, data.split(" ")))

def QuickSort(a, left, right):
    if(left>=right):
        return
    i,j = left,right
    while(i!=j):
        while(i<j and a[left]<=a[j]):
            j-=1
        while(i<j and a[left]>=a[i]):
            i+=1

        if(i<j):
            a[i],a[j] = a[j],a[i]

    a[left],a[i] = a[i],a[left]
    QuickSort(a, left, i)
    QuickSort(a, i+1, right)

QuickSort(data, 0, len(data)-1)

print(" ".join(map(str, data)))