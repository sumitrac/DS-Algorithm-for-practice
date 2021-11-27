# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# example inputs
input1 = "tree"
# output: eetr or eert 
input2 = "cccaaa"
# output: cccaaaa or aaaccc
input3 = "Aabb "
# output: bbAa or bbaA / 

# To clarify 
# Alphabetical order doesn't matter
# lower != upper case 

# Pseudocode 
# iterate through each char in string
# count the char of string
# Use Hash Key(char): Value(count of char)

# based on the count of char, return key from max to min 

# Time: O(n)
# Space: O(n)

def returnFreChar(string):
    count_char = {} #{'t': 1, 'r': 1, 'e': 2}
    for char in string:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    # print(count_char)
    # Get a dictionary of with the keys being
    # letter counts and the values being strings
    # storing all the letters with that count 
    # that many times
    # Example:  { 3: 'ttteee' } for "etette"
    max_count = 0
    letter_strings = {}
    for letter, count in count_char.items():
        if letter_strings.get(count):
            letter_strings[count] += letter * count
        else:
            letter_strings[count] = letter * count
        
        if max_count < count:
            max_count = count
    

    # Combine the letter strings in descending order
    result = ""
    while max_count > 0:
        if letter_strings.get(max_count):
            result += letter_strings[max_count]
        max_count -= 1

    return result

print(returnFreChar(input1))
print(returnFreChar(input2))
print(returnFreChar(input3))


