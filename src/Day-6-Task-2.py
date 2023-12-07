# RESOLVED
# DURATION CODING: 0h 10m 37s

def formatFile(file):
    race = {"time": 0, "distance": 0}
    lines = [line.strip().split()[1:] for line in file]
    total = ""

    for time in lines[0]:
        total += time
    race["time"] = int(total)

    total = ""

    for distance in lines[1]:
        total += distance
    race["distance"] = int(total)

    return race

if __name__ == "__main__":
    file = open("../inputs/input-Day-6.txt", "r")
    ways_to_lose = seg_btn = 0
    win = False

    race = formatFile(file)

    file.close()

    while not win:
        distance = (race["time"]-seg_btn) * seg_btn

        if distance < race["distance"]:
            ways_to_lose += 1
        else:
            win = True
        seg_btn += 1

    ways_to_win = race["time"] - (2*ways_to_lose)+1

    print(ways_to_win)