class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_in_middle(head, x):
    new_node = Node(x)
    if not head:
        return new_node
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    new_node.next = slow.next
    slow.next = new_node
    return head

