class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        dic={0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}
        musk=[]
        m=0
        for i in matrix:
            tmp=[]
            for j in range(len(i)):
                m+=1
                tmp.append(0)
            musk.append(tmp)
        step_num=0
        n=1
        step=[0,0]
        c=0
        print(matrix[0][0])
        musk[0][0]=1
        while n<m:
            try:
                if musk[step[0] + dic[c % 4][0]][step[1] + dic[c % 4][1]]!=1:
                    print(matrix[step[0] + dic[c % 4][0]][step[1] + dic[c % 4][1]])
                    musk[step[0] + dic[c % 4][0]][step[1] + dic[c % 4][1]] = 1
                    step[0]+=dic[c % 4][0]
                    step[1] += dic[c % 4][1]
                    n+=1
                else:
                    c+=1
            except:
                c+=1


A=[[1]]
s=Solution()
s.printMatrix(A)