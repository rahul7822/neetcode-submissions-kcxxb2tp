class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2:
            return False

        freq_s1 = {}
        freq_sub_s2 = {}
        for i in range(len_s1):
            freq_s1[s1[i]] = 1 + freq_s1.get(s1[i], 0)
            freq_sub_s2[s2[i]] = 1 + freq_sub_s2.get(s2[i], 0)

        if freq_s1 == freq_sub_s2:
            return True

        for r in range(len_s1, len_s2):
            left_ch = s2[r - len_s1]
            right_ch = s2[r]

            cnt = freq_sub_s2[left_ch] - 1
            if cnt == 0:
                del freq_sub_s2[left_ch]
            else:
                freq_sub_s2[left_ch] = cnt

            freq_sub_s2[right_ch] = 1 + freq_sub_s2.get(right_ch, 0)

            if freq_s1 == freq_sub_s2:
                return True

        return False