class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq1 = {}
        freq2 = {}

        for l in range(len(s)):
            freq1[s[l]] = 1 + freq1.get(s[l], 0)
            freq2[t[l]] = 1 + freq2.get(t[l], 0)


        return freq1 == freq2