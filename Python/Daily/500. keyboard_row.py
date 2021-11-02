#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/keyboard-row/
# Given an array of strings words, return the words that can be typed using letters of the alphabet on
# only one row of American keyboard like the image below.
#
#
"""
Example:
    Input: words = ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]
"""

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_map = {
            1: "qwertyuiop",
            2: "asdfghjkl",
            3: "zxcvbnm",
        }

        vals = []
        if not words:
            return vals

        chars = [[c for c in word] for word in words]
        print(chars)

        for key, val in keyboard_map.items():
            for char in chars:
                if all([True if c.lower() in val else False for c in char]):
                    vals.append("".join(char))

        return vals


class Solution2:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_map = {
            1: set("qwertyuiop"),
            2: set("asdfghjkl"),
            3: set("zxcvbnm"),
        }

        vals = []
        if not words:
            return vals

        for _, val in keyboard_map.items():
            for word in words:
                if set(word.lower()) <= val:
                    vals.append(word)

        return vals


if __name__ == "__main__":
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
    print(Solution2().findWords(["Hello", "Alaska", "Dad", "Peace"]))
