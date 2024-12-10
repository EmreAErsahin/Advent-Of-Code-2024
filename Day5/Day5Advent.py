from collections import defaultdict, deque

def split_string(s: str, delimiter: str) -> list:
    return s.split(delimiter)

def p1(update: list, rules: list) -> int:
    # Map each element to its position in the update list
    positions = {value: idx for idx, value in enumerate(update)}
    
    # Check each rule to ensure dependencies are met
    for a, b in rules:
        if a in positions and b in positions:
            if positions[a] > positions[b]:
                # Dependency violated: 'a' comes after 'b'
                return 0
    
    # If all dependencies are satisfied, return the middle value
    if not update:
        return 0  # Handle empty list case
    return update[len(update) // 2]

def p2(update: list, rules: list) -> int:
    # First, check if the current update satisfies all dependencies
    mid_p1 = p1(update, rules)
    if mid_p1 > 0:
        # Dependencies are already satisfied; no correction needed
        return 0
    
    # Build the dependency graph: key -> set of dependents
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    elements = set(update)
    
    for a, b in rules:
        if a in elements and b in elements:
            graph[b].add(a)  # 'b' must come before 'a'
            in_degree[a] += 1  # 'a' has one more prerequisite
    
    # Initialize queue with nodes having in-degree 0 (no prerequisites)
    queue = deque([elem for elem in update if in_degree[elem] == 0])
    
    sorted_order = []
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        
        for dependent in graph[current]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    # Check if topological sort was successful
    if len(sorted_order) != len(elements):
        # Cycle detected or unresolved dependencies
        return 0
    
    # Find and return the middle value of the sorted list
    middle_index = len(sorted_order) // 2
    return sorted_order[middle_index]

def solution(rules: list, updates: list):
    total_p2 = 0
    for idx, update in enumerate(updates, 1):
        middle_p1 = p1(update, rules)
        
        middle_p2 = p2(update, rules)
        
        # Aggregate the result for p2
        total_p2 += middle_p2
    print(total_p2)
    return total_p2

def read_input(file_path: str) -> tuple:
    rules = []
    updates = []
    with open(file_path, 'r') as file:
        # Read rules until an empty line is encountered
        for line in file:
            line = line.strip()
            if not line:
                break  # Empty line signifies end of rules
            parts = split_string(line, '|')
            if len(parts) == 2:
                a, b = int(parts[0]), int(parts[1])
                rules.append((a, b))
        
        # Read updates after the empty line
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            parts = split_string(line, ',')
            update = [int(part) for part in parts]
            updates.append(update)
    
    return rules, updates

def main():
    # Update the file path to your actual input file location
    input_file = '/Users/emreersahin/Desktop/Advent-of-Code-2024/Day5/Day5Advent.txt'
    rules, updates = read_input(input_file)
    
    # Process updates and compute the result using both p1 and p2
    solution(rules, updates)
    
    return 0

if __name__ == "__main__":
    main()
