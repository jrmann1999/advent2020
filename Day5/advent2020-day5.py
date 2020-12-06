def rowRecurse(oldrange, direction):
    if oldrange.start == oldrange.stop:
        return oldrange
    if direction[0] == 'F':
        return rowRecurse(range(oldrange.start, oldrange.stop - int(((oldrange.stop - oldrange.start) + 1) / 2)), direction[1:])
    elif direction[0] == 'B':
        return rowRecurse(range(oldrange.start + (int(((oldrange.stop - oldrange.start) + 1) / 2)), oldrange.stop), direction[1:])

def colRecurse(oldrange, direction):
    if oldrange.start == oldrange.stop:
        return oldrange
    if direction[0] == 'L':
        return colRecurse(range(oldrange.start, oldrange.stop - int(((oldrange.stop - oldrange.start) + 1) / 2)), direction[1:])
    elif direction[0] == 'R':
        return colRecurse(range(oldrange.start + (int(((oldrange.stop - oldrange.start) + 1) / 2)), oldrange.stop), direction[1:])

def Part1(lines):
    top = 0
    for line in lines:
        rowstart = range(0, 127)
        colstart = range(0, 7)
        row = rowRecurse(rowstart, line.strip()[:-3]).start
        col = colRecurse(colstart, line.strip()[7:]).start
        seat = (row * 8) + col
        if seat > top:
            top = seat
    print(top)

def Part2(lines):
    seats = []
    for line in lines:
        rowstart = range(0, 127)
        colstart = range(0, 7)
        row = rowRecurse(rowstart, line.strip()[:-3]).start
        col = colRecurse(colstart, line.strip()[7:]).start
        seat = (row * 8) + col
        seats.append(seat)
    seats.sort()
    seatRange = range(seats[0], seats.pop() + 1)
    seatList = [*seatRange]
    print((set(seatList) - set(seats)))


with open("day5-input.txt") as file:
  lines = file.readlines()

Part1(lines)
Part2(lines)
