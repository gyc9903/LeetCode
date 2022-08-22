# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-
"""
给你一个字符串 s，找到 s 中最长的回文子串。回文子串是正反顺序一致，即"abccba"是一整个回文子串

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
 
提示：
1 <= s.length <= 1000
s 仅由数字和英文字母组成1
"""

# class Solution(object):
#     """思路：中心扩散"""
#     def expandAroundCenter(self, s, left, right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return left + 1, right - 1
#
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         # 回文子串的起点和终点位置
#         start, end = 0, 0
#         for i in range(len(s)):
#             # 回文子串长度为单数
#             left1, right1 = self.expandAroundCenter(s, i, i)
#             # 回文子串长度为双数
#             left2, right2 = self.expandAroundCenter(s, i, i + 1)
#             if right1 - left1 > end - start:
#                 start, end = left1, right1
#             if right2 - left2 > end - start:
#                 start, end = left2, right2
#         print(start, end)
#         return s[start:end + 1]


class Solution(object):
    """中心扩散：超级快"""

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 如果整个字符串就是回文子串 或者 字符串长度较短，就直接返回
        if len(s) < 2 or s == s[::-1]:
            return s
        res = s[0]
        # 当前最长的回文子串长度
        maxlen = 1
        for i in range(1, len(s)):
            # 分奇偶两种情况，获取可能符合条件的字符串
            odd = s[i - maxlen - 1:i + 1]
            even = s[i - maxlen:i + 1]
            # 判断是否为回文子串
            if odd == odd[::-1] and i - maxlen - 1 >= 0:
                res = odd
                maxlen += 2  # 由于左右两边都扩展一个元素，则 maxlen+2
                continue
            if even == even[::-1] and i - maxlen >= 0:
                res = even
                maxlen += 1
                continue
        return res


words = "addavadda"
a = Solution().longestPalindrome(words)
print(a)
