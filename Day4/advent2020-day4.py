import re

def processPassport(documents):
    validpassportkeys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    if documents:
        passport = " ".join(documents)
        passportContents = {}
        for entry in passport.split(' '):
            kv = entry.split(':')
            passportContents[kv[0]] = kv[1]

        if all(key in passportContents for key in validpassportkeys):
            #print(passportContents, 'passport')
            return 1

def validHeight(height):
    r = re.match('^(\d+)cm$', height)
    if(r):
        if 150 <= int(r.groups()[0]) <= 193:
            return True

    r = re.match('^(\d+)in$', height)
    if(r):
        if 59 <= int(r.groups()[0]) <= 76:
            return True
    
    return False

def validHairColor(color):
    if(re.match('^#([a-f0-9]{6})$', color)):
        return True
    return False

def validEyeColor(color):
    colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if color in colors:
        return True
    return False

def validPassport(documents):
    passport = " ".join(documents)
    passportContents = {}
    for entry in passport.split(' '):
        kv = entry.split(':')
        passportContents[kv[0]] = kv[1]
    
    if (1920 <= int(passportContents['byr']) <= 2002 and
       2010 <= int(passportContents['iyr']) <= 2020 and
       2020 <= int(passportContents['eyr']) <= 2030 and
       validHeight(passportContents['hgt']) and
       validHairColor(passportContents['hcl']) and
       validEyeColor(passportContents['ecl']) and
       len(str(passportContents['pid'])) == 9):
        return True
    else:
        return False

def Part1(lines):
    passports = 0
    passportList = []
    documents = []
    valid = 0
    last = lines[-1]
    for line in lines:
        if (line == last):
            documents.append(line.strip())
            if(processPassport(documents)):
                valid += 1
            passports += 1
            documents = []
        elif (line != "\n"):
            documents.append(line.strip()) 
        else:
            if(processPassport(documents)):
                valid += 1
            passports += 1
            documents = []

    print('{valid} valid passports in {total}'.format(valid=valid, total=passports))

def Part2(lines):
    passports = 0
    documents = []
    valid = 0
    last = lines[-1]
    for line in lines:
        if (line == last):
            documents.append(line.strip())
            if(processPassport(documents) and validPassport(documents)):
                valid += 1
            passports += 1
            documents = []
        elif (line != "\n"):
            documents.append(line.strip()) 
        else:
            if(processPassport(documents) and validPassport(documents)):
                valid += 1
            passports += 1
            documents = []

    print('{valid} valid passports in {total}'.format(valid=valid, total=passports))


with open("day4-input.txt") as file:
  lines = file.readlines()

Part1(lines)
Part2(lines)