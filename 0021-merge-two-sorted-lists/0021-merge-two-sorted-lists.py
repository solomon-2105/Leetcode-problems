# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy=ListNode()
        # cur=dummy
        # while l1 and l2:
        #     if l1.val>l2.val:
        #         cur.next=l2
        #         l2=l2.next
        #     else:
        #         cur.next=l1
        #         l1=l1.next
        #     cur=cur.next
        # if l1:
        #     cur.next=l1
        # else:
        #     cur.next=l2
        # return dummy.next
        if not l1 or not l2:
            return l1 if l1  else l2
        if l1.val>l2.val:
            l1,l2=l2,l1
        l1.next=self.mergeTwoLists(l1.next,l2)
        return l1