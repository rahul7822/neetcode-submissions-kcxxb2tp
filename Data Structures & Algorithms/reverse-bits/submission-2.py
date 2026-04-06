class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0

        res = 0

        counter = 0
        while n > 0:
            is_set_bit = True if n & 1 == 1 else False
            if is_set_bit:
                res = res | (1 << (31 - counter))

            counter += 1
            n >>= 1

        return res
