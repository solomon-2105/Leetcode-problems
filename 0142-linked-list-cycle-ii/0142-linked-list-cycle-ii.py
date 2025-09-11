# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s,f=head,head
        while f and f.next:
            s=s.next
            f=f.next.next
            if s==f: break
        else: return None
        f=head
        while f!=s:
            f=f.next
            s=s.next
        return s
        