from copy import deepcopy

def Part1(matrix):
    newmatrix = deepcopy(matrix)
    counter = 0
    while True:
        counter += 1
        for i, line in enumerate(matrix):
            for j, entry in enumerate(matrix[i]):
                if i == 0:
                    if j == 0:
                        testlist = [matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
                        if entry == "L":
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                    elif j < len(matrix[i]) - 1:
                        testlist = [matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1], matrix[i][j+1]]
                        if entry == "L":
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        elif entry == '#':
                            if testlist.count('#') >= 4:
                                newmatrix[i][j] = "L"
                    else:
                        testlist = [matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j]]
                        if entry == "L":
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                elif i < len(matrix) - 1:
                    if j == 0:
                        testlist = [matrix[i-1][j], matrix[i-1][j+1], matrix[i][j+1], matrix[i+1][j+1], matrix[i+1][j]]
                        if entry == "L":
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        elif entry == '#':
                            if testlist.count('#') >= 4:
                                newmatrix[i][j] = "L"
                    elif j < len(matrix[i]) - 1:
                        testlist = [matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1], matrix[i][j+1], matrix[i-1][j+1], matrix[i-1][j], matrix[i-1][j-1]]
                        if entry == "L":
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        elif entry == '#':
                            if testlist.count('#') >= 4:
                                newmatrix[i][j] = "L"
                    else:
                        testlist = [matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j], matrix[i-1][j], matrix[i-1][j-1]]
                        if entry == "L":
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        elif entry == '#':
                            if testlist.count('#') >= 4:
                                newmatrix[i][j] = "L"
                else:
                    if j == 0:
                        testlist = [matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]]
                        if entry == "L":
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                    elif j < len(matrix[i]) - 1:
                        testlist = [matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1], matrix[i][j+1]]
                        if entry == "L":
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                        elif entry == '#':
                            if testlist.count('#') >= 4:
                                newmatrix[i][j] = "L"
                    else:
                        testlist = [matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j]]
                        if entry == "L":
                            if '#' not in testlist:
                                newmatrix[i][j] = '#'
                    

        print(counter)

        if newmatrix == matrix:
            seatcount = 0
            for entry in matrix:
                seatcount += entry.count('#')
            print(seatcount)
            break
        matrix = deepcopy(newmatrix)

with open(r"Day11\day11-input.txt") as file:
    lines = [x.strip() for x in file.readlines()]

matrix = []
for i, line in enumerate(lines):
    matrix.append(list(line))

Part1(matrix)


