# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-


class Node:
    """链表"""

    def __init__(self, item):
        self.item = item
        self.next = None


# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
#
# # AttributeError: 'NoneType' object has no attribute 'item'
# print(a.next.next.next.item)

def create_linklist_head(li):
    """头插法：倒序"""
    head = Node(li[0])  # 传入头结点
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


def create_linklist_tail(li):
    """尾插法：正序"""
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end='、')
        lk = lk.next


lk1 = create_linklist_head([1, 2, 3])
lk2 = create_linklist_tail([1, 2, 3])
print_linklist(lk1)
print_linklist(lk2)
