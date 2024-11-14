from typing import List


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        result = dict()
        for num in nums:
            result[num] = 1
        for idx, key in enumerate(result.keys()):
            nums[idx] = key
        return len(result.keys())


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            print(f'i: {i}, j: {j} nums: {nums} nums[i]: {nums[i]}, nums[i-1]: {nums[i-1]} nums[j]: {nums[j]}')
            if nums[i] != nums[i-1]:
                print(f'nums[i]: {nums[i]}, nums[i-1]: {nums[i-1]}')
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1,1,2]))

    solution2 = Solution2()
    print(solution2.removeDuplicates([1,1,2]))
