import math

starMap = [
    '..............#.#...............#....#....',
    '#.##.......#....#.#..##........#...#......',
    '..#.....#....#..#.#....#.....#.#.##..#..#.',
    '...........##...#...##....#.#.#....#.##..#',
    '....##....#...........#..#....#......#.###',
    '.#...#......#.#.#.#...#....#.##.##......##',
    '#.##....#.....#.....#...####........###...',
    '.####....#.......#...##..#..#......#...#..',
    '...............#...........#..#.#.#.......',
    '........#.........##...#..........#..##...',
    '...#..................#....#....##..#.....',
    '.............#..#.#.........#........#.##.',
    '...#.#....................##..##..........',
    '.....#.#...##..............#...........#..',
    '......#..###.#........#.....#.##.#......#.',
    '#......#.#.....#...........##.#.....#..#.#',
    '.#.............#..#.....##.....###..#..#..',
    '.#...#.....#.....##.#......##....##....#..',
    '.........#.#..##............#..#...#......',
    '..#..##...#.#..#....#..#.#.......#.##.....',
    '#.......#.#....#.#..##.#...#.......#..###.',
    '.#..........#...##.#....#...#.#.........#.',
    '..#.#.......##..#.##..#.......#.###.......',
    '...#....###...#......#..#.....####........',
    '.............#.#..........#....#......#...',
    '#................#..................#.###.',
    '..###.........##...##..##.................',
    '.#.........#.#####..#...##....#...##......',
    '........#.#...#......#.................##.',
    '.##.....#..##.##.#....#....#......#.#....#',
    '.....#...........#.............#.....#....',
    '........#.##.#...#.###.###....#.#......#..',
    '..#...#.......###..#...#.##.....###.....#.',
    '....#.....#..#.....#...#......###...###...',
    '#..##.###...##.....#.....#....#...###..#..',
    '........######.#...............#...#.#...#',
    '...#.....####.##.....##...##..............',
    '###..#......#...............#......#...#..',
    '#..#...#.#........#.#.#...#..#....#.#.####',
    '#..#...#..........##.#.....##........#.#..',
    '........#....#..###..##....#.#.......##..#',
    '.................##............#.......#..'
]


class Vector:

    def __init__(self, x, y, px, py):
        self.x = x
        self.y = y
        self.px = px
        self.py = py

    def getTheta(self):
        rad = math.atan2(self.x, self.y)
        return rad if rad >= 0 else 2 * math.pi + rad

    def getDistance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


def calculateVector(position, otherPosition):
    return Vector(otherPosition['x'] - position['x'], position['y'] - otherPosition['y'], otherPosition['x'],
                  otherPosition['y'])


starPositions = []

for y in range(len(starMap)):
    for x in range(len(starMap[y])):
        if starMap[y][x] == '#':
            starPositions.append(dict({'x': x, 'y': y}))

print(f'All stars is {len(starPositions)}')

max = 0
for star in starPositions:
    allVectors = [calculateVector(star, otherStar) for otherStar in starPositions if not (
            star['x'] == otherStar['x'] and star['y'] == otherStar['y'])]
    angles = []
    for vector in allVectors:
        if vector.getTheta() not in angles:
            angles.append(vector.getTheta())
    if (len(angles) > max):
        max = len(angles)
        position = star

print(f'Max visible stars is {max} of Star {position}')

vectors = [calculateVector(position, otherPosition) for otherPosition in starPositions if not (
        position['x'] == otherPosition['x'] and position['y'] == otherPosition['y'])]

sortedVectors = sorted(sorted(vectors, key=lambda vector: vector.getDistance(
)), key=lambda vector: vector.getTheta())

destroyedCount = 0
previousTheta = None

while len(sortedVectors) > 0:
    currentVector = sortedVectors.pop(0)
    if previousTheta != currentVector.getTheta():
        destroyedCount += 1
        print(
            f'Destroyed {destroyedCount} stars at position {currentVector.px}, {currentVector.py}, [{currentVector.getTheta()}-{currentVector.getDistance()}]')
    else:
        sortedVectors.append(currentVector)
        if len(set([vector.getTheta() for vector in sortedVectors])) == 1:
            sortedVectors = sorted(
                sortedVectors, key=lambda vector: vector.getDistance())
            while len(sortedVectors) > 0:
                remain = sortedVectors.pop(0)
                destroyedCount += 1
                print(
                    f'Destroyed {destroyedCount} stars at position {remain.px}, {remain.py}, [{remain.getTheta()}-{remain.getDistance()}]')

    previousTheta = currentVector.getTheta()
