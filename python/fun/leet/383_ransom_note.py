class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_ransom = [0] * 26
        hash_magazine = [0] * 26
        for r in ransomNote:
            hash_ransom[ord(r)-ord('a')] += 1
        for r in magazine:
            hash_magazine[ord(r)-ord('a')] += 1
        result = [a_i - b_i for a_i, b_i in zip(hash_magazine, hash_ransom)]
        return sum(n < 0 for n in result) <= 0