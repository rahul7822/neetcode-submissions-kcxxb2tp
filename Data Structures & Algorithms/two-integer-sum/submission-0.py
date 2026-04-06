class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            rem = target - nums[i]

            j = i + 1
            while j < len_nums:
                if nums[j] == rem:
                    return [i, j]
                j += 1
        