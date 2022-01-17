#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
"""
Given the heads of two singly linked-lists headA and headB, return the node at which the
two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

...
"""

from typing import Union
from utils import ListNode


class Solution:
    def getIntersectionNode(
            self, headA: ListNode, headB: ListNode
    ) -> Union[ListNode, None]:
        linkedList_A = []
        A, B = headA, headB
        while headA:
            linkedList_A.insert(0, A)
            A = A.next

        while B:
            if B in linkedList_A:
                return B
            B = B.next

        return None


class Solution2:
    def getIntersectionNode(
            self, headA: ListNode, headB: ListNode
    ) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA

        return A


if __name__ == "__main__":
    l1_copy = l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(5)

    l2_copy = l2 = ListNode(5)
    l2.next = ListNode(4)
    l2.next.next = ListNode(10)
    l2.next.next.next = ListNode(2)
    l2.next.next.next.next = ListNode(1)

    print("l1: ", l1)
    print("l1 copy: ", l1_copy)
    print("l2: ", l2)

    # print(Solution().getIntersectionNode(l1, l3))
    print(Solution2().getIntersectionNode(l1_copy, l2_copy))
