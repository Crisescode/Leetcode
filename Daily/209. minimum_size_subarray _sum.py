#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/minimum-size-subarray-sum/
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there
# isn't one, return 0 instead.
# For example, Given Input: s = 7, nums = [2, 3, 1, 2, 4, 3],
# Output will be: 2, Because the subarray [4,3] has the minimal length under
# the problem constraint.
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n).
#
from utils.timer_decorater import timer
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        pass
