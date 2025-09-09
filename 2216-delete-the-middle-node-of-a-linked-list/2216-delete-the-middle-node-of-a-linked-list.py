# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None or head.next is None:
    #         return None
    #     size=self.length(head)
    #     brr=size//2
    #     cur=head
    #     for _ in range(brr-1):
    #         cur=cur.next
    #     cur.next=cur.next.next
    #     return head

    # def length(self,head):
    #     cur=head
    #     count=0
    #     while cur is not None:
    #         count+=1
    #         cur=cur.next
    #     return count
        if head is None or head.next is None:
            return None
        fast,slow=head,head
        prev=None
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head