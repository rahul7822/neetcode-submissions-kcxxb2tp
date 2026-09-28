class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)

        result = ""
        carry = "0"
        idx = 0
        while idx < len_a and idx < len_b:
            cur_a = a[len_a - 1 - idx]
            cur_b = b[len_b - 1 - idx]

            if carry == "0":
                if cur_a == "1" and cur_b == "1":
                    result += "0"
                    carry = "1"
                elif cur_a == "1" or cur_b == "1":
                    result += "1"
                    carry = "0"
                else:
                    result += "0"
                    carry = "0"
            else:
                if cur_a == "1" and cur_b == "1":
                    result += "1"
                    carry = "1"
                elif cur_a == "1" or cur_b == "1":
                    result += "0"
                    carry = "1"
                else:
                    result += "1"
                    carry = "0"
            
            idx += 1

        remaining_str = None if len_a == len_b else (a, len_a) if len_a > len_b else (b, len_b)

        if remaining_str == None:
            if carry == "1":
                result += "1"
        else:
            rem_str, str_len = remaining_str

            while idx < str_len:
                cur_ch = rem_str[str_len - 1 - idx]
                if carry == "1":
                    if cur_ch == "1":
                        result += "0"
                        carry = "1"
                    else:
                        result += "1"
                        carry = "0"
                else:
                    if cur_ch == "1":
                        result += "1"
                        carry = "0"
                    else:
                        result += "0"
                        carry = "0"

                idx += 1

            if carry == "1":
                result += "1"

        return result[::-1]


