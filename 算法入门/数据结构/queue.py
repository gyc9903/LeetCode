# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-


class Queue:
    def __init__(self, size):
        self.queue = [0 for _ in range(100)]
        self.size = size
        self.rear = 0  # 队尾
        self.front = 0  # 队首

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled!")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        raise IndexError("Queue is empty!")

    # 判断队空
    def is_empty(self):
        return self.rear == self.front

    # 判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(5)
for i in range(4):
    q.push(i)
print(q.pop())
q.push(4)

