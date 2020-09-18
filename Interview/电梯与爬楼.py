import sys


class Solution:
    def find_floor(self, floor, nums):
        res = [0 for i in range(floor)]
        min_res, min_index = sys.maxsize, 0

        for i in range(floor):
            for j in range(len(nums)):
                res[i] += abs(i - nums[j])

            if min_res > res[i]:
                min_res = res[i]
                min_index = i

        print(min_res)
        print(min_index)


if __name__ == "__main__":
    Solution().find_floor(10, [1, 3, 8, 10, 9])
