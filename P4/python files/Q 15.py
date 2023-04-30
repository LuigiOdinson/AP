# 15
def sum_positive(a):
    sum = 0
    for i in a:
        if i >= 0:
           sum += i
    return sum


lst = [3, -3, 5, 2, -1, 2]
print(sum_positive(lst))
