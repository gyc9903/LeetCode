"""
https://leetcode.cn/problems/3sum-closest/
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。

示例 1：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
"""


class Solution(object):

    # def threeSumClosest(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     # 首先进行列表排序
    #     nums.sort()
    #     ans = nums[0] + nums[1] + nums[2]
    #     # 1.在列表 nums 中，进行遍历，每遍历一个值利用其下标i，形成一个固定值 nums[i]
    #     for i in range(len(nums)):
    #         # 2.再使用前指针指向 start = i + 1 处，后指针指向 end = nums.length - 1 处，也就是结尾处
    #         start = i + 1
    #         end = len(nums) - 1
    #         while start < end:
    #             tar = nums[start] + nums[end] + nums[i]
    #             # 3.根据 sum = nums[i] + nums[start] + nums[end] 的结果，判断 sum 与目标 target 的距离，如果更近则更新结果 ans
    #             if abs(target - tar) < abs(target - ans):
    #                 ans = tar
    #             # 4.同时判断 sum 与 target 的大小关系，因为列表有序，
    #             # 如果 sum > target 则 end--，如果 sum < target 则 start++，如果 sum == target 则说明距离为 0 直接返回结果
    #             elif tar > target:
    #                 end -= 1
    #             elif tar < target:
    #                 start += 1
    #             else:
    #                 return ans
    #     return ans

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = sum(nums[:3])

        for i in range(len(nums)):
            # 如果当前i的值和上一个值即i-1的值相等，那么没有必要再查找一次，直接跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            # 如果答案在left或right的相邻位置，直接替换节省时间
            if i < right - 1 and nums[i] + nums[right] + nums[right -
                                                              1] <= target:
                left = right - 1
            if i > left + 1 and nums[i] + nums[left] + nums[left +
                                                            1] >= target:
                right = left + 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(ans - target):
                    ans = s
                if s > target:
                    # right 与前一个值即right-1相等，那么再往前一步
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif s < target:
                    # left 与前一个值即 left+1 相等，那么再往后一步
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                else:
                    return target
        return ans


nums = [-1, 2, 1, -4]
target = 1
s = Solution().threeSumClosest(nums, target)
print(s)