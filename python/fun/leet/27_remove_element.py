from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        total = right
        while left <= right:
            if nums[left] != val and nums[right] != val:
                left += 1
                print(f'left: {left}, right: {right} nums: {nums}')
            elif nums[left] == val:
                nums[left] = nums[right]
                nums[right] = -1
                right -= 1
                total -= 1
                print(f'left: {left}, right: {right} nums: {nums}')
            else:
                nums[right] = -1
                right -= 1
                total -= 1
                print(f'left: {left}, right: {right} nums: {nums}')
        return  left if left > right else left - 1

test = Solution().removeElement([2], 3)
print(test)