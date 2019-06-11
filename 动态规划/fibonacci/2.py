
n = int(input())

a = list(-1 for i in range(1001))

def fib(n, a):
    if(n==1 or n==2):
        return 1
    if(a[n]!=-1):
        return a[n]
    a[n] = fib(n-1, a)+fib(n-2, a)
    return a[n]

print(fib(n, a))