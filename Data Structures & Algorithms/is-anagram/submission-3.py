class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}

        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1

        for ch in t:
            if ch not in dict_s:
                return False
            else:
                dict_s[ch] = dict_s[ch] - 1
        
        for value in dict_s.values():
            if value != 0:
                return False

        return True