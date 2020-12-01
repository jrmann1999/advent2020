numbers = [#listofnumbers]
target = 2020

def prob2(numbers, target):
    for counter, num in enumerate(numbers):
        for counter2, num2 in enumerate(numbers[counter+1:]):
            if (num + num2) == target:
                print (num, num2)
                print (num * num2)
                return


def prob3(numbers, target):
     for counter, num in enumerate(numbers):
        for counter2, num2 in enumerate(numbers[counter+1:]):
            for counter3, num3 in enumerate(numbers[counter2+1:]):
                if (num + num2 + num3) == target:
                    print (num, num2, num3)
                    print (num * num2 * num3)
                    return

prob2(numbers, target)
prob3(numbers, target)