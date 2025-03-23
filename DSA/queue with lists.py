from collections import deque

class Queue:
    def __init__(self):
        self.st = deque()
    def push(self, item):
        self.st.append(item)
    def pop(self):
        if len(self.st) > 0:
            return self.st.popleft()
        else:
            return None
    def __str__(self):
        return str(self.st)

ren = Queue()
ren.push(3)
ren.push(45)
print(ren.pop())