class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        d = {}
        result = 0

        while r < len(s):
            if s[r] in d:
                d[s[r]] += 1
            else:
                d[s[r]] = 1

            is_valid_substr = self.checkFrequency(d, l, r, k)

            if is_valid_substr:
                result = max(result, r - l + 1)
                r += 1
            else:
                d[s[l]] -= 1
                l += 1
        
        return result

    def checkFrequency(self, d, l , r, k):
        max_freq = 0
        total_freq = r - l + 1
        for key, value in d.items():
            if value > max_freq:
                max_freq = value

        if total_freq - max_freq <= k:
            return True
        
        return False
            

            
        