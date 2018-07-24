'''
（1）子序列： 一个序列A ＝ a1,a2,……an,中任意删除若干项，剩余的序列叫做A的一个子序列。也可以认为是从序列A按原顺序保留任意若干项得到的序列。

例如：

对序列 1,3,5,4,2,6,8,7来说，序列3,4,8,7 是它的一个子序列。
对于一个长度为n的序列，它一共有2^n 个子序列，有(2^n – 1)个非空子序列。

请注意：子序列不是子集，它和原始序列的元素顺序是相关的。

（2）公共子序列 ： 顾名思义，如果序列C既是序列A的子序列，同时也是序列B的子序列，则称它为序列A和序列B的公共子序列。

例如：

对序列 1,3,5,4,2,6,8,7和序列 1,4,8,6,7,5 来说

序列1,8,7是它们的一个公共子序列。

请注意： 空序列是任何两个序列的公共子序列。
例如： 序列1,2,3和序列4,5,6的公共子序列只有空序列。

（3）最长公共子序列

A和B的公共子序列中长度最长的（包含元素最多的）叫做A和B的公共子序列。
仍然用序列1,3,5,4,2,6,8,7和序列1,4,8,6,7,5

它们的最长公共子序列是：

1,4,8,7
1,4,6,7

'''


'''
解题思路，对于A和B，用L(A,B)表示其最大长度l，如果A[-1]==B[-1]则，最大长度l=L(A[:-1],B[:-1])+1
否则，l=max(L(A,B[:-1]),L(A[:-1],B))
'''


def findLCS(A, n, B, m):
    c = []
    for i in range(n+1):
        tmp = []
        for j in range(m+1):
            tmp.append(0)
        c.append(tmp)
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                c[i][j]=0
            elif A[i-1] == B[j-1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max([c[i - 1][j], c[i][j - 1]])
    for i in c:
        print(i)
    return c[-1][-1]

A="joneoovzzmuispkgmnhqgdmbchdntanbofhcwftcdnbsyvcragunnopknzazjqoprujqfiesoreslzvgzaed"
B="oynwkodiovsvkliehbvvggpdydesncaentayeufhoaaildsdwkfpnvxwpsqcujtssriiudgyxstiefyvsp"

print(findLCS(A,84,B,82))