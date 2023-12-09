# RESOLVED
# DURATION OF CODING: 0h 33m 17s

def parseFile(file):
    nodes = {}

    lines = [line.strip() for line in file if line.strip() != ""] 
    rules = [(0,1)[c == 'R'] for c in lines[0]]

    lines.pop(0)

    for line in lines:
        node = line.split("=")[0].split()[0]
        left = line.split("=")[1].split(",")[0].split("(")[1]
        right = line.split("=")[1].split(",")[1].split(")")[0][1:]

        nodes[node] = [left, right]

    return [rules, nodes]


if __name__ == "__main__":
    file = open("../inputs/input-Day-8.txt", "r")

    info = parseFile(file)

    file.close()

    rules = info[0]
    nodes = info[1]

    start = 'AAA'
    steps = 0

    while start != 'ZZZ':
        start = nodes[start][rules[steps % len(rules)]]
        steps += 1

    print(steps)

