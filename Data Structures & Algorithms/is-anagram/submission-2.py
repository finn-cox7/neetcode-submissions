class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssort = sorted(s)
        tsort = sorted(t)
        if tsort == ssort:
            return True
        return False