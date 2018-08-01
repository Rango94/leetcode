'''
给定一个有序数组和一个k 求数组中所有加和为k的两个数的个数
'''


'''
递归求解
'''


def solution(A,k):
    i=0
    j=len(A)-1
    while True:
        if A[i]+A[j]>k:
            j-=1
        if A[i]+A[j]<k:
            i+=1
        if A[i]+A[j]==k:
            pre_n=1
            aft_n=1
            if A[i]!=A[j]:
                while A[i+1]==A[i]:
                    pre_n+=1
                    i+=1
                while A[j-1]==A[j]:
                    aft_n+=1
                    j-=1
                return pre_n*aft_n+solution(A[i+1:j],k)
            else:
                return (j-i+1)*(j-i)/2
        if i>=j:
            return 0




A=[0,1,1,1,1,1,1,1]
k=2
print(solution(A,k))


