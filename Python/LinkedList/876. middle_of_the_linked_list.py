#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/binary-tree-pruning/
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
#

"""
Example:

1 -> 2 -> 3 -> 4 -> 5

    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

1 -> 2 -> 3 -> 4 -> 5 -> 6

    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

from utils import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


if __name__ == "__main__":
    node = head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(head)
    print(Solution().middleNode(node))
