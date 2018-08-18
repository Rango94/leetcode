class tree:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None


        '''
         1
        2 3
       4   5
        '''

t1=tree(1)
t2=tree(2)
t3=tree(3)
t4=tree(4)
t5=tree(5)


# t2.left=t4
# t3.right=t5
# t1.left=t2
# t1.right=t3

t1.left=t2
t1.right=t3
t2.left=t4
t3.right=t5


print(t1.left.left.val)
print(t1.right.right.val)