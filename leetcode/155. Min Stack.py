class MinStack(object):

    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)

    def pop(self):
        self.list.pop()

    def top(self):
        return self.list[len(self.list) - 1]

    def getMin(self):
        return min(self.list)


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_4 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_5 = obj.getMin()
