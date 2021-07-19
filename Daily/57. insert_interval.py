#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 04/11/2020

# https://leetcode-cn.com/problems/insert-interval/
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example1:
# Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
# Output: [[1, 5], [6, 9]]
#
# Example2:
# Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
# Output: [[1, 2], [3, 10], [12, 16]]
#
# Example3:
# Input: intervals = [], newInterval = [2, 5]
# Output: [[2, 5]]
#
# Example4:
# Input: intervals = [[1, 5]], newInterval = [2, 3]
# Output: [[1, 5]]
#
# Example5:
# Input: intervals = [[1, 5]], newInterval = [2, 7]
# Output: [[1, 7]]
from Utils.timer_decorater import timer
from typing import List


@timer
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pass