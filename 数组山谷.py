'''
数组山谷是指数组A的子数组B满足 存在i使得B[0]>B[1].....>B[i]<B[i+1]<B[i+2]....B[len(B)-1]
给出一个数组A，返回最长B的长度
'''


def find_v(s):
    out=[]
    max_len=0
    for i in range(1,len(s)-1):
        tmp=find_max(s,i)
        if tmp>max_len:
            max_len=tmp
    return max_len



def find_max(s,idx):
    i=idx-1
    j=idx+1
    if s[i]<s[idx] or s[j]<s[idx]:
        return 0
    while i>0 and s[i]>s[i+1]:
        i-=1
    while j<len(s) and s[j]>s[j-1]:
        j+=1
    return j-i-1


print(find_v([4,5,6,7,2,2,3,4,5,6,7,1]))