class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero_count += 1
        
        result = []
        if zero_count > 1:
            return [0 for _ in range(len(nums))]

        if zero_count == 1:
            for num in nums:
                if num == 0:
                    result.append(prod)
                else:
                    result.append(0)
        
            return result

        return list(map(lambda x : prod // x, nums))