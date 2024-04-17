class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums[i+1:]:
                return i, nums[i+1:].index(complement) + i + 1
