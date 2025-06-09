'''
🟢 Problem: 
🔗 Link: https://leetcode.com/problems/
📘 Category: Array / 
💡 Approach:
- 
- 
- 
⏱️ Complexity: Time O(n), Space O(n)
🧪 Example:
Input:
Output:
'''
import re

def isPalindrome(s):

    s = s.lower().replace(' ','')

    s = re.sub(r'[^a-z0-9]', '', s)
    
    str_len = len(s)

    j = -1

    index_loop = str_len//2
    result = True

    if str_len>1:
        for element in s[:index_loop]:
            if element == s[j]:
                j-=1
            
            else:
                result = False
                break
    print(s,j,index_loop,result)
    return result      

s = "A man, a plan, a canal: Panama"

isPalindrome(s)  # Example usage, should return True