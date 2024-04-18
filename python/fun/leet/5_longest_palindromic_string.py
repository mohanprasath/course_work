class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        result = dict()
        for num in nums:
            result[num] = 1
        return len(result.keys())#, list(result.keys())