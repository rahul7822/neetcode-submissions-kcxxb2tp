class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_index = {}

        max_len = 0
        l, r = 0, 0
        c = 0
        while r < len(s):
            if len(dict_index) == 0:
                dict_index[s[r]] = r
                r += 1
            else:
                if s[r] in dict_index:
                    dict_index[s[r]] = r
                    r += 1
                elif c < k:
                    r += 1
                    c += 1
                else:
                    l += 1
                    r = l
                    dict_index = {}

            max_len = max(max_len, r - l)

        return max_len