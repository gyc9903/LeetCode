# @Project: VSCODE_WORKSPACE
# !/user/bin/env python
# -*- encoding:utf-8 -*-

# 进阶：你能不将整数转为字符串来解决这个问题吗？


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


# class Solution(object):
#     def isPalindrome(self, x):
#         return bool(str(x) == str(x)[::-1])


num = 12321
so = Solution().isPalindrome(num)
print(so)
