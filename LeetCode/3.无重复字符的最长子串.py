# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-
"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 
提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""


class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     start = 0
    #     end = 1
    #     res = 0  # 无重复字符穿的最长子串长度
    #     if len(s) == len(set(s)):
    #         return len(s)
    #     while end <= len(s):
    #         st = s[start:end]
    #         if len(st) == len(set(st)):
    #             end += 1
    #             res += 1
    #         else:
    #             start += 1
    #             end += 1
    #     return res

    def lengthOfLongestSubstring(self, s):
        """
        滑动窗口的思路（最快）
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0  # 无重复字符穿的最长子串长度
        left = -1  # 最长子串的首元素的位置
        for index, word in enumerate(s):
            # 字符和字符位置存储到字典中
            if word in dic.keys():
                # 如果元素重复，就移动首元素下标
                left = max(left, dic[word])
            dic[word] = index
            res = max(res, index - left)
        return res


li = Solution().lengthOfLongestSubstring("abcaacvb")
print(li)
