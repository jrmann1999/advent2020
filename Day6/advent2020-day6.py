def Part1(lines):
    last = lines[-1]
    form = []
    total = 0
    for line in lines:
        if ((line == last) or (line == "\n")):
            if(line == last):
                form.append(line.strip())
            questions = {}
            for entry in form:
                for answer in entry:
                    questions[answer] = 1
            print(questions, len(questions.keys()))
            total += len(questions.keys())
            form = []
        else:
            form.append(line.strip())
    
    print(total)

def Part2(lines):
    last = lines[-1]
    form = []
    total = 0
    linecount = 0
    for line in lines:
        if ((line == last) or (line == "\n")):
            if(line == last):
                form.append(line.strip())
                linecount += 1
            questions = {}
            for entry in form:
                for answer in entry:
                    if answer in questions.keys():
                        questions[answer] += 1
                    else:
                        questions[answer] = 1

            combinedquestions = {}
            for k, v in questions.items():
                if v == linecount:
                    combinedquestions[k] = v
            print(combinedquestions, linecount)
            total += len(combinedquestions.keys())
            form = []
            linecount = 0
        else:
            form.append(line.strip())
            linecount += 1
    
    print(total)        
                

with open("day6-input.txt") as file:
  lines = file.readlines()

#Part1(lines)
Part2(lines)