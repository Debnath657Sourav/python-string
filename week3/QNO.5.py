def kthFromEnd(head, k):
    fast = slow = head
    for _ in range(k):
        if not fast:
            return -1
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.data if slow else -1
