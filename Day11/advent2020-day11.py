from copy import deepcopy

def Part1(matrix):
    newmatrix = deepcopy(matrix)
    counter = 0
    while True:
        counter += 1
        for i, line in enumerate(matrix):
            for j, entry in enumerate(matrix[i]):
                if entry == "L":
                    if i == 0:
                        if j == 0:
                            testlist = [matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        elif j < len(matrix[i]) - 1:
                            testlist = [matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1], matrix[i][j+1]]
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        else:
                            testlist = [matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j]]
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                    elif i < len(matrix) - 1:
                        if j == 0:
                            testlist = [matrix[i-1][j], matrix[i-1][j+1], matrix[i][j+1], matrix[i+1][j+1], matrix[i+1][j]]
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        elif j < len(matrix[i]) - 1:
                            testlist = [matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1], matrix[i][j+1], matrix[i+1][j+1], matrix[i+1][j], matrix[i+1][j-1], matrix[i][j-1]]
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        else:
                            testlist = [matrix[i-1][j-1], matrix[i-1][j], matrix[i+1][j], matrix[i+1][j-1], matrix[i][j-1]]
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                    else:
                        if j == 0:
                            testlist = [matrix[i-1][j], matrix[i-1][j+1], matrix[i][j+1]]
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        elif j < len(matrix[i]) - 1:
                            testlist = [matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1], matrix[i][j+1], matrix[i][j-1]]
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        else:
                            testlist = [matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]]
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
        print(counter, newmatrix)
        break

with open(r"Day11\day11-input-small.txt") as file:
    lines = [x.strip() for x in file.readlines()]

matrix = []
for i, line in enumerate(lines):
    matrix.append(list(line))

#for i, entry in enumerate(matrix):
#    for j, char in enumerate(entry):
#        print('({i},{j}),{char}'.format(i = i, j = j, char = char), end = ' ')
#    print('')

Part1(matrix)
#print(matrix)

