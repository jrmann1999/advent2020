def processCommand(lines, curPos):
    if commandList:
        if curPos in commandList:
            return 0
        else:
            commandList.append(curPos)
    else:
        commandList.append(curPos)

    
    if curPos > len(lines):
        return 0

    command, value = lines[curPos].strip().split(' ')
    if command == 'nop':
        curPos += 1
        return processCommand(lines, curPos)
    elif command == 'acc':
        curPos += 1
        return int(value) + processCommand(lines, curPos)
    elif command == 'jmp':
        curPos += int(value)
        return processCommand(lines, curPos)
    else:
        return 0

def fixCommand(lines, curPos):
    print(commandList)
    print(curPos)
    if commandList:
        if curPos in commandList:
            return 0
        else:
            commandList.append(curPos)
    else:
        commandList.append(curPos)

    
    if curPos > len(lines):
        return 0

    command, value = lines[curPos].strip().split(' ')
    if command == 'nop':
        curPos += 1
        return fixCommand(lines, curPos)
    elif command == 'acc':
        curPos += 1
        return int(value) + fixCommand(lines, curPos)
    elif command == 'jmp':
        curPos += int(value)
        return fixCommand(lines, curPos)
    else:
        return 0
    



with open("day8-input.txt") as file:
  lines = file.readlines()

# Part1
curpos = 0
count = 0
commandList = []
count += processCommand(lines, curpos)
print(count)

# Part2
curpos = 0
count = 0
commandList = []
count += fixCommand(lines, curpos)
print(count)

