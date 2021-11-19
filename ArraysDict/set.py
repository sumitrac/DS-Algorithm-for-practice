# convert list to a set
nums = [1, 2, 4, 5, 1, 3, 5, 7]
print("list: " + str(nums))
new_set = set(nums)
print("Set: " + str(new_set))

# print list index
n = 5
def say_hi_n_times(n):
    for time in range(n):
        print(str(time) + " hi")
print(say_hi_n_times(n))


# def print_all_items(items):
#     for item in items:
#         print(item)