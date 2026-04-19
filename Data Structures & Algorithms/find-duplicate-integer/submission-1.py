class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        n = len(nums) - 1

        while (nums[slow] != nums[fast]):
            slow += 1
            fast += 2

            if slow > n:
                slow = 0
            if fast > n:
                fast = 1


        return nums[slow]