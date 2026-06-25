class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #bruteforce solution
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return[]
        # ✅ Correct implementation for all test cases
        # 🕒 Time Complexity: O(n²) - nested loops check all possible pairs
        # 🚀 Optimal solution exists with O(n) time using a hash map:
        # Create a dictionary to store numbers and their indices
        # For each number, check if (target - current number) exists in the dictionary
        # If yes, return current index and stored index
        # If not, add current number to dictionary and continue

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna