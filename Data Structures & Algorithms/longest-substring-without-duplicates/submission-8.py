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
                while True:
                    chr_s.remove(s[l])
                    l += 1
                    if s[l-1] == s[r]:
                        break

            
            m_len = max(m_len, len(chr_s))
            

        return m_len




