'''
与子序列相似，只是要求连续
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
        l1=solution(A[:-1],B)
        l2=solution(A,B[:-1])
        return max([l0,l1,l2])
    else:
        return l0


A=[1,2,3,45,1,2,3,4,5,6,6,7,8,8]
B=[1,2,3,5,1,2,3,4,9]

print(solution(A,B))