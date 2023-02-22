print("Enter five integer values")
n1 = int(input("Enter value 1: "))
n2 = int(input("Enter value 2: "))
n3 = int(input("Enter value 3: "))
n4 = int(input("Enter value 4: "))
n5 = int(input("Enter value 5: "))
max = n1
min = n1
if n2 >= max:
    max = n2
elif n2 <= min:
    min = n2

if n3 >= max:
    max = n3
elif n3 <= min:
    min = n3

if n4 >= max:
    max = n4
elif n4 <= min:
    min = n4

if n5 >= max:
    max = n5
elif n5 <= min:
    min = n5
print("Max:", max, sep='', end=' ')
print("Min:", min, sep='')