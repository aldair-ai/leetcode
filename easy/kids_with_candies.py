'''
🟢 Problem: Kids With the Greatest Number of Candies  
🔗 Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/  
📘 Category: Array / Greedy  
💡 Approach:
- Find the current maximum number of candies among all kids.
- Iterate through the list and for each child, check if giving `extraCandies` would allow them to reach or exceed that max.
- Store the result (`True` or `False`) in a new list for each child.

⏱️ Complexity:  
- Time: O(n)  
- Space: O(n) for the result list (O(1) auxiliary space)

🧪 Example:  
Input: candies = [2, 3, 5, 1, 3], extraCandies = 3  
Output: [True, True, True, False, True]  
'''

def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    result = []
    for candy in candies:
        result.append(candy + extraCandies >= max_candies)
    return result

# Test example
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))  # Output: [True, True, True, False, True]
