# P2, Using A Ton of Code From DocStringed P1

# Matrix with each string to search
with open('/Users/emreersahin/Desktop/Advent of Code 2024/Day4/Day4Advent.txt', 'r') as file:
    matrix = [line.strip() for line in file]

# Helper Function to find Pattern
def how_many_X(row, col):
    # Check All Four Possibilities
    operations = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    # Make sure operations are valid
    for operation in operations:
        x, y = operation
        updated_row, updated_col = x + row, y + col
        if not (0 <= updated_row < len(matrix)) or not (0 <= updated_col < len(matrix[0])):
            return 0

    if matrix[row+1][col+1] == "M":
        # TR M, BR M
        if matrix[row+1][col-1] == "M" and matrix[row-1][col-1] == "S" and matrix[row-1][col+1] == "S":
            return 1
        # TL M, TR M
        if matrix[row+1][col-1] == "S" and matrix[row-1][col-1] == "S" and matrix[row-1][col+1] == "M":
            return 1
    elif matrix[row+1][col+1] == "S":
        # TL M, BL M
        if matrix[row+1][col-1] == "S" and matrix[row-1][col-1] == "M" and matrix[row-1][col+1] == "M":
            return 1
        # BL M, BR M
        if matrix[row+1][col-1] == "M" and matrix[row-1][col-1] == "M" and matrix[row-1][col+1] == "S":
            return 1
    return 0

# Return count
counter = 0

# Loop through every part of file
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == "A":
            counter += how_many_X(row, col)

print(counter)


'''

# Find all XMAS - Forward down back every which way

# Processing File into Matrix
with open('/Users/emreersahin/Desktop/Advent of Code 2024/Day4/Day4Advent.txt', 'r') as file:
    # Array to hold 2d matrix
    matrix = []
    for line in file:
        matrix.append([line.strip()])

# Helper Function to Check # of Xmas from one X
def how_many_XMAS(row, col):
    # Helper_Function_Counter
    help_count = 0

    # We have X at a certain index (row, col), Must check Left, Right, Up, Down, Diagonal All Ways
    operations = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    
    # Loop through every kind of operation
    for operation in operations:
        x, y = operation
        updated_row = row
        updated_col = col
        for i in range(3):
            updated_row += x
            updated_col += y
            if 0 <= updated_row < len(matrix) and 0 <= updated_col < len(matrix[0][0]):
                # Use operation to figure out if XMAS
                if i == 0:
                    if matrix[updated_row][0][updated_col] != "M":
                        break
                elif i == 1:
                    if matrix[updated_row][0][updated_col] != "A":
                        break
                elif i == 2:
                    if matrix[updated_row][0][updated_col] == "S":
                        help_count += 1
            # Indice Invalid
            else:
                break

    # Return final count
    return help_count

# Now we have a matrix of lines so can do DFS with every X

# Counter for number of XMAS counted
counter = 0

# Looping through every entry
for row in range(len(matrix)):
    for col in range(len(matrix[row][0])):
        if matrix[row][0][col] == "X":
            XMAS_count = how_many_XMAS(row, col)
            counter += XMAS_count

# ANSWER
print(counter)

'''

