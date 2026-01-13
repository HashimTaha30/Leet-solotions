class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        Len = len(words[-1])
        return Len
        