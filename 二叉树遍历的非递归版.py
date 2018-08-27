class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre(root):
    nodes=[root]
    out=[]
    while nodes!=[]:
        p=nodes[-1]
        print([i.val for i in nodes])
        nodes.pop(-1)
        print(p.val)
        if p!=None:
            out.append(p.val)
            if p.right!=None:
                nodes.append(p.right)
            if p.left!=None:
                nodes.append(p.left)
    return out

def mid(root):
    nodes=[root]
    out=[]
    p = nodes[-1]
    while nodes!=[]:
        while p!=None and p.left!=None:
            p=p.left
            nodes.append(p)
        p=nodes[-1]
        out.append(p.val)
        nodes.pop(-1)
        print([i.val for i in nodes],out)
        if p.right!=None:
            nodes.append(p.right)
            p=p.right
        else:
            p=None
    return out


def bak(root):
    nodes=[]
    out=[]
    p=root
    node_tmp=[]
    while nodes!=[] or p!=None:
        while p!=None:
            nodes.append(p)
            p=p.left
        p=nodes[-1]
        if p.right !=None and p.right not in node_tmp :
            node_tmp.append(p.right)
            p=p.right
        else:
            print(p.val)
            nodes.pop(-1)
            p=None

    return out



t4 = TreeNode(4)
t5 = TreeNode(5)
t7 = TreeNode(7)
t10 = TreeNode(10)
t12 = TreeNode(12)


'''
        10
    5       12
4       7
'''

t5.left=t4
t5.right=t7

t10.left=t5
t10.right=t12


print(bak(t10))