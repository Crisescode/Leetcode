#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/maximum-profit-in-job-scheduling/
# We have n jobs, where every job is scheduled to be done from startTime[i]
# to endTime[i], obtaining a profit of profit[i].
#
# You're given the startTime , endTime and profit arrays, you need to output
# the maximum profit you can take such that there are no 2 jobs in the subset 
# with overlapping time range.
#
# If you choose a job that ends at time X you will be able to start
# another job that starts at time X.

# For example:
# Input: startTime = [1, 2, 3, 4], endTime = [3, 4, 5, 6],
# profit = [50, 10, 40, 70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.


from typing import List


class Solution:
    def jobScheduling(
            self,
            startTime: List[int],
            endTime: List[int],
            profit: List[int]
    ) -> int:
        pass
