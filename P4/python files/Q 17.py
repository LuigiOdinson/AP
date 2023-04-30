# 17
def print_big_enough(list, n):
    for i in list:
        if i >= n:
            print(i)


lst = [3, 5, 4, -1, 0, 2]
num = 2
print_big_enough(lst, num)
