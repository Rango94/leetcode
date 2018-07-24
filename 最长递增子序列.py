


def findLongest(A, n):
    c = []
    for i in range(n):
        tmp = [1]
        c.append(1)
        for j in range(i, -1, -1):
            if A[j] < A[i]:
                tmp.append(c[j] + 1)
        c[i] = max(tmp)
    return max(c)



A=[157,232,6]
print(findLongest(A,len(A)))