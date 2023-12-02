def formatGame(game):
    game_info = {"id":0, "rolls": []}
    rolls = []

    game = game.strip()
    game_info["id"] = int(game.split(":")[0].split(" ")[1])

    game = game.split(":")[1]

    game = game.split(";")

    for cubes in game:
        rolls.append(cubes.split(","))

    for i in range(0, len(rolls)):
        for j in range(0, len(rolls[i])):
            rolls[i][j] = rolls[i][j][1:]

    game_info["rolls"] = rolls

    return game_info

def resetCubesRolled():
    return {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

def validGame(cubes, max):
    return cubes["red"] <= max["red"] and cubes["green"] <= max["green"] and cubes["blue"] <= max["blue"]




if __name__ == "__main__":

    MAXCUBES = {
        "red" : 12,
        "green" : 13,
        "blue" : 14
    }

    cubes_in_roll = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    ids = []
    file = open("../inputs/input-Day-2.txt")
    validRoll = True

    for line in file:
        game = formatGame(line)

        for roll in game["rolls"]:
            for cube in roll:
                key = cube.split(" ")[1]
                value = int(cube.split(" ")[0])

                cubes_in_roll[key] = value
        
            validRoll = validRoll and validGame(cubes_in_roll, MAXCUBES)
            cubes_in_roll = resetCubesRolled()
        
        if validRoll:
            ids.append(game["id"])
        
        validRoll = True

    file.close()

    print(sum(ids))