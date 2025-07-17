'''
🟢 Problem: Can Place Flowers  
🔗 Link: https://leetcode.com/problems/can-place-flowers/  
📘 Category: Greedy / Array  
💡 Approach:
- Iterate through the flowerbed to check if a flower can be planted at position `i`.
- A flower can be planted at `i` if:
    - The spot is empty (0), and
    - Its neighbors (i-1 and i+1) are also empty or out of bounds.
- Modify the flowerbed in-place when planting and increment a counter.
- Return True if `counter >= n`, otherwise False.

⏱️ Complexity:  
- Time: O(n)  
- Space: O(1) (in-place update of flowerbed)

🧪 Example:  
Input: flowerbed = [1, 0, 0, 0, 1], n = 1  
Output: True  
'''

def canPlaceFlowers(flowerbed, n):
    counter = 0
    for i in range(len(flowerbed)):
        if i != 0 and i != len(flowerbed) - 1:
            if flowerbed[i] == flowerbed[i - 1] == flowerbed[i + 1] == 0:
                counter += 1
                flowerbed[i] = 1
        elif i == 0 and len(flowerbed) > 1:
            if flowerbed[i] == flowerbed[i + 1] == 0:
                counter += 1
                flowerbed[i] = 1
        elif i + 1 == len(flowerbed) and len(flowerbed) > 1:
            if flowerbed[i] == flowerbed[i - 1] == 0:
                counter += 1
                flowerbed[i] = 1
        elif len(flowerbed) == 1 and flowerbed[i] == 0:
            counter += 1

    return counter >= n

# Test example
flowerbed = [1, 0, 0, 0, 1]
n = 1
print(canPlaceFlowers(flowerbed, n))  # Output: True
