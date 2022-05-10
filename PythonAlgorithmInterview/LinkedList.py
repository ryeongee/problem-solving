import collections
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def isPalindromeList(head) -> bool:
    q = []
    if not head:
        return True
    node = head
    i = 0
    while(node is not None):
        if(i == len(head)):
            break
        q.append(node[i])
        i += 1

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True

def isPalindromeDeque(head) -> bool:
    q = collections.deque()
    if not head:
        return True
    node = head
    i = 0
    while node is not None:
        if(i == len(head)):
            break
        q.append(node[i])
        i += 1
    while len(q) >1:
        if q.popleft() != q.pop():
            return False
    return True

def isPalindromeRunner(head) -> bool: 
    rev = None
    slow = fast = head
    # 런너를이용해역순연결리스트구성 
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next 
    if fast:
        slow = slow.next
    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next 
    return not rev
ipt = list(map(int, input().split("->")))

print(isPalindromeList(ipt))
print(isPalindromeDeque(ipt))

