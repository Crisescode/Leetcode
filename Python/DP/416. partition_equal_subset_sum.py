#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/partition-equal-subset-sum/
# Given a non-empty array nums containing only positive integers, find if the
# array can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
#
"""
Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 == 1:
            return False
        target = target // 2

        dp = [0] * 10001
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        return target == dp[target]


if __name__ == "__main__":
    print(Solution().canPartition([1, 5, 5, 11]))
