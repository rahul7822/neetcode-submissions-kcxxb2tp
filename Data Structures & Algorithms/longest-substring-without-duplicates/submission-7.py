class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chr_s = {}
        m_len = 0
        length = len(s)

        l, r = 0, 0
        while r < length:
            if s[r] not in chr_s:
                chr_s[s[r]] = r
                r += 1
            else:
                tmp_l = chr_s[s[r]]
                while l <= tmp_l:
                    del chr_s[s[l]]
                    l += 1
            
            m_len = max(m_len, len(chr_s))
            

        return m_len




