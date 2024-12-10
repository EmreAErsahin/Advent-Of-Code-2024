from collections import defaultdict


# Part 1 Code
def p1():
    res = 0

    with open('/Users/emreersahin/Desktop/Advent of Code 2024/Day5/Day5Advent.txt', 'r') as file:
        updates = False
        rule_dict = defaultdict(set)
        update_arr = []
        for line in file:
            if line.strip() == "":
                updates = True
            # Adding to rule dict
            if not updates:
                rule_dict[line[3:].strip()].add(line[:2])
            # Adding to update matrix
            if updates:
                update_arr.append(line.strip().split(','))
    
    # RULE DICT: Every number mapped to a set of every number that should proceed it
    # UPDATE ARRAY: Every update represented as an array of string numbers

    # Iterate through every update, if everything valid then add middle number to res, otherwise continue
    for update in update_arr:
        for i in range(len(update), -1, -1):
            



    return res

def main():
    print(p1())
    # print(p2())


if __name__ == "__main__":
    main()

