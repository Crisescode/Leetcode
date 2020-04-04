#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/daily-temperatures/
# Given a list of daily temperatures T, return a list such that, for each day in the input,
# tells you how many days you would have to wait until a warmer temperature. If there is no
# future day for which this is possible, put 0 instead.
#
# For example:
# given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be
# [1, 1, 4, 2, 1, 1, 0, 0]
from utils.timer_decorater import timer


class Solution(object):
    @timer
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        counts = [0] * len(T)
        length = len(T)
        for i in range(length):
            for j in range(i + 1, length):
                if T[j] > T[i]:
                    counts[i] = j - i
                    break

        return counts


class Solution2(object):
    @timer
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        pass


if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(T))