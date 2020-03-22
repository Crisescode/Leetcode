#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/valid-parentheses/
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# For example, Given Input = "()[{}]", output will be True. Given Input = "([})", Output will be False.
#
from utils.timer_decorater import timer


class Solution(object):
    @timer
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        data = []

        for sc in s:
            if sc in bracket_dict:
                data.append(sc)
                continue
            if data and sc == bracket_dict[data[-1]]:
                data.pop()
            else:
                return False

        return True if not data else False


if __name__ == "__main__":
    input_str = '(([{}]))'
    print(Solution().isValid(input_str))
