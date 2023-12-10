# RESOLVED
# DURATION OF CODING: 0h 8m 37s
# Resolved with recursiviness

def parseFile(file):
    lines = [line.strip().split() for line in file]
    nums = []

    for i in range(0,len(lines)):
        nums.append([int(lines[i][x]) for x in range(0,len(lines[i]))])

    return nums

def getDiffs(line):
    aux = []
    all_diffs = []

    for i in range(len(line)-1,0,-1):
        aux.insert(0,line[i]-line[i-1])

    all_diffs.append(aux)

    if(not allZero(aux)):
        for el in getDiffs(aux):
            all_diffs.append(el)

    return all_diffs

def allZero(line):
    zero = True
    x = 0

    while x in range(0, len(line)) and zero:
        zero = line[x] == 0
        x+=1
    
    return zero


if __name__ == "__main__":
    file = open("../inputs/input-Day-9.txt","r")

    lines = parseFile(file)
    diffs = []
    sum = 0
    
    file.close()

    for line in lines:
        diffs = getDiffs(line)
        diffs.insert(0,line)

        value = 0
        for i in range(len(diffs)-1,0,-1):
            value = diffs[i-1][0] - value

        sum += value
    
    print(sum)