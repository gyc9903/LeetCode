# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-
from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e


# print(root.lchild.rchild.data)


def pre_order(root):
    """前序遍历"""
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)


# print("前序遍历:", end='')
# pre_order(root)  # 前序遍历:E,A,C,B,D,G,F,


def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)


# print("中序遍历:", end='')
# in_order(root)  # A,B,C,D,E,G,F,


def post_order(root):
    """后序遍历"""
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')


# print("后序遍历:", end='')
# post_order(root)  # B,D,C,A,F,G,E,


def level_order(root):
    queue = deque()  # 队列
    queue.append(root)
    while len(queue) > 0:  # 只要队不空
        node = queue.popleft()
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


print("层次遍历", end='')
level_order(root)  #
