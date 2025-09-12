class Solution:
    def addTwoNumbers(self,l1,l2):
        d=ListNode(0)
        c=d
        f=0
        while l1 or l2 or f:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            s=x+y+f
            f=s//10
            c.next=ListNode(s%10)
            c=c.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return d.next
