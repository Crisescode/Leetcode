#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
# that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
"""
Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = []
    Output: []

Example 3:
    Input: nums = [0]
    Output: []
"""

from typing import List


# 方法一，暴力解法，直接超时，另寻他法了
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return []

        res = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if sorted([nums[i], nums[j], nums[k]]) not in res:
                            res.append(sorted([nums[i], nums[j], nums[k]]))

        return res


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
