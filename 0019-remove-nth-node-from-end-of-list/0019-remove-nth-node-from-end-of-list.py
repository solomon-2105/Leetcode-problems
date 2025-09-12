class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        c=head
        while c:
            l+=1
            c=c.next
        p=l-n+1
        if p==1:
            return head.next
        c=head
        i=1
        while i<p-1:
            c=c.next
            i+=1
        c.next=c.next.next
        return head
