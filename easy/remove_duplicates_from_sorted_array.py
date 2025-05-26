'''
🟢 Problem: Remove Duplicates from Sorted Array
🔗 Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array
📘 Category: Array 
💡 Approach:
- Use a pointer to track unique positions
- Skip the first element using a flag
- Overwrite duplicates in-place
⏱️ Complexity: Time O(n), Space O(1)
🧪 Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
'''

def removeDuplicates(nums):

    i = 0 if nums[0]!=nums[-1] else 1
        
    started = False
    
    if i==0 :
        for element in nums:
        
            if started:
                if nums[i-1] != element:
                    nums[i] = element
                    i += 1
            else:
                started = True
                i+=1


    return i

    


removeDuplicates([0,0,1,1,1,2,2,3,3,4])