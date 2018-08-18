n=0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            for l in range(1,10):
                if i+j+k+l==10:
                    n+=1
print(n)