class Solution:
    def InversePairs(self, data):
        n=0
        new_data = []
        for i in data:
            new_data.append([i])
        while len(new_data) != 1:
            tmp_n,new_data = self.solution(new_data)
            print(tmp_n,new_data)
            n+=tmp_n
        return n

    def solution(self, data):
        out = []
        n=0
        while data != []:
            if len(data) == 1:
                out.append(data[0])
                data.pop(0)
            else:
                n += self.inverse(data[0], data[1])
                out.append(self.sort(data[0], data[1]))
                data.pop(0)
                data.pop(0)

        return n,out

    def sort(self, a, b):
        out = []
        i = 0
        j = 0
        while i<len(a) or j<len(b):
            if i==len(a):
                out.append(b[j])
                j+=1
            elif j==len(b):
                out.append(a[i])
                i+=1
            elif a[i]<b[j]:
                out.append(a[i])
                i+=1
            elif a[i]>=b[j]:
                out.append(b[j])
                j+=1
        return out

    def inverse(self,a,b):
        n=0
        for i in a:
            for j in range(len(b)-1,-1,-1):
                if i>b[j]:
                    n+=j+1
                    break
        return n





s=Solution()
a=[364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
print(s.InversePairs(a))