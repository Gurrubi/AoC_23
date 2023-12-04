def formatFile(file):
    aux = []

    for line in file:
        line = line.strip()
        aux.append(line)

    return aux

def isPartNumber(init_pos, last_pos, engine):
    part_number = False

    i_range = [(0,-1)[init_pos[0] > 0], (0,1)[last_pos[0] < len(engine)-1]]
    j_range = [(0,-1)[init_pos[1] > 0], (0,1)[last_pos[1] < len(engine[init_pos[0]])-1]]

    i_range = [init_pos[0]+i_range[0], last_pos[0]+i_range[1]+1]
    j_range = [init_pos[1]+j_range[0], last_pos[1]+j_range[1]+1]

    for i in range(i_range[0],i_range[1]):
        for j in range(j_range[0], j_range[1]):
            if not engine[i][j].isdigit() and not engine[i][j] == '.':
                part_number = True

    return part_number

def nextIsNumber(engine,i,j):
    number = False

    if(len(engine[i])-2 >= j):
        number = engine[i][j+1].isdigit()
    else:
        number = False
    
    return number

if __name__ == "__main__":
    part_numbers = []
    file = open("../inputs/input-Day-3.txt")
    
    engine = formatFile(file);

    curr_num = ""
    digit = False
    init_pos = last_pos = []

    for i in range(0,len(engine)):
        for j in range(0,len(engine[i])):
            if engine[i][j].isdigit():
                if not digit:
                    init_pos = [i,j]

                curr_num += engine[i][j]
                digit = True

            if(digit and not nextIsNumber(engine,i,j)):
                last_pos = [i,j]

                if isPartNumber(init_pos, last_pos, engine):
                    part_numbers.append(int(curr_num))
                
                curr_num = ""
                digit = False

    file.close()

    print(sum(part_numbers))
        

