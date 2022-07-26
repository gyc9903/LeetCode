# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-
"""题目描述：

给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()  # 先设置一个头结点，这个链表是用来存储l1和l2的和的
        cur = head  # 因为第一个结点只能是头结点，
        # 所有当前结点为头结点，为什么不用head?因为后面要新增加后面的结点，
        # 如果后面的结点也用head来表示那么最后就不能返回完整的链表了
        values, up = 0, 0  # 设置两个变量来存储每一位相加的和与进位的数
        while l1 or l2:  # 只要有一个链表没有遍历完，就继续遍历
            if not l1:  # 表示l1已经遍历完了，这里就只对l2对应的位进行遍历计算
                values = l2.val + up
                l2 = l2.next
            elif not l2:  # 如上同理
                values = l1.val + up
                l1 = l1.next
            else:  # 如上同理
                values = l1.val + l2.val + up
                l1 = l1.next
                l2 = l2.next
            values, up = values % 10, values // 10  # 对每一位加好的数进行处理
            cur.next = ListNode(values)  # 创建下一个结点
            cur = cur.next  # 移动当前结点

        if up:  # l1,l2循环完毕，检查最后一位是否进位
            cur.next = ListNode(up)  # 如果有进位，创建新的结点
        return head.next


# 调用上述方法（非常重要）
a = ListNode(2)
b = ListNode(4)
c = ListNode(6)
a.next = b
b.next = c

e = ListNode(5)
f = ListNode(6)
g = ListNode(4)
e.next = f
f.next = g


def linklist(lk):
    li = []
    while lk:
        # print(lk.val, end='、')
        li.append(lk.val)
        lk = lk.next
    return li


t = Solution().addTwoNumbers(a, e)
print(linklist(a))
print(linklist(e))
t = linklist(t)
t.reverse()
print("".join(map(str, t)))
