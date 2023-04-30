# 18
def next_number(a):
    if len(a) == 0:
        return 1
    else:
        spi = 1  # smallest positive integer
        for i in range(len(a)):
            if a[i] == spi:
                spi += 1
        return spi


lst = [5, 3, 1, 0, 3, -2]
# making sure the conditions are met
fun_lst = list({x for x in lst if x >= 1})  # we made it a set so they're all unique
print(next_number(fun_lst))
