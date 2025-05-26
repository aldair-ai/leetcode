"""
🟢 Problem: Move Zeroes
🔗 Link: https://leetcode.com/problems/move-zeroes
📘 Category: Array / Pointers
💡 Approach:
    - Create a temporary list to store all non-zero elements
    - Overwrite the original list with non-zero elements first
    - Fill the rest of the list with zeros
⏱️ Complexity: Time O(n), Space O(n)

🧪 Example:
Input:  nums = [0, 1, 0, 3, 12]
Output: nums = [1, 3, 12, 0, 0]
"""

from typing import List

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    final_list = []

    # Step 1: Collect all non-zero elements
    for element in nums:
        if element != 0:
            final_list.append(element)

    # Step 2: Overwrite original array
    for i in range(len(nums)):
        if i < len(final_list):
            nums[i] = final_list[i]
        else:
            nums[i] = 0
