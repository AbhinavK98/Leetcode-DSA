class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #bruteforce -O(n*2)
        # n=len(numbers)
        # for i in range(n):
        #     for j in range(i+1, n):
        #        if numbers[i]+numbers[j]==target:
        #             return [i+1,j+1]
        # return []
        #Avg
        n=len(numbers)
        hash_map={}
        for i in range(n):
            rest=target-numbers[i]
            if rest in hash_map:
                return [hash_map[rest]+1, i+1]
            hash_map[numbers[i]]=i
        return[]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna