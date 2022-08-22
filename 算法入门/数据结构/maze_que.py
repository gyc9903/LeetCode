# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-
from collections import deque

"""
队列—迷宫问题
    找出最短的那条路
"""
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
dirs = [  # x,y 四个方向 x-1,y; x+1,y; x,y-1; x,y+1
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x, y - 1),
]


def print_r(path):
    real_path = []
    i = len(path) - 1
    while i >= 0:
        real_path.append(path[i][0:2])  # 存储当前节点在maze中的坐标
        # 将i值修改为前一个节点在path列表中的位置
        i = path[i][2]
    real_path.reverse()
    for node in real_path:
        print('->', node, end='')


def maze_path_queue(x1, y1, x2, y2):
    queue = deque()  # 队列 存储正在走的节点
    path = []  # 存储出队的节点
    queue.append((x1, y1, -1))  # 队列 前两个元素存储在maze中的坐标、第三个元素存储path列表中的位置
    while len(queue) > 0:  # 当队列不空时循环
        # 1.将当前节点从队列中删除并添加到path列表中
        cur_node = queue.popleft()
        path.append(cur_node)
        if cur_node[0] == x2 and cur_node[1] == y2:
            # 到达终点
            print_r(path)
            return True
        for d in dirs:
            # 获取下一个节点
            next_node = d(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                # 如果节点可以走，就添加到队列中
                queue.append((next_node[0], next_node[1], len(path) - 1))
                maze[next_node[0]][next_node[1]] = 2  # 标记为已走过
    return False


maze_path_queue(1, 1, 8, 8)
