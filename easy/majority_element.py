"""
🟢 Problem: Majority Element
🔗 Link: https://leetcode.com/problems/majority-element
📘 Category: Array / Hash Map
💡 Approach:
    - Use a hash map (dictionary) to count the frequency of each element
    - Iterate through the array and update counts in the dictionary
    - Find the element with the highest count (majority element)
⏱️ Complexity: Time O(n), Space O(n)

🧪 Example:
Input:  nums = [3, 2, 3]
Output: 3
"""
def majorityElement(self, nums: list[int]) -> int:
    set_elements = set(nums)
        
    my_dict = {key: 0 for key in set_elements}

    for element in nums:
        my_dict[element] += 1

    max_key = max(my_dict, key=my_dict.get) 

    return max_key
