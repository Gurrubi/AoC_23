file = open("../inputs/input-Day-1.txt")

last = first = "0"
first_num = True
sum = 0

for line in file:
    for character in line:
        if (character.isdigit()):
            if(first_num):
                first = character
                first_num = False

            last = character

    sum += int(first+last)
    first_num = True
    first = last = "0"

file.close();

print(sum)