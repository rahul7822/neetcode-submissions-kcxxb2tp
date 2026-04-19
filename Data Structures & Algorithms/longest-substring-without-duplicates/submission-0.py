class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_dict = {}

        max_len = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] not in ch_dict:
                ch_dict[s[r]] = r
            else:
                l = ch_dict[s[r]]
                max_len = max(max_len, r - l)
                ch_dict[s[r]] = r
                
            r += 1

        return max_len


