class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0

        mask = 2 ** 31

        while n & mask == 0:
            n <<= 1

        return n
