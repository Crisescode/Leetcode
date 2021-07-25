#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 13/09/20

# https://leetcode-cn.com/problems/longest-increasing-subsequence/
# Given an unsorted array of integers, find the length of longest increasing subsequence.
# For example, Given Input: [10, 9, 2, 5, 3, 7, 101, 18], Output will be: 4.
#
# Explanation: The longest increasing subsequence is [2, 3, 7, 101],
# therefore the length is 4.
#

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
