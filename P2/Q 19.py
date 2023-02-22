print("Enter five integer values")
n1 = int(input("Enter value 1: "))
n2 = int(input("Enter value 2: "))
n3 = int(input("Enter value 3: "))
n4 = int(input("Enter value 4: "))
n5 = int(input("Enter value 5: "))

if n1 == n2 or n1 == n3 or n1 == n4 or n1 == n5:
    print("DUPLICATES")
elif n2 == n1 or n2 == n3 or n2 == n4 or n2 == n5:
    print("DUPLICATES")
elif n3 == n1 or n3 == n2 or n3 == n4 or n3 == n5:
    print("DUPLICATES")
elif n4 == n1 or n4 == n2 or n4 == n3 or n4 == n5:
    print("DUPLICATES")
elif n5 == n1 or n5 == n2 or n5 == n3 or n5 == n4:
    print("DUPLICATES")
else:
    print("ALL UNIQUE")