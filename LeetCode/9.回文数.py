# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x % 10 == 0 and x != 0:
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = x // 10
            print("revertedNumber:", revertedNumber, "、x:", x)

        return x == revertedNumber or x == revertedNumber // 10  # 数字长度分为 奇数 和 偶数 两种情况


num = 1221
so = Solution().isPalindrome(num)
print(so)
