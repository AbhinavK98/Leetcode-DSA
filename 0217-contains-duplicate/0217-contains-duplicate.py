class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Bruteforce TLE
        # for i in range(len(nums)):
        #     for j in range (i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
        sort_nums=sorted(nums)
        for i in range(len(nums)-1):
                if sort_nums[i]==sort_nums[i+1]:
                    return True
        return False
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna