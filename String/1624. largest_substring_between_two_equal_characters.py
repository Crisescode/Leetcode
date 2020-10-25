#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters/
# Given a string s, return the length of the longest substring between two equal characters,
# excluding the two characters. If there is no such substring return -1.
#
# A substring is a contiguous sequence of characters within a string.
#
'''
Example 1:
    Input: s = "aa"
    Output: 0
    Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
    Input: s = "abca"
    Output: 2
    Explanation: The optimal substring here is "bc".

Example 3:
    Input: s = "cbzxy"
    Output: -1
    Explanation: There are no characters that appear twice in s.

'''
from Utils.timer_decorater import timer


@timer
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s) == 1:
            return 0

        char_count = {}
        for c in s:
