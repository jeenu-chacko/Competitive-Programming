#iterative method

class Solution:
    def reverseList(self,head):
        pre, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre