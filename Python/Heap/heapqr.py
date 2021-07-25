import heapq

# first
"""
函数定义：
heapq.heappush(heap, item)
    - Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap)
    - Pop and return the smallest item from the heap, maintaining the heap invariant.
    If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
"""

nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)

print(heap[0])
print([heapq.heappop(heap) for _ in range(len(nums))])

# second
heapq.heapify(nums)
print([heapq.heappop(nums) for _ in range(len(nums))])


"""
函数定义：
heapq.merge(*iterables)
    - Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.
    - Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once, and assumes that each of the input streams is already sorted (smallest to largest).
"""
import itertools
nums1 = [32, 3, 5, 34, 54, 23, 132]
nums2 = [23, 2, 12, 656, 324, 23, 54]

print(sorted(itertools.chain(*[[num for num in nums1], [num for num in nums2]])))

nums1 = sorted(nums1)
nums2 = sorted(nums2)
print(list(heapq.merge(nums1, nums2)))



