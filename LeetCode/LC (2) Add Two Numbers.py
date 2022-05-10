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
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            now.val = num%10
            num //= 10
            if l1 or l2 or num:
                now.next = ListNode()
                now = now.next
            else:
                break
        return result