class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1]
        result = 0
        if '-' in s:
            result= int('-' + s.replace('-', ''))
        else:
            result = int(s)
        return result if result.bit_length() < 32 else 0 