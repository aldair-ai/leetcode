'''
🟢 Problem: 
🔗 Link: https://leetcode.com/problems/is-subsequence/
📘 Category: String
💡 Approach:
- Two-pointer technique: Iterate through t while tracking position i in s, advancing i only when characters match.
-Early stopping: Stops scanning once all characters of s are found in order.
-Subsequence check: Returns True if all characters in s are found sequentially in t.
⏱️ Complexity: Time O(n), Space O(1)
🧪 Example:
Input: s = "abc", t = "ahbgdc"
Output: true
'''

def isSubsequence(s, t):

    i = 0

    string_len = len(s)

    for element in t:
        if i<=(string_len-1) :
            if element == s[i]:
                i += 1
    if i == len(s):
        return True
    else:
        return False
        
s = "b"
t = "abc"

isSubsequence(s, t)
