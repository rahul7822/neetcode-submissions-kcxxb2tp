class Solution:
    def find_min_pivot(self, nums):
        l, r = 0, len(nums) - 1
        
        while l <= r:

            if nums[l] <= nums[r]:
                return l
            
            m = (l + r) // 2
            
            left = m - 1 if m - 1 >= l else l
            right = m + 1 if m + 1 <= r else r

            if nums[m] < nums[left] and nums[m] < nums[right]:
                return m

            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m  - 1

        return -1

    def binaray_search(self, nums, l, r, target):
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:

        min_pivot_index = self.find_min_pivot(nums)
        if min_pivot_index == -1:
            return -1

        l, r = 0, len(nums) - 1

        result_1 = self.binaray_search(nums, l, min_pivot_index, target)
        result_2 = self.binaray_search(nums, min_pivot_index, r, target)

        if result_1 == -1 and result_2 == -1:
            return -1
        
        if result_1 != -1:
            return result_1
        else:
            return result_2

        

        