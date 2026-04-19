class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        has_0 = False
        max_n = float("-inf")
        s = 0

        for num in nums:
            if num == 0:
                has_0 = True
            if max_n < num:
                max_n = num
            s += num

        if has_0 == False:
            return 0

        return (((max_n) * (max_n + 1)) // 2) - s