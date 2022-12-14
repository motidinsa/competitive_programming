class MyQueue(object):

    def __init__(self):
        self.list = []

    def push(self, x):
        self.list.append(x)

    def pop(self):
        x = self.list[0]
        self.list.remove(x)
        return x

    def peek(self):
        return self.list[0]

    def empty(self):
        return len(self.list) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
