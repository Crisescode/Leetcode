#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is
# not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
#

"""
Example 1:
1 -> 2 -> 3 -> 4 -> 5

2 -> 1 -> 4 -> 3 -> 5

Input: head = [1, 2, 3, 4, 5], k = 2
Output: [2, 1, 4, 3, 5]
"""

from Utils.timer_decorater import timer
from utils import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass
