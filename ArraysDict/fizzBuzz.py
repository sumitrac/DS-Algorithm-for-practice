# number = 5 # 1, 2, 3, 4, 5
# out: 1, 2, Fizz, 4, Buzz
number = 15


def fizzBuzz(num):
    returnList = []

    for n in range(1, num+1): #1, 2, 3, 4, 5
    # Write your code here
        if n % 3 == 0 and n % 5 == 0:
            returnList.append("FizzBuzz")
        elif n % 3 == 0:
            returnList.append("Fizz") 
        elif n % 5 == 0: 
            returnList.append("Buzz")
        else:
            returnList.append(n)
    return returnList

print(fizzBuzz(number))
