# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-
"""
栈——迷宫问题
    用栈可以用最快的时间找出一条路，但不一定是最短的那条
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


def maze_path(x1, y1, x2, y2):  # (x1,y1)是起点，(x2,y2)是终点
    # 存放路径
    path = list()  # 创建一个列表作为存储路径的栈stack
    path.append((x1, y1))  # 以集合存储节点作为走过的路径
    while len(path) > 0:
        cur_node = path[-1]  # 当前节点
        if cur_node[0] == x2 and cur_node[1] == y2:  # 走到终点了
            for p in path:
                print('->', p, end='')
            return True
        # x,y 四个方向 x-1,y; x+1,y; x,y-1; x,y+1
        for d in dirs:  # 按右左上下顺序判断
            # 以当前节点为基准，走下一步
            next_node = d(cur_node[0], cur_node[1])
            # 如果下一个节点能走
            if maze[next_node[0]][next_node[1]] == 0:
                path.append(next_node)
                maze[next_node[0]][next_node[1]] = 2  # 2表示走过的路
                break
        else:  # 找不到能走的节点
            maze[next_node[0]][next_node[1]] = 2
            path.pop()
    else:
        print("没有路")
        return False


maze_path(1, 1, 8, 8)
