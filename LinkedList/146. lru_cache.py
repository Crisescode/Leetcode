#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 12/09/20

# https://leetcode-cn.com/problems/palindrome-linked-list/
# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
#
# For example, Given Input: 1->2->3, Output will be: False.
# Given Input: 1->2->3->3->2->1, Output will be: True.
# get(key) - Get the value (will always be positive) of the key if the key exists
# in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used
# item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
"""
Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1);
lRUCache.put(2, 2);
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // evicts key 2
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // evicts key 1
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

"""


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
