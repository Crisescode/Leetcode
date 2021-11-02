#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/remove-linked-list-elements/
# Given the head of a linked list and an integer val, remove all the nodes of the linked list
# that has Node.val == val, and return the new head.
#

"""
Example:

1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6

Input: head = [1, 2, 6, 3, 4, 5, 6], val = 6
Output: [1, 2, 3, 4, 5]
"""

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head)
        cur = dummy_head

        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy_head.next


def traversal(head: ListNode) -> List[int]:
    vals = []

    if head is None:
        return vals

    while head:
        vals.append(head.val)
        head = head.next

    return vals


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(6)
    node.next.next.next = ListNode(3)
    node.next.next.next.next = ListNode(4)
    node.next.next.next.next.next = ListNode(5)
    node.next.next.next.next.next.next = ListNode(6)

    print(traversal(node))
    print(traversal(Solution().removeElements(node, 6)))
