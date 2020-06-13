from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        flag = False
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(j - i) <= k:
                    flag = True

        return flag


class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        arrs = {}
        for i in range(len(nums)):
            if nums[i] in arrs and abs(i - arrs[nums[i]]) <=k:
                return True
            arrs[nums[i]] = i

        return False


if __name__ == "__main__":
    nums, k = [99, 99], 2
    print(Solution2().containsNearbyDuplicate(nums, k))
