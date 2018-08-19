class listnode:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        z1=pHead
        z2=pHead
        while z1!=None and z2!=None:
            try:
                z2=z2.next
                z2=z2.next
                z1=z1.next
                if z1==z2:
                    z1=pHead
                    return self.solution(z1,z2)
            except:
                return None
        return None
    def solution(self,p1,p2):
        while True:
            print(p1.val,p2.val)
            p1=p1.next
            p2=p2.next
            if p1==p2:
                return p1


s=Solution()

a1=listnode(1)
a2=listnode(2)
a3=listnode(3)
a4=listnode(4)
a5=listnode(5)
a6=listnode(6)
a7=listnode(7)
a8=listnode(8)
a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a5
a5.next=a6
a6.next=a7
a7.next=a8
a8.next=a7

print(s.EntryNodeOfLoop(a1))