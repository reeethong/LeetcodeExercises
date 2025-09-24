class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1: #base cases
            return len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i) #not efficient as result does not require the list to only have the unique numbers
                continue
            i += 1
        return len(nums)
