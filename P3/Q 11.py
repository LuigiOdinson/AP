# 11
def sumfile(filename):
    sum = 0
    for num in filename:
        sum += int(num)
    return sum


file = open("numbers.txt", 'r')
print(sumfile(file))
