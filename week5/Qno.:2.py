class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
      
    def pop(self):
        if self.top is None:
            return -1
        val = self.top.data
        self.top = self.top.next
        self.count -= 1
        return val

    def peek(self):
        if self.top is None:
            return -1
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def size(self):
        return self.count

if __name__ == "__main__":
    s = Stack()
    queries = [
        [1, 10],  
        [1, 20],   
        [3],       
        [2],
        [3],      
        [4],       
        [5]       
    ]
    
    for q in queries:
        if q[0] == 1: 
            s.push(q[1])
        elif q[0] == 2:  
            print(s.pop())
        elif q[0] == 3:  
            print(s.peek())
        elif q[0] == 4: 
            print(s.isEmpty())
        elif q[0] == 5:  
            print(s.size())
