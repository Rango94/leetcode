class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        p=self
        while p!=None:
            print(p.val)
            p=p.next


class Solution:
    def deleteDuplication(self, pHead):
        if pHead==None:
            return None
        out_pHead=None
        out=None
        cur=pHead
        nex=pHead.next
        while nex!=None:
            while nex.val==cur.val:
                cur=cur.next
                nex=nex.next
            if out ==None:
                out_pHead=ListNode(cur.val)
                out=out_pHead
            else:
                print(cur.val)
                out.nex=ListNode(cur.val)
                out=out.nex
            cur=cur.next
            nex=nex.next
        return out_pHead
    

a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(3)
a4=ListNode(3)
a5=ListNode(4)
a6=ListNode(4)
a7=ListNode(5)
a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a5
a5.next=a6
a6.next=a7
s=Solution()
s.deleteDuplication(a1).print()
