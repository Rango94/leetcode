def Find( target, array):
    print(array)
    if len(array) == 1 :
        if target in array[0]:
            return True
        else:
            return False
    x, y = [len(array), len(array[0])]
    if array[int(x / 2)][int(y / 2)] == target:
        return True
    elif array[int(x / 2)][int(y / 2)] < target:
        return Find(target, [[j for j in i[int(y/2):]]for i in array[int(x/2):]]) or Find(target, [[j for j in i[:int(y/2)]]for i in array[int(x/2):]]) or Find(target, [[j for j in i[int(y/2):]]for i in array[:int(x/2)]])
    else:
        return Find(target, [[j for j in i[:int(y/2)]]for i in array[:int(x/2)]]) or Find(target, [[j for j in i[int(y/2):]]for i in array[:int(x/2)]]) or Find(target, [[j for j in i[:int(y/2)]]for i in array[int(x/2):]])


n,A=7,[[1,2,8,9],[4,7,10,13]]
print(Find(n,A))