# 20
# making the matrix
m = []
for row in range(6):
    r = [] # inner list
    for column in range(9):
        r.append(1)
    m.append(r)

# printing the matrix
for row in range(6):
    for column in range(9):
        print(m[row][column], end=" ")
    print()

m[2][4] = 0

# printing again
print("_"*20)
for row in range(6):
    for column in range(9):
        print(m[row][column], end=" ")
    print()
