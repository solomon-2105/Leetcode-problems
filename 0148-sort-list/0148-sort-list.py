# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        cur=head
        while cur:
            l.append(cur.val)
            cur=cur.next
        l.sort()
        curr=head
        i=0
        while curr:
            curr.val=l[i]
            i+=1
            curr=curr.next
        return head