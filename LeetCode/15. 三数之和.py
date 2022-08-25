# https://leetcode.cn/problems/3sum/
import bisect
from collections import defaultdict


class Solution(object):

    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     n = len(nums)
    #     nums.sort()
    #     ans = list()
    #     # 枚举a
    #     for first in range(n):
    #         # 需要和上一次枚举的数不同
    #         if first > 0 and nums[first] == nums[first - 1]:
    #             continue
    #         third = n - 1
    #         target = -nums[first]
    #         # 枚举b
    #         for second in range(first + 1, n):
    #             # 需要和上一次枚举的数不同
    #             if second > first + 1 and nums[second] == nums[second - 1]:
    #                 continue
    #             # 保证 指针b 在 指针c 的左侧
    #             while second < third and nums[second] + nums[third] > target:
    #                 third -= 1
    #             if second == third:
    #                 break
    #             if nums[second] + nums[third] == target:
    #                 ans.append([nums[first], nums[second], nums[third]])
    #     return ans

    def threeSum(self, nums):
        nums.sort()  # [-4, -1, -1, 0, 1, 2]
        if len(nums) < 3 or nums[-1] < 0 or nums[0] > 0:
            return []
        counts = defaultdict(int)
        # 统计每个数字的个数
        for i in nums:
            counts[i] += 1
        print(counts
              )  # defaultdict(<class 'int'>, {-4: 1, -1: 2, 0: 1, 1: 1, 2: 1})

        # 剔除重复数字再次排序
        nums = sorted(counts)  # [-4, -1, 0, 1, 2]
        res = []

        for i, num in enumerate(nums):
            # 枚举出第一个数字
            if counts[num] > 1:  # 该数字出现次数大于1
                if num == 0:
                    if counts[num] > 2:
                        res.append([0, 0, 0])
                elif -2 * num in counts:
                    res.append([num, num, -2 * num])

            if num < 0:
                two_sum = -num  # 剩余两数之和为第一个数字的相反数
                # 二分查找
                left = bisect.bisect_left(nums, two_sum - nums[-1], i + 1)
                # bisect.bisect_left(a, x, lo=0, hi=len(a)) 返回值是可以被放在 list.insert() 的第一个参数的。
                print("left: ", left, ";nums:", nums)
                a = nums[left:bisect.bisect_right(nums, two_sum // 2, left)]
                print(a)

                for i in a:
                    j = two_sum - i
                    if j in counts and j != i:
                        res.append([num, i, j])
        return res


nums = [2, 2, -1, -4, 3]  # -4 -1 2 2 3
# nums = [0, 0, 1]
s = Solution().threeSum(nums)
print(s)