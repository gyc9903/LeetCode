# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-


# 链表
class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __iter__(self):
            return self

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)  # 创建一个链表节点
        if not self.head:  # 如果链表为空
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):  # 转换成字符串 str(self)
        return "<<" + ", ".join(map(str, self)) + ">>"


# 类似集合的结构：哈希表每个位置都连接一个链表（拉链法）
class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]

    def h(self, k):
        """
        hash函数
        :param k: 存在哈希表中的值
        :return:
        """
        return k % self.size

    def find(self, k):
        i = self.h(k)  # i：哈希表中的位置
        return self.T[i].find(k)

    def insert(self, k):
        # 将i插入到k位置上
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert.")
        else:
            self.T[i].append(k)

    def delete(self, k):
        return


ht = HashTable()
ht.insert(0)
ht.insert(1)
# ht.insert(0)  # Duplicated Insert.
ht.insert(3)
ht.insert(102)
ht.insert(508)
print(",".join(map(str, ht.T)))
"""<<0>>,<<1, 102>>,<<>>,<<3, 508>>"""

print(ht.find(202))