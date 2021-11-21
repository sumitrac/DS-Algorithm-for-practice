# Design and implement a method that takes two integer arrays 
# with the unique values
# and returns their intersection in a new array 

#input examples 
nums1 = [4, 2, 6, 3, 78, 20]
nums2 = [5, 2, 6, 45, 24]
#output = [2, 6]

# pseudocode 
# loop though arrays
# check if integer from array1 exist in array2
# append that common integer to new array

# Time: O(n)
# Space: O(n)

def returnIntersection(Array1, Array2):
    Array3 = []
    for i in Array1:
        if i in Array2 and i not in Array3:
            Array3.append(i)
    return Array3
print("Intersection of two Arrays: " + str(returnIntersection(nums1, nums2)))

# An unsorted array has all unique elements except one. 
# Design an algorithm/method to find the repeating element

# input examples 
inputArray = [1, 1, 1, 2, 2, 3, 3, 5]
#out = [1, 2, 3]

# pseudocode 
# iterate through the array
# loop for repeating integers 
# use Hash to store the integer as key and value as a count of integer 
# return integers that has count larger than 1

# Time O(n)
# Space O(n)

def repeatedIntegers(array):
    integersHash = {}
    returnArray = []

    for int in array:
        if int in integersHash:
            integersHash[int] += 1 
        else: 
            integersHash[int] = 1

    for key, value in integersHash.items():
        if value != 1:
            returnArray.append(key)
    return ("Repeated numbers: " + str(returnArray))

print(repeatedIntegers(inputArray))

# Design a method that takes an array of positive integers
# returns the index of the two integers that sum up to 10

inputNums = [2, 4, 1, 6]
sumNums = 10 
# output: 1, 2, index of 4 and 6 

# pseudocode 
# use range to iterate through the Array 
# Store nums in Hash
# check if sumNums - num in Hash 
    # return indices 

# Time: O(n)
# Space: O(n)

def indexOfSum(array, targetSum):
    hashOfNums = {}
    for int in range(len(array)):
        if targetSum - array[int] in hashOfNums:
            return [hashOfNums[targetSum - array[int]], int]
        else: 
            hashOfNums[array[int]] = int

print("Index of targeted integers: " + str(indexOfSum(inputNums, sumNums)))

# # Design a method that takes an array of positive integers
# # returns all pair of integers that sum up to K

# positiveInt = [1, 2, 4, 6, 3, 7]
# sumTarget = 10 
# # output = [[4, 6]. [3, 7]]

# # pseudocode 
# # create an empty hash
# # loop through Array to check if sumTarget - int exist in hash
# # if true append that pair to list 

# def pairSums(array, targetSum):
#     hashOfNums = {}
#     returnList = []
#     for int in array:
#         if targetSum - array[int] in hashOfNums:
#             returnList.append(hashOfNums[targetSum - array[int]])
#             return returnList

# print(pairSums(positiveInt, sumTarget))



