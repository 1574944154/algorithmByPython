
a = "I love you"

data = " ".join(list(map(lambda x:x[::-1],a.split()))[::-1])

print(data)