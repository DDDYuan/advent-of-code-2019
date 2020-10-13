import utils

tunnel = '''#################################################################################
#.#...#.....#...............#.....#v....#.........#p....#...#...................#
#.#.#.#.#.#.#M#############.#.###.#####.#####.###.#.###.#.#.#################.#.#
#..n#...#.#...#.#...........#...#.......#.....#.....#.#...#...#.......#...#...#.#
#########.#####.#.###########.#.#######.#.###########.#######.#C#####.#.#.#.###.#
#.........#.#.....#.........#.#.#.......#...........#...........#...#.#.#...#...#
#.#########.#.#########.#####.#W###.###############.###.#########.###.#.#####.###
#.Y...#...#...#.......#z......#...#.#...#...#.....#..d#.#.#..x..#...#.#.#...#.#.#
#####.#.#.#.###.#.###.#####.#####.#.#.#.#.#.#.###.###.#.#.#.###.#.#.#.#.#.#.#.#.#
#.....#.#...#...#.#.#.....#...#...#.#.#.#.#...#.......#...#.#...#.#.....#.#...#.#
#.#######.#######.#.#####.#####.#####.#.#.#############.###.#.###.#########.###.#
#...#...#.#...#...#.#...#.....#...B...#.#.....#...#.....#...#.#.....#....t#.....#
#.#.#.#.#.#.#.#.###.#.#.#####.#.#######.#.###.#.#.###.###.###.#.#####.###.#####N#
#.#...#.#...#.#.#.....#...#...#.#...#...#...#.#.#...#.#...#...#...#...#.#...#.#.#
#.#####.#####.#.#########.#.###.#.#.#.#.###.#.#.###.###.###.#######.###.###.#.#.#
#.#...#.#.......#...#.....#...#...#.#.#.#.#.#...#.#.....#...#.....#.#...#...#.#.#
#.#.###.#########.#.#.###.###.#####.#.#.#.#.#####.#######.###.###.#.#.###.###.#.#
#.#...#.#...#.....#.#...#...#.#...#.#.#.#.#.#.....#.....#...#.#.#...#...#.#...#.#
#.###.#.#.#.#.#####.#.#.#####.#.###.#.###.#.#.###.###.#.###.#.#.#####.#.#J#E###.#
#.....#.#.#...#...#.#.#.....#.#.....#...#.#.#.#.......#.#...#.#...#...#...#.....#
#######.#.#####.###.#######.#.#########.#.#.#.#########.#.###.#.#.#.#########.###
#.......#.#.....#.I.#.....#.............#...#...#.....#.#...#.#.#.#.........#...#
#.#######.###.###.#.#####.#.###########.#.###.#.###.###.###.#####.#########.###.#
#.......#...#.#...#.....#.#.#.......#...#.#...#.#...#.....#.........#.....#.#...#
#.#####.###.#.#.#######.#.###.#####.#.###.#####.#.###.#######.#####.#.###.#.###.#
#.#...#...#.#.#.......#.#.....#.#...#...#.#...#.#...#u#.....#...#...#.#.#.#...#.#
#.###.#.###.#.#######.#.#######.#.#####.#.#.#.#.#.#.#.#.#.#.###.#####.#.#.###.#.#
#...#.#...#.....#.....#.#.....#...#...#.#...#.#.#.#...#.#.#...#.#.....#.#.#...#.#
###.#.###.#####.#.#####.#.#.#.#.###.#.#.#####.#.#.#####.#.#.###.#.#####.#.#.###.#
#...#...#.......#.#.....#.#.#.#.....#.#.#.....#.#.#.....#.#.#...#.....#.#.#.#..k#
#.###.###########.#.#######.#.#######.#.#.#####.###.#####.###.#.#####.#.#.#.#.###
#...#...........#.#.....#...#.......#.#.#...#.........#...#...#.#.....#.#...#.#.#
###.#.###.###.###.#####.#.#.#######.#.#.###.#.#########.#.#.###.#.#####.#####.#.#
#.#.#...#...#.#...#...#.#.#.#.....#.#.#.#.#.#...#.......#.#.#...#...#.....#...#.#
#.#.###.###.#.#.###.#.#.#.###.###.###.###.#.#####.#######.#.#.#####.#.#.#.#.###.#
#.#.#.....#.#.#.....#g#...#...#.#...#...#.#.......#...#...#.#...#.#.#.#.#.#.....#
#.#.#######.#.#######.###.#.###.###.###.#.#########.###.###.###.#.#.#.#.#######.#
#...#.....#.#.#.....#.#...#.......#.#...#.....#.......#.#.#...#...#.#.#.......#.#
#.###.###.#.#.#.###.#.###########.#.#.###.###.#.#####.#.#.###.#####.#.#######.#.#
#.....#.....#...#...#.A...........#.........#.......#.R.....#.......#.......#...#
#######################################.@.#######################################
#.....#.........#...........#......r#...........#.#...#.............#.......#...#
###.###.#.#######.#.#######.#.#####.###.#.#.###.#.#.#.#.#######.###.#.#####.###.#
#...#...#.........#...#...#.#.....#.....#.#...#...#.#...#...#...#.#.#.....#.....#
#.###.###############.#.###.#.###.#####.#.###.#####.#######.#.###.#.#####.#######
#.....#.......#.#.....#...#.#.#...#.....#.#.#.#.....#.......#.#...#.....#.......#
#.#######.###.#.#.#######.#.###.#.#######.#.#.#.#########.###.#.#######G#.#####.#
#.....#...#.#...#.#.......#...#.#.#.....#...#.#.#.....#..a#...#.#.....#.#i....#.#
#####.#.###.###.#.###.#.#####.#.###.###.#####.#.###.#.#.#.#.###.#.###.#.#######.#
#...#.#.#.....#.#...#.#.#.....#.....#...#...#.......#...#.#.#.....#.#.........#.#
#.#.#.#.#.#####.###.#.###.###########.###.#.#.#############.#.#####.#########.#.#
#.#.#.#.#.......#...#.....#.....#...#...#.#.#.#.............#.......#...#.....O.#
#.#.#.#.#########.#######.#.###.#.#.###.#.#.###.###########.#########.#.#######.#
#.#.#e#.........#.#.....#...#...#.#.....#.#.#...#...........#.......#.#.....#...#
###.#.#########.#.#.###.#####P###.#######.#.#.#########.#####.#####.#.#####.#.###
#...#.......#...#...#.#.#...#...#...#...#.#...#.......#.#w....#f..#...#...#.#...#
#.#.#######.#.#######.#.#.#####.#.#.#.#.#.#.###.#####.###.###.#.#.#####.#.#.#####
#.#.#...#...#.........#.#...#...#.#...#.#.#.#.......#.#...#...#.#...#...#.#.#...#
#.#.#.###.#######.###.#.#.#.#.###.#####.#.###.#######.#.#######.###.#.###.#.#.#.#
#.#...#...#.....#...#.#.#.#...#..o..#...#...#...#...#.#...#...F.#...#...#.#...#.#
#.#####.###.###.###.###.#####.#####.#.#.#.#.#.###.#.#.###.#.#####L###.#.#.#####.#
#.......#...#.#.#...#.#.....#.....#.#.#.#.#...#...#.#.#...#...#...#...#.#.....#.#
#K#######.#.#.#.#.###.#####.#####X###.#.#######.###.#.#.#######.#####.#.#######.#
#....j..#.#.#.....#...#.....#...#...#.#.#.......#...#.#.....#...#.S.#.#.........#
#######.###.#####.#.###.#####.#.###.#.###.#######.###.#####.#.###.#.#.###########
#.....#...#.....#.#...#.......#...#.#...#.....#.#.#.......#.#l....#.#.#...#.....#
#T#.#####.#####.#####.#.#########.#.###.#.###.#.#.#####.#.#.#######.#.#.###.###.#
#.#.....#.#.....#.....#.#.......#.#.#...#c#.#.#.....#...#.#...Z.#...#.#.....#...#
#.###.###.#.#.###.#####.#.#####.#.#.#.#.#.#.#.#####.#.#######.###.###.#.#####.#.#
#...#...#...#.#...#...#...#...#.#.#.#.#.#...#.....#...#.....#.#s..#...#.#.#...#.#
###.###.#.#####.###.###.###.#.###.#.#.###.#######.###.#.#.###.#.###.###Q#.#.#####
#.#.#.#.#.#...#...#...#.#...#.....#.#...#.#.....#.#...#.#.#...#.V.#.#...#.#.....#
#.#.#.#.#.#.#.###.#.#.#.#.#########.###.#.#.###.#.#####.#.#.#####.#.#.###.#####.#
#...#.#...#.#...#.#.#.#.#...#...#...#...#.#...#y..#...#.#.#.......#.#.#.......#.#
#.###.#####.###.#.###.#.###.#.###.###.#.#####.#####.#.#.#.#########.#.#.#.#####.#
#.#.....#...#.#...#...#.#...#.#.D.#.U.#.#.....#...#.#.#.#.......#...#..b#.#.....#
#.#####.#.###.#####.###.#.###.#.###.###.#.#####.#.#.#.#.#######.#.#######.#.###.#
#.H...#.#...#...........#.#...#.#.....#.#m......#...#...#.......#.#...#...#.#...#
#####.#.###.#############.#.#.#.#####.#.#.###############.#######.#.#.#####.#.###
#..q......#...............#.#.........#.#...............#...........#.......#..h#
#################################################################################'''

