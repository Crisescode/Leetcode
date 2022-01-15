#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/reverse-linked-list-ii/
# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.
#

"""
Example:

1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6


Input: head = [1, 2, 6, 3, 4, 5, 6], left = 2, right = 5
Output: [1, 4, 3, 6, 2, 5, 6]
"""

from utils import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or head.next is None:
            return head

        idx = 0
        node = head

        while node and node.next:
            idx += 1
            if idx == left:
                tmp = node.next

