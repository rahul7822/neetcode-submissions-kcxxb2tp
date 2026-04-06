class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)

        result = set()
        length = len(nums)

        for i in range(length): # O(n^2)
            l, r = 0, length - 1

            while l < r:
                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue

                cur_sum = nums[i] + nums[l] + nums[r]

                if cur_sum == 0:
                    result.add(",".join(map(lambda x : str(x), sorted([nums[i], nums[l], nums[r]]))))
                
                if cur_sum > 0:
                    r -= 1
                else:
                    l += 1

        result = list(map(lambda x : list(map(lambda y : int(y) , x.split(","))) , list(result)))


        return result



        
        