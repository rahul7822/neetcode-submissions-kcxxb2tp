class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        length = len(nums)

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, length - 1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if cur_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                
                if cur_sum > 0:
                    r -= 1
                else:
                    l += 1

        return result



        
        