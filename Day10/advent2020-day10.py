def Part1(lines):
    counters = {}
    counters[1] = 0
    counters[2] = 0
    counters[3] = 0
    chargeStart = 0
    last = lines[len(lines) - 1]
    print(last)
    while chargeStart < last:
        if (chargeStart + 1) in lines:
            chargeStart += 1
            counters[1] += 1
        elif (chargeStart + 2) in lines:
            chargeStart += 2
            counters[2] += 1
        elif (chargeStart + 3) in lines:
            chargeStart += 3
            counters[3] += 1

    return counters

with open(r"day10-input.txt") as file:
    lines = [int(x.strip()) for x in file.readlines()]

lines.sort()
device = lines[len(lines) - 1] + 3
lines.append(device)
print(lines)

counters = Part1(lines)

print(counters)
print(counters[1] * counters[3])

