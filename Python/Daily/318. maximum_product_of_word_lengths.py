#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/maximum-product-of-word-lengths/
# Given a string array words, return the maximum value of length(word[i]) * length(word[j])
# where the two words do not share common letters. If no such two words exist, return 0.
#
"""
Example 1:
    Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16
    Explanation: The two words can be "abcw", "xtfn".

Example 2:
    Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
    Output: 4
    Explanation: The two words can be "ab", "cd".

Example 3:
    Input: words = ["a","aa","aaa","aaaa"]
    Output: 0
    Explanation: No such pair of words.

"""

from typing import List


class Solution:
    def maxProuct(self, words: List[str]) -> int:
        ans = 0
        for idx, word in enumerate(words):
            for jdx in range(idx + 1, len(words)):
                if not set(word) & set(words[jdx]):
                    ans = max(ans, len(word) * len(words[jdx]))

        return ans


if __name__ == "__main__":
    ex1 = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    ex2 = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    ex3 = ["a", "aa", "aaa", "aaaa"]
    print(Solution().maxProuct(ex3))
