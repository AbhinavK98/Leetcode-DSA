class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #bruteforce solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return[]

        #Optimal hashmap

        n=len(nums)
        hashmap = {}
        for i in range(n):
            comp=target-nums[i]
            if comp in hashmap:
                return[hashmap[comp], i]
            hashmap[nums[i]]=i
        return []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna