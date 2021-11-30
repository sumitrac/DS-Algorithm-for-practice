input = [3, 6, 3, 2]
# put [2, 0, 1]

def chooseFleets(wheels):
    # Write your code here
    # check the edges case with raising exception with invalid input if there no wheels
    if wheels is None or len(wheels) == 0:
        raise Exception('Invalid input')
    # using list to store the data 
    result = list()
    # Iterate through the list of wheels 
    for n in wheels:
        # check if the nums in wheels is mode of 2 
        # than return append 0 to our empty list 
        # else append (num / 4 + 1) to the list the list
        # return the list 
        result.append(0 if n % 2 != 0 else int(n / 4 + 1))
    return result
    
print(chooseFleets(input))