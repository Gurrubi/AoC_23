def parseStratchCards(file):
    stratchcards = {"winning" : [], "numbers": []}
    
    for line in file:
        winning_numbers = []
        numbers = []

        line = line.strip()
        line = line.split(":")[1]

        winning_line = line.split("|")[0].split(" ")
        numbers_line = line.split("|")[1].split(" ");

        for el in winning_line:
            if el.isdigit():
                winning_numbers.append(int(el))

        for el in numbers_line:
            if el.isdigit():
                numbers.append(int(el))

        stratchcards["winning"].append(winning_numbers)
        stratchcards["numbers"].append(numbers)
    
    return stratchcards

if __name__ == "__main__":
    file = open("../inputs/input-Day-4.txt", "r")

    stratchcards = parseStratchCards(file)
    card_value = 0
    first = True

    points = []

    for cards in range(0,len(stratchcards["winning"])):
        for i in range(0,len(stratchcards["winning"][cards])):
            if stratchcards["winning"][cards][i] in stratchcards["numbers"][cards]:
                card_value = (2*card_value, card_value+1)[first]
                first = False

        if card_value != 0:
            points.append(card_value)
            card_value = 0
            first = True


    print(sum(points))