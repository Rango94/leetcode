class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def Print(self, pRoot):
        flag=True
        out=[]
        cur=[pRoot]
        tmp=[]
        while True:
            if flag:
                tmp_out=[]
                for i in cur:
                    tmp_out.append(i.val)
                    if i.left!=None:
                        tmp.insert(0,i.left)
                    if i.right!=None:
                        tmp.insert(0,i.right)
                cur=[i for i in tmp]
                tmp=[]
                out.append(tmp_out)
                flag=not flag
            else:
                tmp_out=[]
                for i in cur:
                    tmp_out.append(i.val)
                    if i.right!=None:
                        tmp.insert(0,i.right)
                    if i.left!=None:
                        tmp.insert(0,i.left)
                cur=[i for i in tmp]
                tmp=[]
                out.append(tmp_out)
                flag=not flag
            if cur==[]:
                break
        return out



a1=TreeNode(1)
a2=TreeNode(2)
a3=TreeNode(3)
a4=TreeNode(4)
a5=TreeNode(5)
a6=TreeNode(6)
a7=TreeNode(7)
a1.left=a2
# a1.right=a3
a2.left=a4
# a2.right=a5
a4.left=a6
# a3.right=a7
s=Solution()


print(s.Print(a1))


