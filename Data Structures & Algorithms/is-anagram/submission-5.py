class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [] 
        for i in range(len(s)):
            chars.append(s[i])
        for i in range(len(t)):
            if t[i] not in chars:
                return False
            chars.remove(t[i])
        if len(chars) != 0:
            return False
        return True
    