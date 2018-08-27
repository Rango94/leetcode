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

class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array)==0 or array==None:
            return False
        if len(array)==1 and len(array[0])==1:
            if array[0][0]==target:
                return True
            else:
                return False
        else:
            x,y=int(len(array)/2),int(len(array[0])/2)
            if array[x][y]==target:
                return True
            elif array[x][y]>target:
                return self.Find(target,[i[:y] for i in array[:x]]) \
                        or self.Find(target,[i[y:] for i in array[:x]]) \
                        or self.Find(target,[i[:y] for i in array[x:]])
            else:
                return self.Find(target,[i[y:] for i in array[x:]]) \
                        or self.Find(target,[i[y:] for i in array[:x]]) \
                        or self.Find(target,[i[:y] for i in array[x:]])
        # write code here

n,A=7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
s=Solution()

print(s.Find(n,A))