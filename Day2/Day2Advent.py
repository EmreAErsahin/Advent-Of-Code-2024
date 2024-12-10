# Part 1
# Go through every strip, must be either all increasing or all decreasing
# Every increase/decrease must go by at least 1 and at most 3

# Part 2
# Now, a strip is determined safe if one number can be removed and be safe

# Helper function to find if something is a valid sequence
def validSequence(array):
    up = array[-1] > array[0]
    for i in range(len(array) - 1):
        diff = array[i+1] - array[i]
        if not (1 <= abs(diff) <= 3):  # Differences must be between 1 and 3
            return False
        if up and diff < 0:  # Should be increasing
            return False
        if not up and diff > 0:  # Should be decreasing
            return False
    return True

# Extended function to handle Problem Dampener
def isSafeWithProblemDampener(line):

    # Convert to list bc map function returns map iterable object
    array = list(map(int, line.split()))
    
    # Check if the original sequence is valid
    if validSequence(array):
        return True
    
    # Check if removing one number makes it valid
    for i in range(len(array)):
        modified_array = array[:i] + array[i+1:]  # Remove the i-th element
        if validSequence(modified_array):
            return True
    
    return False

file_path = "/Users/emreersahin/Desktop/Advent of Code 2024/Day2/AdventDay2.txt"

# Counter variable to hold the final answer
counter = 0

with open(file_path, 'r') as file:
    for line in file:
        if isSafeWithProblemDampener(line):
            counter += 1

print(counter)


# OPTIMIZED SOLUTION WITH GPT

# Can scan through linearly and if a problem number comes up then see if removing the current number or that number works
# If not, then return that it is not safe. Keep track of how many times this happens as if it happens more than once and gets solved
# then the strip isn't safe because more than one need to be removed