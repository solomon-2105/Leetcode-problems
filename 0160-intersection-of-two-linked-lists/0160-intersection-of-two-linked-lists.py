# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        p1,p2=headA,headB
        while p1!=p2:
            p1=p1.next if p1 else headB
            p2=p2.next if p2 else headA
        return p1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def getIntersectionNode(self,A,B):
#         s=set()
#         while A:s.add(A);A=A.next
#         while B:
#             if B in s:return B
#             B=B.next
#         return None