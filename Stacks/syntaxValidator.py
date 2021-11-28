input = "{[]()}" # return True 
input2 = "{[(])}" # return False 
input3 = "{[}" # return False  
input4 = "<>"

# I want to use stack
# append openers in stack
# compare two openers and closers 


def is_valid(string):
    stack = []
    for s in string:
        if s == '{' or s == '[' or s == '(' or s == '<':
            stack.append(s)
        if s == '}' or s == ']' or s == ')' or s == '>':
            opener_par = stack.pop()
            if opener_par == '{' and s == '}' or opener_par == '[' and s == ']' or opener_par == '(' and s == ')' or opener_par == '<' and s == '>':
                return True
            else:
                return False 

print(is_valid(input))
print(is_valid(input2))
print(is_valid(input3))
print(is_valid(input4))
