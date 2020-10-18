#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
# For example, Given Input = [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output will be: 6, Because [4,-1,2,1] has the largest sum = 6.
# If you have figured out the O(n) solution, try coding another solution using the divide
# and conquer approach, which is more subtle.
#
from Utils.timer_decorater import timer


class Solution(object):
    @timer
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        maxContinuousSum = 0
        for num in nums:
            if maxContinuousSum > 0:
                maxContinuousSum += num
            else:
                maxContinuousSum = num
            maxSum = max(maxContinuousSum, maxSum)
        return maxSum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
