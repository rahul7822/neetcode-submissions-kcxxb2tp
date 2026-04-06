class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chr_s = set()
        m_len = 0
        length = len(s)

        l, r = 0, 0
        while r < length:
            if s[r] not in chr_s:
                chr_s.add(s[r])
                r += 1
            else:
                while l < r and s[r] != s[l]:
                    chr_s.remove(s[l])
                    l += 1
                while l < r and s[r] == s[l]:
                    chr_s.remove(s[l])
                    l += 1
            
            m_len = max(m_len, len(chr_s))
            

        return m_len




