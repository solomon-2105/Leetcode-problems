# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    #     for i in nums:
    #         head=self.Brr(i,head)
    #     return head

    # def Brr(self,i,head):
    #     dummy=ListNode(0)
    #     dummy.next=head
    #     a=dummy
    #     while a.next is not None:
    #         if a.next.val==i:
    #             a.next=a.next.next
    #         else:
    #             a=a.next 
    #     return dummy.next
        dummy=ListNode(0)
        dummy.next=head
        a=dummy
        b=set(nums)
        while a.next is not None:
            if a.next.val in b:
                a.next=a.next.next
            else:
                a=a.next 
        return dummy.next