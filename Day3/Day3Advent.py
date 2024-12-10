# Scan through text and find all the places where mul(???, ???) is present.
# Question marks can be 1-3 digits

import re
from collections import deque

count = 0
q = deque()

with open('/Users/emreersahin/Desktop/Advent of Code 2024/Day3/Day3Advent.txt', 'r') as file:
    for line in file:
        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
        matches = re.findall(pattern, line)
        for match in matches:
            q.append(match)
print(matches)

# Set a bool that will make the decision of how to process it depending on what comes out of queue
process_flag = True
while q:
    cur_element = q.popleft()
    if cur_element == 'do()':
        process_flag = True
        continue
    elif cur_element == 'don\'t()':
        process_flag = False
        continue
    else:
        if process_flag:
            needed_part = cur_element[4:-1]
            numbers = needed_part.split(',')
            count += int(numbers[0]) * int(numbers[1])
print(count)