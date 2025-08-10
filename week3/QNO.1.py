class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def delete_node_at_position(head, position):
    if not head:
        return None
    
   
    if position == 1:
        head = head.next
        if head:
            head.prev = None
        return head
    
    curr = head
    for _ in range(position - 1):
        curr = curr.next
        if not curr:
            return head  
    
    if curr.next:
        curr.next.prev = curr.prev
    if curr.prev:
        curr.prev.next = curr.next
    
    return head


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()


head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third

print("Original List:")
print_list(head)

head = delete_node_at_position(head, 3)  # Delete position 3
print("After Deletion:")
print_list(head)
