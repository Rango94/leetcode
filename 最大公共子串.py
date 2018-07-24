'''
与子序列相似，只是要求连续
'''

'''
解题思路，对于A和B，令l0=0，如果A[-1]==B[-1]，则l0++，并判断是否A[-2]==B[-2],直到不满足条件，保存l0

否则，l=max(L(A,B[:-1]),L(A[:-1],B))
'''


def findLongest(A, n, B, m):
    c = []
    for i in range(n + 1):
        tmp = []
        for j in range(m + 1):
            tmp.append(0)
        c.append(tmp)
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = 0
    for i in c:
        print(i)
    return max([max(i) for i in c])


A="1AB2345CD"
B="12345EF"

print(findLongest(A,9,B,7))