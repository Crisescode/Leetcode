#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 13/09/20

# https://leetcode-cn.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of
# each bar is 1, compute how much water it is able to trap after raining.
#
# Example:
# Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
#


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.dummy_head = ListNode(0, 0)
        self.dummy_tail = ListNode(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        node = self.dict[key]
        self.remove(node)
        self.append(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])

        node = ListNode(key, value)
        self.append(node)
        self.dict[key] = node

        if len(self.dict) > self.capacity:
            head = self.dummy_head.next
            self.remove(head)
            del self.dict[head.key]

    def remove(self, node: ListNode):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def append(self, node: ListNode):
        tail = self.dummy_tail.prev
        tail.next = node
        node.prev = tail
        self.dummy_tail.prev = node
        node.next = self.dummy_tail


if __name__ == "__main__":
    obj = LRUCache(2)
    print(obj.get(1))
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    obj.put(3, 3)
    print(obj.get(2))
    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
