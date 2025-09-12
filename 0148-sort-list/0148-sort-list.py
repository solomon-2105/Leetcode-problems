# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         l=[]
#         cur=head
#         while cur:
#             l.append(cur.val)
#             cur=cur.next
#         l.sort()
#         curr=head
#         i=0
#         while curr:
#             curr.val=l[i]
#             i+=1
#             curr=curr.next
#         return head
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        s,f=head,head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        m=s.next
        s.next=None
        l=self.sortList(head)
        r=self.sortList(m)
        return self.merge(l,r)
    def merge(self,a,b):
        d=ListNode()
        c=d
        while a and b:
            if a.val<b.val:
                c.next=a
                a=a.next
            else:
                c.next=b
                b=b.next
            c=c.next
        c.next=a if a else b
        return d.next