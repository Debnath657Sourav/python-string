class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, x):
    new_node = Node(x)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head
