


class Solution:
    def Permutation(self, ss):
        if ss == '':
            return []
        out = self.solution(ss)
        out = [''.join(i) for i in out]
        dic = {}
        for i in out:
            dic[i] = 1
        return [i for i in dic]

    def solution(self, a):
        if a==None:
            return []
        else:
            tmp = self.solution(a[1:])
            out=[]
            for i in tmp:
                for j in range(len(i)):
                    out.append(self.insert_(j,a[0],i))
                    print(out)
                    out.append(self.insert_(j, a[0], i))
            print(out)
            return out

    def insert_(self,index,x,s):
        if index==0:
            return x+s
        if index==len(s):
            return s+x
        else:
            return s[:index]+x+s[index:]

s=Solution()
s.Permutation('abc')