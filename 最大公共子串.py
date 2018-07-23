'''
与子序列相似，只是要求连续
'''

'''
解题思路，对于A和B，令l0=0，如果A[-1]==B[-1]，则l0++，并判断是否A[-2]==B[-2],直到不满足条件，保存l0

否则，l=max(L(A,B[:-1]),L(A[:-1],B))
'''


def solution(A,B):
    l0=0
    i=len(A)-1
    j=len(B)-1
    while i>=0 and j>=0 and A[i]==B[j]:
        i-=1
        j-=1
        l0+=1
    if len(A)>1 and len(B)>1:
        l1=solution(A[:i+1],B[:j])
        l2=solution(A[:i],B[:j+1])
        return max([l0,l1,l2])
    else:
        return l0


A=[5,5,5,5,5,5,1,2,3,45,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
B=[1,2,3,5,1,35,2,3,45,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6]

print(solution(A,B))