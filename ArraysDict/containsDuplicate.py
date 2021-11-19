
# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# create an empty dictionary to store key,value  
# look through the list 
# key=element, value=count of element

# check dictionary if there is any element with > 1 value
# return true 
# else false 
def containsDuplicate(nums):
    if nums is None:
        return None 

    nums_dict = {} 
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1

    for num in nums_dict:
        if nums_dict[num] > 1:
            return True 
    return False 

# Time: O(n)
# Space: O(n)

#TEST CASES
nums = [2,14,18,22,22]
# Output: true
nums1 = [1,2,3,1]
# Output: true
nums2 = [1,2,3,4]
# Output: false
nums3 = [1,1,1,3,3,4,3,2,4,2]
# Output: true

print(containsDuplicate(nums))
print(containsDuplicate(nums1))
print(containsDuplicate(nums2))
print(containsDuplicate(nums3))

def test_containsDuplicate():
    assert containsDuplicate(nums) == True 
def test_containsNoDuplicate():
    assert containsDuplicate(nums) == False