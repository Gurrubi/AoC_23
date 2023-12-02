def isContained(sub_number, number):
    contained = True
    i = 0;

    while i in range(0,len(sub_number)) and contained:
        if sub_number[i] != number[i]:
            contained = False

        i+=1

    return contained


if __name__ == "__main__":        
    file = open("../inputs/input-Day-1.txt")    
    #file = []

    #file.append("sevenfour223qvxrdrvqgkqpctbrzeightqtxjnhgz")
    #file.append("dzrt197twonine")
    #file.append("7two8sevencvfjhqmdtfone")


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

    sum = i = 0

    first_num = True
    found = contained = False

    for line in file:
        line = line.strip()
        for character in line:
            if (character.isdigit()):
                if(first_num):
                    first = character
                    first_num = False
                
                last = character
                sum_str = "";

            else:
                sum_str+=character

                while i in range(0, len(numbers_str)) and not found and not contained:
                    if sum_str == numbers_str[i]:
                        if first_num:
                            first = numbers[sum_str]
                            first_num = False

                        last = numbers[sum_str]
                        #print(f"· {sum_str}")
                        sum_str = character
                        found = True
                    
                    elif isContained(sum_str, numbers_str[i]):
                        contained = True

                    else:
                        i += 1
                        
                if not found and not contained:
                    sum_str = character

                found = contained = False
                i = 0                
        
        print(f"{line} - {first}{last}")
        sum += int(first+last)
        first_num = True
        sum_str = "";
        first = last = "0"

    file.close();

    print(sum)