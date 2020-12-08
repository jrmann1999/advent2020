import re

BIGTREE = []
SOLUTION = {}
TOTAL = 0

# Recursive algorithm using a stack to push/pull searching values
def findEntry(tree, value):
    for entry, contents in tree.items():
        for val in contents:
            y = re.match('.*(' + value + ').*', val)
            if y:
                if SOLUTION:
                    if entry not in SOLUTION.keys():
                        BIGTREE.append(entry)
                        SOLUTION[entry] = 'FOUND'
                else:
                    BIGTREE.append(entry)
                    SOLUTION[entry] = 'FOUND'
    if BIGTREE:
        findEntry(tree, BIGTREE.pop())
    else:
        return        

def findBags(tree, value):
    total = 0
    contents = tree[value]

    if contents:
        for val in contents:
            if val == 'no other':
                return total
            else:
                num, color1, color2 = val.split(' ')
                yint = int(num)
                total += yint
                total += yint * (findBags(tree, color1 + ' ' + color2))
    
    return total
   
with open("day7-input.txt") as file:
  lines = file.readlines()

tree = {}

# Build Tree of Rules
for line in lines:
    condition = line.split()[:2]
    conditions = ' '.join(condition)
    leftover = line.split()[4:]
    rules = ' '.join(leftover).strip().split(',')

    tree[conditions] = []
    for rule in rules:
        tree[conditions].append(rule.strip('.').strip('bag').strip('bags').strip())

# PART1
# Push our key onto the stack, and then start searching with recursion
BIGTREE.append('shiny gold')
findEntry(tree, BIGTREE.pop())
# SOLUTION should have the matrix of combinations, and the number of entries.
print(SOLUTION)
print(len(SOLUTION.keys()))

# PART2
TOTAL += findBags(tree, 'shiny gold')
print(TOTAL)