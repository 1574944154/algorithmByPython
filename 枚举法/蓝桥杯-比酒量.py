

for a in range(20, 1, -1):
    for b in range(20, 1, -1):
        for c in range(20, 1, -1):
            for d in range(20, 1, -1):
                if(1/a+1/b+1/c+1/d==1):
                    print(a,b,c,d)