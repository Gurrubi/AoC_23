def isContained(sub_number, number):
    contained = True
    i = 0;

    while i in range(0,len(sub_number)) and contained:
        if sub_number[i] != number[i]:
            contained = False

        i+=1

    return contained

def isFound(sub_number, number):
    return sub_number == number


if __name__ == "__main__":        
    file = open("../inputs/input-Day-1.txt")    

    numbers = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }

    numbers_str = list(numbers.keys());

    last = first = "0"
    sum_str = ""

    sum = i = j = 0

    first_num = contained = True
    found = False


    for line in file:
        line = line.strip()
        while i in range(0,len(line)):
            if (line[i].isdigit()):
                if(first_num):
                    first = line[i]
                    first_num = False
                
                last = line[i]
                sum_str = "";

            else:
                j = i+1
                k = 0
                
                sum_str = line[i];

                while j in range(i+1,len(line)) and contained and not found:
                    sum_str += line[j]

                    print(sum_str)

                    while k in range (0,len(numbers_str)) and contained and not found:
                        contained = isContained(sum_str,numbers_str[k])
                        found = isFound(sum_str, numbers_str[k])

                        k += 1
                    
                    if found:
                        if first_num:
                            first = numbers[sum_str]
                            first_num = False

                        last = numbers[sum_str]
                    
                    k = 0
                    j += 1
                
                contained = True
                found = False

            i += 1

        print(f"{line} - {first}{last}")
        sum += int(first+last)
        first_num = True
        sum_str = "";
        first = last = "0"

    file.close();

    print(sum)