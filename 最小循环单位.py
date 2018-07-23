'''
对于一个长度为n的数组P，我们可以通过P构造出一个无限长的数组S，其中P[i]=S[i%n]
给定一个字符串P，求其最小循环单位S
'''
'''
解题思路：
找到len(S)的所有因子，截取对应长度比较即可
'''
def solution(S):
    lens=[]
    for i in range(1,int(len(S)/2+1)):
        if len(S)%i==0:
            lens.append(i)
    for i in lens:
        flag=0
        for j in range(int(len(S)/i)-2):
            if S[j*i:(j+1)*i]!=S[(j+1)*i:(j+2)*i]:
                flag=1
                break
        if flag==0:
            return S[0:i]
    return S


print(solution([1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2]))

