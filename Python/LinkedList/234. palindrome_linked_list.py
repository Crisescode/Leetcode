#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/palindrome-linked-list/
# Given a singly linked list, determine if it is a palindrome.
# For example, Given Input: 1->2->3, Output will be: False.
# Given Input: 1->2->3->3->2->1, Output will be: True.
#
from utils import ListNode
from Utils.timer_decorater import timer


class Solution(object):
    # Time: o(n)
    # Space: o(n)
    @timer
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        data = []
        while head:
            data.append(head.val)
            head = head.next
        # flag = True
        # for i in range(len(data) // 2):
        #     if data[i] != data[len(data)-i-1]:
        #         flag = False

        # return flag
        return data == data[::-1]


class Solution2(object):
    @timer
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        slow_point = self.get_slowly_point(head)
        reverse_point = self.reverse_linked_list(slow_point.next)

        res = True
        first_position = head
        second_position = reverse_point
        while res and second_position is not None:
            if first_position.val != second_position.val:
                res = False
            first_position = first_position.next
            second_position = second_position.next

        return res

    def get_slowly_point(self, head):
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse_linked_list(self, head):
        curr, prev = head, None
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

