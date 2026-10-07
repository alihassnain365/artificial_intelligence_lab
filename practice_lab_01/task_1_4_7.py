# Read the size of the square matrices
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

# Add the two matrices
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(row)

# Display the result
print("Result:")
for row in matrix3:
    print(row)