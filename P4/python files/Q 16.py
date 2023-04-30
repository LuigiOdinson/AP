# 16
def count_evens(a):
    counter = 0
    for i in a:
        if i % 2 == 0:
            counter += 1
    return counter


lst = [3, 5, 4, -1, 0]
print(count_evens(lst))
