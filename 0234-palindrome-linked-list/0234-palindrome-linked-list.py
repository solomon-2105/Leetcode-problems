# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        left=0
        right=len(a)-1
        while left<right:
            if a[left]!=a[right]:
                return False
            left+=1
            right-=1
        return True