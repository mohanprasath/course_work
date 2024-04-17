class Solution:
    def numberOfSteps(self, num: int) -> int:
        return 2 * bin(num).count('1') + bin(num).count('0') - 1 - 1