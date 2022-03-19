#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/
"""
Given an integer array nums, you need to find one continuous subarray that if you only
sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:
    Input: nums = [2,6,4,8,10,9,15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
    Input: nums = [1,2,3,4]
    Output: 0

Example 3:
    Input: nums = [1]
    Output: 0
"""

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        sorted_nums = sorted(nums)
        if nums == sorted_nums:
            return 0

        left_idx = right_idx = 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                left_idx = i
                break

        for r_idx in range(len(nums) - 1, -1, -1):
            if nums[r_idx] != sorted_nums[r_idx]:
                right_idx = r_idx
                break

        if right_idx > left_idx:
            return right_idx - left_idx + 1


if __name__ == "__main__":
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(Solution().findUnsortedSubarray(nums))
