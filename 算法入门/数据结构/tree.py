# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-


class Node:
    """树节点"""

    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type  # 'dir' or 'file'
        self.children = []  # 子节点
        self.parent = None  # 父节点
        # 链式存储

    def __repr__(self):
        return self.name


class FileSystemTree:
    """树状文件夹结构"""

    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        # name 以'/'结尾
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        # 新创建的节点添加到当前节点下作为目录
        self.now.children.append(node)
        # 当前节点就是新创建节点的父节点
        node.parent = self.now

    def ls(self):
        """展示当前目录下的所有目录"""
        return self.now.children

    def cd(self, name):
        """切换下一级目录"""
        if name[-1] != '/':
            name += '/'
        if name == '../':  # 打开上一级目录
            self.now = self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError("invalid dir")


tree = FileSystemTree()
tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('usr/')

tree.cd("bin/")
tree.mkdir('python/')
tree.cd('../')
print(tree.ls())
