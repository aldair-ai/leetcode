'''
🟢 Problem: 
🔗 Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
📘 Category: Array 
💡 Approach:
- Track the minimum price seen so far
- At each step, calculate profit if sold today
- Update max profit when a better profit is found
⏱️ Complexity: Time O(n), Space O(1)
🧪 Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
'''

def maxProfit(prices):

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit