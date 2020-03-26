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


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
obj.push(3)
obj.push(-2)
obj.push(0)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print(param_3)
print(param_4)
