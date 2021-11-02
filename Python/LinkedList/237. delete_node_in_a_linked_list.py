#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/delete-node-in-a-linked-list/
# Write a function to delete a node in a singly-linked list. You will not be given access to
# the head of the list, instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.
#
"""
For example:
    4 -> 5 -> 1 -> 9
      delete

    4 -> 1 -> 9

Input: head = [4, 5, 1, 9], node = 5
Output: [4, 1, 9]

"""


class Solution:
    def deleteNode(self, node):
        """

        :param node: ListNode
        :return: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next
