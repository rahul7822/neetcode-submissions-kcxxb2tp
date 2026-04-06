class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]: # means already sorted
                return nums[l]
            
            m = (l + r) // 2
            
            right = m + 1 if m < r else l
            left = m - 1 if m > l else r

            if nums[m] < nums[right] and nums[m] < nums[left]:
                return nums[m]

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1