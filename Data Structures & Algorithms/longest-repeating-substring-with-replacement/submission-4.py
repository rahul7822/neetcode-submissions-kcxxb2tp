class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        d = {}
        result = 0

        while r < len(s):
            d[s[r]] = 1 + d.get(s[r], 0)

            if self.isValidFreqReplacement(d, l, r, k):
                result = max(result, r - l + 1)
            else:
                d[s[l]] -= 1
                l += 1

            r += 1
        
        return result

    def isValidFreqReplacement(self, d, l , r, k):
        total_freq = r - l + 1
        max_freq = max(d.values(), default = 0)
        return total_freq - max_freq <= k

            

            
        