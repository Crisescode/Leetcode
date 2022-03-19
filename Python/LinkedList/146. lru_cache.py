#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 12/09/20

# https://leetcode-cn.com/problems/lru-cache/
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


# 使用双向链表实现 LRU 缓存
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
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return

        if len(self.dict) == self.capacity:
            node = self.dummy_tail.prev
            self.remove(node)
            del self.dict[node.key]

        node = ListNode(key, value)
        self.insert(node)
        self.dict[key] = node

    def remove(self, node: ListNode):
        node.prev.next, node.next.prev = node.next, node.prev

    def insert(self, node: ListNode):
        head = self.dummy_head.next
        head.prev = node
        node.next = head
        self.dummy_head.next = node
        node.prev = self.dummy_head


# 使用栈实现 LRU 缓存
class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = list()
        self.cache = dict()

    def get(self, key: int):
        if key in self.cache:
            self.stack.remove(key)
            self.stack.insert(0, key)
            return self.cache[key]
        else:
            return -1

    def set(self, key: int, value: int):
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            self.stack.remove(key)
            self.stack.insert(0, key)
        elif len(self.cache) == self.capacity:
            need_to_del_key = self.stack.pop()
            self.cache.pop(need_to_del_key)

            self.stack.insert(0, key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.stack.insert(0, key)


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
