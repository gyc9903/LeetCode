# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-

from collections import deque  # 引用队列 deque==dequeue


# q = deque(iterable=[1, 2, 3, 4, 5], maxlen=5)
# q.append(6)  # 此时队列长度超过maxlen，所以队首自动出队
# print(q.popleft())

# 队尾入队
# q.append(1)


# 队首出队
# print(q.popleft())
# print(q.popleft())  # IndexError: pop from an empty deque

# 用于双向队列
# q.appendleft(1)  # 队首进队
# q.pop()  # 队尾出队


def tail(n):
    with open('dequeue.txt', 'r') as f:
        q = deque(f, n)
        return q


for line in tail(5):
    print(line, end='')
