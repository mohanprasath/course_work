class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        r = x[::-1]
        return x == r