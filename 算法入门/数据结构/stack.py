# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


def brace_match(s):
    match = {'}': '{', ']': '[', ')': '('}
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:  # ch in {'}', ']', ')'}
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


print(brace_match('[{()}'))

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())  # 后进先出

# 20. 有效的括号
# class Solution:
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = []
#         map_ = {']': '[', ')': '(', '}': '{'}
#         for i in range(len(s)):
#             if s[i] in '([{':
#                 stack.append(s[i])
#             else:  # s[i] in ')]}'
#                 if not stack:
#                     return False
#                 elif stack.pop() != map_[s[i]]:
#                     return False
#         return len(stack) == 0
#
#
# s = Solution()
# print(s.isValid('[{()}]'))
