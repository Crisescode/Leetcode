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


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return

        hash_dict = {}
        for num in nums:
            if num in hash_dict:
                hash_dict[num] += 1
            else:
                hash_dict[num] = 1

        for n in hash_dict:
            if hash_dict[n] == 1:
                return n


if __name__ == "__main__":
    nums, k = [99, 99], 2
    print(Solution2().containsNearbyDuplicate(nums, k))
