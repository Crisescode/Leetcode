# https://leetcode-cn.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# For example, Given nums = [2, 7, 11, 15], target = 9, return [0, 1], Because nums[0] + nums[1] = 2 + 7 = 9.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
from utils.timer_decorater import timer


class Solution:
    # Time: o(n^2)
    # Space: o(1)
    @timer
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2:
    # Time: o(n)
    # Space: o(1)
    @timer
    def twoSum(self, nums, target):
        nums_dict = {}
        for i, value in enumerate(nums):
            tmp = target - value
            if tmp in nums_dict:
                return [nums_dict[tmp], i]
            nums_dict[value] = i
        return None


if __name__ == "__main__":
    solu_1 = Solution()
    res = solu_1.twoSum([2, 4, 9, 1, 0, 5], 1)
    print(res)

    solu_2 = Solution2()
    result = solu_2.twoSum([2, 4, 9, 1, 0, 5], 1)
    print(result)

