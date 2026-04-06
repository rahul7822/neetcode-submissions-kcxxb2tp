class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            cur_num = abs(num)

            if nums[cur_num - 1] < 0:
                return cur_num
            
            nums[cur_num - 1] *= -1
