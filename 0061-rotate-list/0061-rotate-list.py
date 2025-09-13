class Solution:
    def rotateRight(self,head:Optional[ListNode],k:int)->Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        n=1
        tail=head
        while tail.next:
            tail=tail.next
            n+=1
        k%=n
        if k==0:
            return head
        curr=head
        for _ in range(n-k-1):
            curr=curr.next
        new_head=curr.next
        curr.next=None
        tail.next=head
        return new_head