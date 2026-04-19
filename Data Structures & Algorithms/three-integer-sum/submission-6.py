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
                
                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    r = r - 1
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

        return result



        
        