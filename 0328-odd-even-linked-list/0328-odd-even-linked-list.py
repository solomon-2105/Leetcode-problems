class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd,even=head,head.next
        eve=even
        while even and even.next:
            odd.next,even.next=odd.next.next,even.next.next
            odd,even=odd.next,even.next
        odd.next=eve
        return head