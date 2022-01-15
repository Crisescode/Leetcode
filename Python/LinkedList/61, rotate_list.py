#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/rotate-list/
# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.
#

"""
Example 1:

          1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
rotate 1: 6 -> 1 -> 2 -> 6 -> 3 -> 4 -> 5
rotate 2: 5 -> 6 -> 1 -> 2 -> 6 -> 3 -> 4

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

          0 -> 1 -> 2
rotate 1: 2 -> 0 -> 1
rotate 2: 1 -> 2 -> 0
rotate 3: 0 -> 1 -> 2
rotate 4: 2 -> 0 -> 1

Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

from typing import Optional
from utils import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> ListNode:
        if not head or not head.next:
            return head

        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        k %= count
        if k == 0:
            return head

        fast, slow = head, head
        while k:
            fast = fast.next
            k -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        newHead = slow.next
        slow.next = None
        fast.next = head

        return newHead


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().rotateRight(head, 2))

