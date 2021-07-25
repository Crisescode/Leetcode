#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 18/10/20

# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# For example, Given Input: head = [1, 2, 3, 4, 5], n = 2.
# Output: [1, 2, 3, 5].


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = ListNode()
        nodes.next = head

        quick = slow = nodes
        for _ in range(n):
            quick = quick.next
            print("q val: ", quick.val)

        while quick.next:
            slow = slow.next
            print("slow val: ", slow.val)
            quick = quick.next
            print("quick val: ", quick.val)

        slow.next = slow.next.next

        return nodes.next


if __name__ == "__main__":
    head = node = ListNode(1)
    node.next = ListNode(2)
    node = node.next
    node.next = ListNode(10)
    node = node.next
    node.next = ListNode(20)
    node = node.next
    node.next = ListNode(30)
    node = node.next

    print(Solution().removeNthFromEnd(head, 2))
