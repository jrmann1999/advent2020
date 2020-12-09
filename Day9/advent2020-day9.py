
def returnFactor(num, array):
    candidate = []
    for entry in array:
        if num < entry:
            continue
        rem = num - entry
        if (rem == entry):
            continue
        candidate.append(rem)

    for entry in candidate:
        if entry in array:
            return []

    return candidate


def Part1(lines):
    numbers = []
    for line in lines:
        #print(numbers)
        num = int(line.strip())
        if len(numbers) < 25:
            numbers.append(num)
        else:
            t = returnFactor(num, numbers)
            if (not t):
                numbers.pop(0)
                numbers.append(num)
            else:
                return(num)
    return None

def Part2(lines):
    num = Part1(lines)

    numbers = []
    for line in lines:
        num2 = int(line.strip())
        if len(numbers) < 25:
            numbers.append(num2)
        else:
            count = 0
            for i, entry in enumerate(numbers, 1):
                count += entry
                if i > 1:
                    if count == num:
                        return(numbers[:i])
            numbers.pop(0)
            numbers.append(num2)

with open(r"day9-input.txt") as file:
    lines = file.readlines()

print(Part1(lines))
num = Part2(lines)
num.sort()
print(num.pop(0) + num.pop())