testTunnel = '''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''

testTunnel2 = '''#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################'''

testTunnel3 = '''########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################'''


def findStartPosition(graph):
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x] == '@':
                return x, y
    raise ValueError('Cannot find start position.')


def getPossibleTargets(startPosition, collectedKeys, grid):
    frontier = [(startPosition, 0)]
    reached = []
    targets = []

    def inFrontier(currentPosition):
        for item in frontier:
            coordinate, distance = item
            if coordinate == currentPosition:
                return True
        return False

    while len(frontier) != 0:
        (x, y), distanceToStart = frontier.pop(0)
        reached.append((x, y))
        for position in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            nextX, nextY = position
            if nextX >= 0 and nextY >= 0 and position not in reached and not inFrontier(position):
                next = grid[nextY][nextX]
                if next == '.' or next == '@':
                    frontier.append((position, distanceToStart+1))
                if 'A' <= next <= 'Z':
                    if next.lower() in collectedKeys:
                        frontier.append((position, distanceToStart+1))
                if 'a' <= next <= 'z':
                    if next in collectedKeys:
                        frontier.append((position, distanceToStart+1))
                    else:
                        targets.append((position, next, distanceToStart+1))
                        reached.append(position)
    return targets


def calculateShortestPath(startPosition, collectedKeys, grid):
    targets = getPossibleTargets(startPosition, collectedKeys, grid)
    print(f'Possible targets of {startPosition}[{grid[startPosition[1]][startPosition[0]]}] is {targets}, collected keys: {collectedKeys}')
    if len(targets) == 0:
        return 0
    paths = []
    for target in targets:
        targetPosition, targetName, targetDistance = target
        paths.append(targetDistance + calculateShortestPath(targetPosition, collectedKeys.copy() + [targetName], grid))
    return min(paths)


def partOne():
    grid = utils.parseGraph(tunnel)
    start = findStartPosition(grid)
    print(f'Start position is {start}')
    print(f'Shortest path is {calculateShortestPath(start, [], grid)}')


if __name__ == '__main__':
    partOne()
