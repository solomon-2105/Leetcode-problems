# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         s=[]
#         current=head
#         while current is  not None:
#             s.append(current.val)
#             current=current.next
#         cur=head
#         while cur is not None:
#             cur.val=s.pop()
#             cur=cur.next
#         return head

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev=None
        # current=head
        # while current:
        #     nxt=current.next
        #     current.next=prev
        #     prev=current
        #     current=nxt
        # return prev
        def brr(current,prev):
            if current is None:
                return prev
            nxt=current.next
            current.next=prev
            return brr(nxt,current)
        return brr(head,None)

