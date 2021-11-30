# Write a function that takes a list of characters and reverses the letters in place.
list1 = ['a', 'b', 'c', 'd']
#output c, b, a

def reverseChar(list_of_chars):

    left_index  = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = list_of_chars[right_index], list_of_chars[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1

print(reverseChar(list1))

