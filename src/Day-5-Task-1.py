# RESOLVED
# DURATION OF CODING : 1h 35m 56s

def parseInputAlmanac(file):
    file_str = ""

    for line in file:
        file_str += line

    file = file_str.split("\n")
    aux = []
    final_file = []

    file = [x for x in file if x != '']
    final_file.append([file[0].split(":")[1][1:]])

    for i in range(1,len(file)):
        if ':' not in file[i]:
            aux.append(file[i])

        elif aux != []:
            final_file.append(aux)
            aux = []

    final_file.append(aux)
    aux = []

    for i in range(0,len(final_file)):
        for j in range(0,len(final_file[i])):
            for number in final_file[i][j].split(" "):
                aux.append(int(number))
            
            final_file[i][j] = aux
            aux = []

    return final_file

if __name__ == "__main__":
    file = open("../inputs/input-Day-5.txt", "r")

    almanac = parseInputAlmanac(file)
    seeds = almanac[0][0]
    almanac.pop(0)
    value = 0
    transfor = False

    seed_values = []

    for seed in seeds:
        value = seed

        for type in almanac:
            for row in type:
                if value in range(row[1],row[1]+row[2]) and not transfor:
                    value = value - row[1] + row[0]
                    transfor = True
            
            transfor = False    
        seed_values.append(value)    

    file.close()
    print(min(seed_values))