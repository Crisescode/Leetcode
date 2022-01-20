#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/next-permutation/
# Implement next permutation, which rearranges numbers into the lexicographically next
# greater permutation of numbers.
# If such an arrangement is impossible, it must rearrange it to the lowest possible order
# (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.
#
"""
Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]

Example 2:
    Input: nums = [3,2,1]
    Output: [1,2,3]

Example 3:
    Input: nums = [1,1,5]
    Output: [1,5,1]
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1, 0, -1):
            print(nums[i])
        #     # 对应第3部，找到下标l的位置,这里 l == i-1
        #     if nums[i - 1] < nums[i]:
        #         for j in range(len(nums) - 1, i - 1, -1):
        #             # 对应第4步找到下标r，这里 r == j
        #             # 然后交换 下标l 与 下标r 的值
        #             if nums[j] > nums[i - 1]:
        #                 nums[i - 1], nums[j] = nums[j], nums[i - 1]
        #                 break
        #         # 对应第6步，反转下标l后的子序列
        #         for j in range((len(nums) - i + 1) // 2):
        #             nums[i + j], nums[len(nums) - 1 - j] = nums[len(nums) - 1 - j], nums[i + j]
        #         return nums
        # nums.reverse()
        # return nums


if __name__ == "__main__":
    print(Solution().nextPermutation([1, 2, 3]))
