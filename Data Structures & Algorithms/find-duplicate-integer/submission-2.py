class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        n = len(nums) - 1

        while slow <= n:
            if (nums[slow] == nums[fast]) and (slow != fast):
                return nums[slow]
            
            if slow + 1 <= n and nums[slow] == nums[slow + 1]:
                return nums[slow]

            if fast + 1 <= n and nums[fast] == nums[fast + 1]:
                return nums[fast]

            slow += 1
            fast += 2

            if fast >= n:
                fast = 0


        return -1