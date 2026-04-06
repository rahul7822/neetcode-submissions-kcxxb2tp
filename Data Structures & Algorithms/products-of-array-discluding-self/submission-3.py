class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [ 1 for _ in range(len(nums))]

        prod = 1
        for num in nums:
            prod *= num
            prefix.append(prod)

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            suffix[i] = prod

        result = [ 0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                result[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                result[i] = prefix[i - 1]
            else:
                result[i] = prefix[i - 1] * suffix[i + 1]

        return result

        