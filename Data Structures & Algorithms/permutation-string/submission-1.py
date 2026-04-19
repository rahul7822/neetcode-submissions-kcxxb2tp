class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        freq_s1 = {}
        for ch in s1:
            freq_s1[ch] = 1 + freq_s1.get(ch, 0)

        l, r = 0, len_s1 - 1
        freq_sub_s2 = {}

        for ch in s2[l : r + 1]:
            freq_sub_s2[ch] = 1 + freq_sub_s2.get(ch, 0)

        while r < len_s2 - 1:
            if freq_s1 == freq_sub_s2:
                return True

            ch_freq = freq_sub_s2[s2[l]]
            if ch_freq == 1:
                del freq_sub_s2[s2[l]]
            else:
                freq_sub_s2[s2[l]] = freq_sub_s2[s2[l]] - 1

            l += 1
            r += 1

            freq_sub_s2[s2[r]] = 1 + freq_sub_s2.get(s2[r], 0)


        return False