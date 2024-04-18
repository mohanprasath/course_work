class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        result = dict()
        for num in nums:
            result[num] = 1
        for idx, key in enumerate(result.keys()):
            nums[idx] = key
        return len(result.keys())


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1,1,2]))