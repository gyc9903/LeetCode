# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-
from 数据结构.bst import BiTreeNode, BST


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0  # balance factor:平衡度


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c
        # 仅插入情况
        p.bf = 0
        c.bf = 0
        return c  # 返回旋转后的根节点

    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c

        # 仅限插入情况
        p.bf = 0
        c.bf = 0
        return c  # 返回旋转后的根节点

    def rotate_right_left(self, p, c):
        g = c.lchild
        # 右旋
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g
        # 左旋
        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 变更bf
        if g.bf > 0:  # 右偏，key插入到s3上
            p.bf = -1
            c.bf = 0
        else:
            p.bf = 0
            c.bf = 1
        g.bf = 0
        return g  # 返回旋转后的根节点

    def rotate_left_right(self, p, c):
        # 左旋
        g = c.rchilde
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        # 右旋
        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新bf
        if g.bf < 0:  # key插到了s2上的
            p.bf = 1
            c.bf = 0
        else:
            p.bf = 0
            c.bf = -1
        g.bf = 0
        return g  # 返回旋转后的根节点

    def insert_no_rec(self, val):
        # 1.和BST一样，插入
        p = self.root
        if not p:  # 空数
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # node 存储插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:  # val==p.data，AVL不允许插入值相等的key
                return

        # 2.更新balance factor
        while node.parent:  # node.parent存在
            if node.parent.lchild == node:  # 传递是从左子树来的，左子树高度增加
                # 更新node.parent bf -= 1
                if node.parent.bf < 0:  # 原来node.parent.bf = -1，更新之后变成-2
                    # 做旋转
                    # 看node那边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    if node.bf > 0:  # 左右：左旋右旋
                        n = self.rotate_left_right(node.parent, node)
                    else:  # 左左，右旋
                        n = self.rotate_right(node.parent, node)
                    # 记得把n和g连起来
                elif node.parent.bf > 0:  # 原来node.parent.bf = 1，更新之后变成0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf = 0，更新之后变成-1
                    node.parent.bf = -1
                    node = node.parent  # node上移
                    continue

            else:  # 传递是从右子树来的，右子树高度增加
                # 更新node.parent.bf += 1
                if node.parent.bf > 0:  # 原来node.parent.bf = 1，更新之后变成2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    if node.bf > 0:  # node.bf = 1
                        n = self.rotate_left(node.parent, node)
                    else:  # node.bf = -1
                        # 获得当前子树的根节点
                        n = self.rotate_right_left(node.parent, node)
                elif node.bf < 0:
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = 1
                    node = node.parent
                    continue
            # 连接旋转后的子树
            n.parent = g  # n是当前子树的根节点
            if g:  # g不是空
                if node.parent == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break