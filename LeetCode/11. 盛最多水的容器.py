# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-
"""
https://leetcode.cn/problems/container-with-most-water/
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i])。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。

说明：你不能倾斜容器。

提示：
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


# 方法：双指针 https://leetcode.cn/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode-solution/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        ans = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            ans = max(ans, area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return ans


h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(h))
