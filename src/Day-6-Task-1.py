# RESOLVED
# DURATION CODING: 0h 30m 21s

def formatFile(file):
    race = {"time":[], "distance":[]}
    lines = [line.strip().split()[1:] for line in file]

    race["time"] = [int(x) for x in lines[0]]
    race["distance"] = [int(x) for x in lines[1]]

    return race

if __name__ == "__main__":
    file = open("../inputs/input-Day-6.txt", "r")
    valid = []
    ways_to_win = 0

    races = formatFile(file)

    file.close()

    for i in range(0,len(races["time"])):
        race = races["time"][i]
        race_dist = races["distance"][i]

        for seg_btn in range(1,race+1):
            distance = (race-seg_btn) * seg_btn

            if distance > race_dist:
                ways_to_win += 1

        valid.append(ways_to_win)
        ways_to_win = 0

    ways_to_win = 1

    for way in valid:
        ways_to_win *= way

    print(ways_to_win)