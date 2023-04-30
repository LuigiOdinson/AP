# 22
def check(matrix):
    length = len(matrix)
    row_elements = []
    column_elements = []
    for i in range(length):
        row_elements.append(matrix[i])
        column_elements.append([matrix[k][i] for k in range(length)])

    for sub in row_elements:
        if sub in column_elements:
            return True
    return False


lst = [[1, 2, 8],
       [2, 0, 5],
       [2, 5, 5]]

print(check(lst))
