class Solution(object):

    # def longestCommonPrefix(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """

    #     def isCommonPrefix(length):
    #         # 获取第一个str，并与后面的str比较前缀
    #         str0, count = strs[0][:length], len(strs)
    #         return all(strs[i][:length] == str0 for i in range(1, count))

    #     if not strs:
    #         return ""
    #     # 获取strs中最小的str
    #     minlength = min(len(s) for s in strs)
    #     low, high = 0, minlength
    #     while low < high:
    #         mid = (high - low + 1) // 2 + low
    #         if isCommonPrefix(mid):
    #             low = mid
    #         else:
    #             high = mid - 1
    #     return strs[0][:low]

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        s1 = max(strs)  #选出最长和最短的字符串
        s2 = min(strs)
        print(s1)
        print(s2)
        for i, s in enumerate(s2):  #i是序号，s是值，这里用enumerate把s2转化为数组。
            if s != s1[i]:
                return s2[:i]  #一直判断到不等就可以了，不需要累加。
        return s2


strs = ["flower", "flow", "flight"]
s = Solution().longestCommonPrefix(strs)
print(s)