# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        nodeA = headA
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
        lenB = 0
        nodeB = headB
        while nodeB:
            lenB += 1
            nodeB = nodeB.next
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next
        return self.compare(headA, headB)

    def compare(self, headA, headB):
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
