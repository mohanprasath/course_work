class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        location = dict()
        for i, num in enumerate(nums):
            if target - num in location:
                return [i, location[target-num]]
            location[num] = i
