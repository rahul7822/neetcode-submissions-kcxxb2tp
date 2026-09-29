class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []

        i, j, carry = len(a) - 1, len(b) - 1, 0

        while i >= 0 or j >= 0:
            digit_a = 0 if i < 0 else int(a[i])
            digit_b = 0 if j < 0 else int(b[j])

            sum = digit_a + digit_b + carry

            result.append(sum % 2)
            carry = sum // 2

            i -= 1
            j -= 1

        if carry == 1:
            result.append(carry)

        result.reverse()

        return "".join(map(lambda x: str(x), result))