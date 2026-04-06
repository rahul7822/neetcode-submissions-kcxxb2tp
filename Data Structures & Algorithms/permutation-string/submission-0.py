class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_sorted = "".join(sorted(s1))

        l, r = 0, len_s1 - 1

        while r < len_s2:
            sub_str = "".join(sorted(s2[l : r + 1]))

            if s1_sorted == sub_str:
                return True

            l += 1
            r += 1

        return False

        