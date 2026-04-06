class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_seq_c_max = 0

        for num in nums:
            if num - 1 not in nums:
                seq_c = 1
                while (num + seq_c) in nums:
                    seq_c += 1
                
                if longest_seq_c_max < seq_c:
                    longest_seq_c_max = seq_c

                # if len(nums) - longest_seq_c_max <= 0:
                #     break

        return longest_seq_c_max

        