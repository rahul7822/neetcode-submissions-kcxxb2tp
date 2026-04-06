class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}

        for ch in s:
            if ch in dict_s:
                dict_s[ch] = dict_s[ch] + 1
            else:
                dict_s[ch] = 1

        for ch in t:
            if ch not in dict_s:
                return False
            else:
                dict_s[ch] = dict_s[ch] - 1
        
        for ch in s:
            if dict_s[ch] != 0:
                return False

        return True