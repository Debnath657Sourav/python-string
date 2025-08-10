def reverse_doubly_linked_list(head):
    if not head: return None
    curr = head
    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        head = curr
        curr = curr.prev
    return head
