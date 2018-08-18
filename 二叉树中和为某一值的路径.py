'''
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import copy


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    out = []
    tmp = []

    def FindPath(self, root, expectNumber):
        self.new(root, expectNumber)
        new_out = copy.deepcopy(self.out)
        self.out = []
        self.tmp = []
        return new_out

    def new(self, root, expectNumber):
        if root != None:
            self.tmp.append(root.val)
            if root.left == None and root.right == None and sum(self.tmp) == expectNumber:
                self.out.append(copy.deepcopy(self.tmp))
                self.tmp.pop(-1)
            if root.left != None:
                self.new(root.left, expectNumber)
            if root.right != None:
                self.new(root.right, expectNumber)
            else:
                self.tmp.pop(-1)
        return self.out


t4=TreeNode(4)
t5=TreeNode(5)
t7=TreeNode(7)
t10=TreeNode(10)
t12=TreeNode(12)

t5.left=t4
t5.right=t7

t10.left=t5
t10.right=t12

s=Solution()
print(s.FindPath(t10,22))
print(s.FindPath(t10,15))
print(s.FindPath(t10,19))
