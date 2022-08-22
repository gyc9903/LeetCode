# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-
"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
 
示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"
 
提示：
1 <= s.length <= 1000
s 由英文字母（小写和大写）、',' 和 '.' 组成
1 <= numRows <= 1000

思路：
1.周期为2r-2
2.每个周期的第一行和最后一行只有一个字符，其余每个周期的每行只有两个字符
3.通过遍历每行，找到每行第一个字符
4.通过第一行的每个周期的第一个字符，该周期其余行的第二个字符
0             0+t                    0+2t                     0+3t
1      t-1    1+t            0+2t-1  1+2t            0+3t-1   1+3t
2  t-2        2+t  0+2t-2            2+2t  0+3t-2             2+3t
3             3+t                    3+2t                     3+3t
"""
from itertools import chain


class Solution(object):
    # def convert(self, s, numRows):
    #     """
    #     :type s: str
    #     :type numRows: int
    #     :rtype: str
    #     """
    #     n, r = len(s), numRows  # n:字符串长度；r:行数
    #     if r == 1 or r >= n:  # 只有一行
    #         return s
    #     t = 2 * r - 2  # 一个Z的周期是2r-2
    #     ans = []
    #     for i in range(r):  # 枚举矩阵的行
    #         for j in range(0, n - i, t):  # 枚举每个周期的起始下标
    #             ans.append(s[j + i])  # 当前周期的第一个字符，取第i行的值
    #             if 0 < i < r - 1 and j + t - i < n:  # 第一行和最后一行没有第二个字符，判断j+t-i是否在字符串s的范围内
    #                 print(s[j + t - i])  # 从每个周期的起点（s[j+t]）算起，再减掉当前行数，等于该周期该行的第二个字符
    #                 ans.append(s[j + t - i])  # 当前周期、当前行的第二个字符
    #     return ''.join(ans)

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        r = numRows
        if r == 1 or r >= len(s):
            return s
        mat = [[] for _ in range(r)]
        t = 2 * r - 2
        x = 0  # mat内的列表下标，每一个列表代表一行
        for i, ch in enumerate(s):
            mat[x].append(ch)
            # x += 1 if i % t < r - 1 else -1
            if i % t < r - 1:  # 如果 i % t < r - 1，就加一行 x+1
                x += 1
            else:
                x += -1
        return ''.join(chain(*mat))


s_str = 'PAYPALISHIRING'
s = Solution().convert(s_str, numRows=4)
print(s)  # PINALSIGYAHRPI
