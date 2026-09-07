class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSize = len(s)
        tSize = len(t)

        if sSize != tSize:
            return False
        s = sorted(s)
        t = sorted(t)
        if s != t:
            return False
        return True
        