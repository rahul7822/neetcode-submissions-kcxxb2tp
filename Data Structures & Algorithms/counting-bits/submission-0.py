class Solution:
    def set_bits_count(self, n):
        counter = 0
        while n > 0:
            if n & 1:
                counter += 1
            n >>= 1
        return counter

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(self.set_bits_count(i))

        return res