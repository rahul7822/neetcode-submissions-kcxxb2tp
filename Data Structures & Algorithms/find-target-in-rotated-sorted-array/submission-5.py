class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[l] < nums[m] and target > nums[l] and target < nums[m]:
                r = m - 1
            elif nums[m] < nums[r] and target > nums[m] and target < nums[r]:
                l = m + 1
            elif nums[l] > nums[m] and target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return -1

        