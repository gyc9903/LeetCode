# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-
import random


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):
        """递归"""
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):
        """非递归"""
        p = self.root
        if not p:  # 空数
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.lchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def pre_order(self, root):
        """前序遍历"""
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # print("前序遍历:", end='')
    # pre_order(root)  # 前序遍历:E,A,C,B,D,G,F,

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    # print("中序遍历:", end='')
    # in_order(root)  # A,B,C,D,E,G,F,

    def post_order(self, root):
        """后序遍历"""
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

    def __remove_node_1(self, node):
        # 情况1：如果要删除的节点是叶子节点：直接删除
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:  # node是他父亲的左孩子
            node.parent.lchild = None
        else:  # node是他父亲的右孩子
            node.parent.rchild = None

    def __remove_node_21(self, node):
        # 情况2：如果要删除的节点只有一个左孩子：将此节点的父亲与孩子连接，然后删除该节点。
        if not node.parent:  # 无父母，是根节点，删除后由左孩子做根节点
            self.root = node.lchild
            node.lchild.parent = None  # 根节点无父亲
        elif node == node.parent.lchild:  # node父亲的左孩子
            # 将此节点的父亲与孩子连接，双向连接
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:  # node是父亲的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # node只有一个右孩子
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:  # 不是空树
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            elif not node.rchild:  # 1.只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild:  # 2.只有一个右孩子
                self.__remove_node_22(node)
            else:  # 3.两个孩子都有，将其右子树的最小节点（该节点最多有一个右孩子）删除，并替换当前节点
                min_node = node.rchild  # 先进入右子树
                while min_node.lchild:  # 一直往左子树走，直到找出一个没有左孩子的根节点，此节点就是右子树中最小的节点
                    min_node = min_node.lchild
                node.data = min_node.data  # min_node替换到node上
                # 删除原min_node
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


li = list(range(0, 500, 2))
random.shuffle(li)

# tree = BST(li)
# print("前序遍历：")
# tree.pre_order(tree.root)
# print("\n中序遍历：")  # 升序遍历
# tree.in_order(tree.root)
# print("\n后序遍历：")
# tree.post_order(tree.root)
# print(tree.query_no_rec(3))

tree = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
print("\n中序遍历：")
tree.in_order(tree.root)
tree.delete(4)
print("\n中序遍历：")
tree.in_order(tree.root)
