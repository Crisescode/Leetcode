#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/merge-k-sorted-lists/
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#

"""
Example 1:

    Input: [[1, 4, 5], [1, 3, 4], [2, 6]]
    Output: [1, 1, 2, 3, 4, 4, 5, 6]

Example 2:

    Input: lists = []
    Output: []

Example 3:

    Input: lists = [[]]
    Output: []
"""

from typing import List, Optional
from utils import ListNode


# 方法一：两两排序，类暴力解法
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:
        if not lists:
            return None

        res = None
        for item in lists:
            res = self.mergeTwoLists(res, item)

        return res

    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]):
        dummy = ListNode(0)
        move = dummy

        while node1 and node2:
            if node1.val < node2.val:
                move.next = node1
                node1 = node1.next
            else:
                move.next = node2
                node2 = node2.next

            move = move.next
        move.next = node1 or node2

        return dummy.next


# 方法二：归并合并
class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:
        if not lists:
            return None

        return self.mergeSort(lists, 0, len(lists) - 1)

    def mergeSort(self, node_lists: List[ListNode], left: int, right: int) -> ListNode:
        if left == right:
            return node_lists[left]

        mid = (left + right) // 2
        left_node_lists = self.mergeSort(node_lists, left, mid)
        right_node_lists = self.mergeSort(node_lists, mid + 1, right)

        return self.mergeTwoLists(left_node_lists, right_node_lists)

    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]):
        dummy = ListNode(0)
        move = dummy

        while node1 and node2:
            if node1.val < node2.val:
                move.next = node1
                node1 = node1.next
            else:
                move.next = node2
                node2 = node2.next

            move = move.next
        move.next = node1 or node2

        return dummy.next


# 方法三：最小堆
class Solution3:
    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:
        import heapq
        minHeap = []
        for list_item in lists:
            while list_item:
                heapq.heappush(minHeap, list_item.val)
                list_item = list_item.next

        print("min heap", minHeap)
        dummy = ListNode(0)
        p = dummy
        while minHeap:
            v = heapq.heappop(minHeap)
            print("val: ", v)
            p.next = ListNode(v)
            p = p.next

        return dummy.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node1.next = ListNode(4)
    node1.next.next = ListNode(5)

    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)

    node3 = ListNode(2)
    node3.next = ListNode(6)

    # print(Solution().mergeKLists([node1, node2, node3]))
    # print(Solution2().mergeKLists([node1, node2, node3]))
    print(Solution3().mergeKLists([node1, node2, node3]))
