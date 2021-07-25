#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/palindrome-linked-list/
# Given a singly linked list, determine if it is a palindrome.
# For example, Given Input: 1->2->3, Output will be: False.
# Given Input: 1->2->3->3->2->1, Output will be: True.
#
from LinkedList.utils.node import ListNode
from Utils.timer_decorater import timer


@timer
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        return vals == vals[::-1]


@timer
class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        slow = self.find_middle_node(head)
        reverse_listnode = self.reverse_listnode(slow.next)

        res = True
        init_pos = head
        rev_pos = reverse_listnode
        while res and rev_pos:
            if init_pos.val != rev_pos.val:
                res = False

            init_pos = init_pos.next
            rev_pos = rev_pos.next

        return res

    def find_middle_node(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse_listnode(self, head):
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


if __name__ == '__main__':
    l3 = l3_1 = ListNode(0)
    l3_1.next = ListNode(1)
    l3_1 = l3_1.next
    l3_1.next = ListNode(2)
    l3_1 = l3_1.next
    l3_1.next = ListNode(3)
    l3_1 = l3_1.next
    l3_1.next = ListNode(2)
    l3_1 = l3_1.next
    l3_1.next = ListNode(1)
    l3_1 = l3_1.next
    l3_1.next = ListNode(0)

    print(Solution().isPalindrome(l3))
    print(Solution2().isPalindrome(l3))
