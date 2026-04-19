class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 1:
            return length

        ch_dict = {}

        max_len = 0
        l, r = 0, 0

        while r < length:
            if s[r] not in ch_dict:
                ch_dict[s[r]] = r
            else:
                l = ch_dict[s[r]]
                ch_dict[s[r]] = r

            max_len = max(max_len, r - l)
            r += 1

        return max_len


