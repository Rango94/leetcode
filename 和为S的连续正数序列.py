class Solution:
    def FindContinuousSequence(self, tsum):
        i=1
        max_=tsum/2
        out=[]
        while i<max_:
            j=i+1
            while ((i+j)*(j-i+1))/2<tsum:
                j+=1
            if ((i+j)*(j-i+1))/2==tsum:
                out.append([k for k in range(i,j+1)])
            i+=1
        return out


s=Solution()
print(s.FindContinuousSequence(964))