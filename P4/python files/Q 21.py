# 21
# 1st way
lst = []
for num in range(1, 11):
    lst.append(num)
print(lst)

# 2nd way
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)

# 3rd way
lst = [num for num in range(1, 11)]
print(lst)

# 4th way
nums = range(1, 11)
lst = list(nums)
print(lst)

# 5th way
first_half = [1, 2, 3, 4, 5]
second_half = [6, 7, 8, 9, 10]
lst = first_half + second_half
print(lst)
