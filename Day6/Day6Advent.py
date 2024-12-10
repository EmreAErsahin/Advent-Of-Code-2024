# P1 Day6

# Setting Direction Helper Function
def set_direction(dir_number):
    # Set Direction
    if dir_number % 4 == 0:
        return "up"
    elif dir_number % 4 == 1:
        return "right"
    elif dir_number % 4 == 2:
        return "down"
    else:
        return "left"

# Part 1, Seeing How Many Places the Guard Visits
def p1(matrix, start_row, start_col):
    visited = set()
    visited.add((start_row, start_col))
    cur_row, cur_col = start_row, start_col
    dir_counter = 0
    while 0 <= cur_row < len(matrix) and 0 <= cur_col < len(matrix[0]):
        if matrix[cur_row][cur_col] == "#":
            cur_row -= dx
            cur_col -= dy
            dir_counter += 1
            continue
        # Setting Direction
        direction = set_direction(dir_counter)
        # Up
        if direction == "up":
            dx, dy = -1, 0
        # Down
        elif direction == "down":
            dx, dy = 1, 0
        # Right
        elif direction == "right":
            dx, dy = 0, 1
        # Left
        elif direction == "left":
            dx, dy = 0, -1
        if matrix[cur_row][cur_col] == "." and (cur_row, cur_col) not in visited:
                visited.add((cur_row, cur_col))
        cur_row, cur_col = cur_row + dx, cur_col + dy
    return len(visited)

def main():
    # Gettig matrix of text input
    with open('/Users/emreersahin/Desktop/Advent-of-Code-2024/Day6/Day6Advent.txt', 'r') as file:
        matrix = [list(line.strip()) for line in file]

    # Looping through till guard is found
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "^":
                print(p1(matrix, row, col))

if __name__ == "__main__":
    main()