# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        now = result
        num = 0

        while(True):
            if l1:
                num += l1.val
                # move next node
                l1 = l1.next
            if l2:
                num += l2.val
                # move next node
                l2 = l2.next
            # input value
            now.val = num % 10
            # carry
            num //= 10
            if l1 or l2 or num:
                # init & move next node
                now.next = ListNode()
                now = now.next
            else:
                break
        return result
