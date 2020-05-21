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
        profit_time_range = []

        for index in range(len(profit)):
            start = startTime[index]
            end = endTime[index]
            pay = profit[index]
            profit_time_range.append((start, end, pay))

        print(profit_time_range)

        count = []
        for i in range(len(profit_time_range)):
            for j in range(i, len(profit_time_range)):
                if profit_time_range[j][0] >= profit_time_range[i][1]:
                    count.append((profit_time_range[i], profit_time_range[j]))
        print(count)


if __name__ == "__main__":
    start_time = [1, 2, 3, 4, 6]
    end_time = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    import itertools

    # H = sorted(zip(start_time, itertools.repeat(1), end_time, profit))
    # print(H)
    # res = 0
    # import heapq
    # while H:
    #     t = heapq.heappop(H)
    #     print(t)
    #     if t[1]:
    #         heapq.heappush(H, (t[2], 0, res + t[3]))
    #     else:
    #         res = max(res, t[2])
    # print(res)
    import bisect
    jobs = sorted(zip(start_time, end_time, profit), key=lambda v: v[1])
    print(jobs)
    dp = [[0, 0]]
    for s, e, p in jobs:
        # bisect.insort(dp, [s + 1])
        # print(dp)
        i = bisect.bisect(dp, [s + 1]) - 1
        print(i)
        print(dp)
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])

    # print(dp[-1][1])

    # Solution().jobScheduling(start_time, end_time, profit)
