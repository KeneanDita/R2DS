class Stack():
    def __init__(self):
        self.sta = list()
    def push(self, item):
        self.sta.append(item)
    def pop(self):
        if len(self.sta) > 0:
            return self.sta.pop()
        else:
            return None
    def peek(self):
        if len(self.sta) > 0:
            return self.sta[len(self.sta)-1]
        else:
            return None
    def __str__(self):
        return str(self.sta)


stu = Stack()
stu.push(2)
stu.push("ken")
print(stu)

print(stu.peek())