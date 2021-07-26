#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/climbing-stairs/
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution2:
    def climbStairs(self, n):
        if n <= 2:
            return n

        sum, one = 2, 1
        for i in range(2, n):
            sum = sum + one
            one = sum - one

        return sum


if __name__ == "__main__":
    print(Solution().climbStairs(5))
    print(Solution2().climbStairs(5))
