def Part1(password):
    counter = 0
    for line in password:
        low = int(line[0].split('-')[0])
        high = int(line[0].split('-')[1])
        count = line[2].count(line[1].strip(':'))
        if low <= count <= high:
            counter = counter + 1
    
    print('{count} is the number of valid passwords in Part1'.format(count=counter))

def Part2(password):
    counter = 0
    for line in password:
        posa = int(line[0].split('-')[0]) - 1
        posb = int(line[0].split('-')[1]) - 1
        char = line[1].strip(':')
        posachar = line[2][posa]
        posbchar = line[2][posb]
        if((posachar == char) | (posbchar == char)) & ((posachar) != (posbchar)): # At least one has to match the character, but they can't both match.
            counter = counter + 1

    print('{count} is the number of valid passwords in Part2'.format(count=counter))


password = []

with open("day2-input.txt") as file:
  password = [line.strip().split(' ') for line in file]

Part1(password)
Part2(password)
