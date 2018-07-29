'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

'''
递归分治
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(tin)==1:
            return TreeNode(pre[0])
        elif tin==[]:
            return None
        else:
            root = TreeNode(pre[0])
            left, right = self.Split(tin, pre[0])
            root.left = self.reConstructBinaryTree(pre[1:len(left) + 1], left)
            root.right = self.reConstructBinaryTree(pre[len(left) + 1:], right)
        return root

    def Split(self, A, x):
        # print(A[:A.index(x)], A[A.index(x) + 1:])
        return A[:A.index(x)], A[A.index(x) + 1:]


A=[1,2,4,3,5,6]
B=[4,2,1,5,3,6]

s=Solution()
s.reConstructBinaryTree(A,B)