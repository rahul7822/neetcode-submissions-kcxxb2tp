class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        counter = 0

        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK

        carry = 0
        while counter < 32:
            is_a_set_bit = True if a & 1 == 1 else False
            is_b_set_bit = True if b & 1 == 1 else False

            if is_a_set_bit and is_b_set_bit:
                if carry == 0:
                    res_bit = 0
                else:
                    res_bit = 1
                carry = 1
            elif is_a_set_bit or is_b_set_bit:
                if carry == 0:
                    res_bit = 1
                    carry = 0
                else:
                    res_bit = 0
                    carry = 1
            else:
                res_bit = carry
                carry = 0

            res |= (res_bit << counter)
            counter += 1

            a >>= 1
            b >>= 1

        if res > MAX_INT:
            res = res - (1 << 32)
        
        return res


