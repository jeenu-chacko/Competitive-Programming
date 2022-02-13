class Solution:
    def reverseList(self,head):
        newHead=head
        if head.next:
            newHead=reverseList(head.next)
            head.next.next=head
        head.next = None

        return newHead
        