class Solution:
    def reverse(self, x: int) -> int:
        # max and min 32-bit integers
        # MAX_INT = 2147483647
        # MIN_INT = -2147483648

        MAX_INT = 214748364
        MIN_INT = -214748364

        res = 0

        while x != 0:
            digit = x % 10

            # python modulo fix for negative
            if x < 0 and digit > 0:
                digit -= 10

            # python division fix for negative (but works for positives as well)
            x = (x - digit) // 10

            # check overflow before updating the result
            if (res > MAX_INT) or (res == MAX_INT and digit > 7):
                return 0

            if (res < MIN_INT) or (res == MIN_INT and digit > 8):
                return 0

            res = res * 10 + digit

        return res