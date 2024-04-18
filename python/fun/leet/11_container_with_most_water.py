class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        length = len(height)
        for i, h in enumerate(height, start=1):
            temp = (length - i) * min(h, height[-1])
            if temp > max_val:
                max_val = temp
            print(i, (length - i), h, height[-1], max_val)
        return max_val
