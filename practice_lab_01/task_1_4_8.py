# Read the size of the matrices
n = int(input("Enter the size of matrix: "))

# Create lists for the matrices
matrix1 = []
matrix2 = []
matrix3 = []

# Read first matrix
print("Enter elements of first matrix:")
for i in range(n):
    row = []
    for j in range(n):
        value = int(input(f"Element [{i}][{j}]: "))
        row.append(value)
    matrix1.append(row)

# Read second matrix
print("Enter elements of second matrix:")
for i in range(n):
    row = []
    for j in range(n):
        value = int(input(f"Element [{i}][{j}]: "))
        row.append(value)
    matrix2.append(row)

# Multiply the matrices
for i in range(n):
    row = []

    for j in range(n):
        total = 0

        for k in range(n):
            total = total + matrix1[i][k] * matrix2[k][j]

        row.append(total)

    matrix3.append(row)

# Display the result
print("Result:")
for row in matrix3:
    print(row)