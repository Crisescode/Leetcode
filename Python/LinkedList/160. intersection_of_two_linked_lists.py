#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

...
"""

from utils.node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A.val != B.val:
            A = A.next if A else headB
            B = B.next if B else headA

        return A.val


if __name__ == "__main__":
    l3 = l3_1 = ListNode(0)
    l3_1.next = ListNode(1)
    l3_1 = l3_1.next
    l3_1.next = ListNode(2)
    l3_1 = l3_1.next
    l3_1.next = ListNode(3)

    l1 = l1_1 = ListNode(5)
    l1_1.next = ListNode(4)
    l1_1 = l1_1.next
    l1_1.next = ListNode(2)
    l1_1 = l1_1.next
    l1_1.next = ListNode(3)

    # print(Solution().getIntersectionNode(l1, l3))
    print(Solution2().getIntersectionNode(l1, l3))
