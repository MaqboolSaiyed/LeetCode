from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Create a dictionary to store seen numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num  # Find the complement needed

            if complement in seen:
                return [seen[complement], i]  # Return indices if complement found

            seen[num] = i 

        raise ValueError("No two sum solution")  