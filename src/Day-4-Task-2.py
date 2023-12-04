# INTENTO
# NO SE LLEGO A COMPLETAR
# :C

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

def checkNextWinnings(stratchcards, actual, n):
    total_winning_cards = 0
    winning_cards = 0;
    tab=""

    for cards in range(actual, n):
        for i in range(0, len(stratchcards["winning"][cards])):
            if stratchcards["winning"][cards][i] in stratchcards["numbers"][cards]:
                    winning_cards += 1

        if winning_cards != 0:
            bot = cards+1
            top = bot + winning_cards
            tab += "\t"

            print(f"{tab}La carta {bot} tiene {winning_cards} winning_cards")

            total_winning_cards += winning_cards
            total_winning_cards += checkNextWinnings(stratchcards, bot, top)
            winning_cards = 0
    
    return total_winning_cards

if __name__ == "__main__":
    #file = open("../inputs/input-Day-4.txt", "r")
    file = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    ]

    stratchcards = parseStratchCards(file)
    
    total_winning_cards = checkNextWinnings(stratchcards, 0, len(stratchcards["winning"]))

    print(total_winning_cards)