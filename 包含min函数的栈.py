'''
定义栈的数据结构，
请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''

'''
建立一个辅助list
'''

class Solution:
    A=[]
    B=[]
    def push(self, node):
        self.A.append(node)
        if self.B==[]:
            self.B.append(node)
        elif self.B[-1]>node:
            self.B.append(node)
        else:
            self.B.append(self.B[-1])

        # write code here
    def pop(self):
        self.A.pop(-1)
        self.B.pop(-1)
        # write code here
    def top(self):
        return self.A[-1]
        # write code here
    def min(self):
        return self.B[-1]