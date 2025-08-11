def removeCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast: break
    else: return False
    slow = head
    if slow == fast:
        while fast.next != slow: fast = fast.next
    else:
        while slow.next != fast.next:
            slow, fast = slow.next, fast.next
    fast.next = None
    return True
