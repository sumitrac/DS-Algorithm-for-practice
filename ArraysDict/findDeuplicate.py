# Write a function which finds an integer that appears more than once in our list. 
# Don't modify the input! (If there are multiple duplicates, you only need to find one of them.) 
input = [1, 1, 2, 3, 4, 2, 1]
#output 1 
input2 = [2, 3, 4, 5, 5]
#output 5 

def find_repeat(numbers):
    numbers_seen = []
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.append(number)

# Time: O(n)
# Space: O(n)
print(find_repeat(input))
print(find_repeat(input2))

# Write a function that returns all duplicates. 
nums = [2, 2, 5, 1, 7, 7]
def find_allrepeat(numbers):
    num_count = {} #{2:2, 5:1, 1:1, 7:2}
    for num in numbers:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    return_allrepeat = []
    for num, count in num_count.items():
        if num_count[num] != 1:
            return_allrepeat.append(num)
    return return_allrepeat

# Time: O(n)
# Space: O(n)
print(find_allrepeat(nums))