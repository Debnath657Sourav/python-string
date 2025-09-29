class Stack:
    def __init__(self, n):
        self.size = n
        self.stack = [None] * n
        self.top = -1

    def push(self, x):
        if self.top < self.size - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self):
        if self.top >= 0:
            self.top -= 1

    def peek(self):
        if self.top >= 0:
            return self.stack[self.top]
        else:
            return -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1
