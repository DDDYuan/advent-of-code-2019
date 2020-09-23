import math


class Coordinate:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __add__(self, other):
        return Coordinate(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __str__(self):
        return f'[{self.__x},{self.__y},{self.__z}]'

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y and self.__z == other.__z

    def calculateAbsSum(self):
        return abs(self.__x) + abs(self.__y) + abs(self.__z)

    def calculateDifference(self, other):
        if self.__x > other.__x:
            x = -1
        elif self.__x < other.__x:
            x = 1
        else:
            x = 0
        if self.__y > other.__y:
            y = -1
        elif self.__y < other.__y:
            y = 1
        else:
            y = 0
        if self.__z > other.__z:
            z = -1
        elif self.__z < other.__z:
            z = 1
        else:
            z = 0
        return Coordinate(x, y, z)

    def copy(self):
        return Coordinate(self.__x, self.__y, self.__z)


class Star:
    def __init__(self, position: Coordinate, velocity: Coordinate):
        self.__position = position
        self.__velocity = velocity

    def __str__(self):
        return f'Star at {str(self.__position)} with velocity {str(self.__velocity)}'

    def updatePosition(self):
        self.__position = self.__position + self.__velocity

    def updateVelocity(self, otherStar):
        self.__velocity = self.__velocity + self.__position.calculateDifference(otherStar.getPosition())

    def calculateKin(self):
        return self.__velocity.calculateAbsSum()

    def calculatePos(self):
        return self.__position.calculateAbsSum()

    def calculateEnergy(self):
        return self.calculateKin() * self.calculatePos()

    def getPosition(self):
        return self.__position

    def __eq__(self, other):
        return self.__position == other.__position and self.__velocity == other.__velocity

    def copy(self):
        return Star(position=self.__position.copy(), velocity=self.__velocity.copy())


class System:
    def __init__(self, stars):
        self.__stars = [star.copy() for star in stars]
        self.__initStars = [star.copy() for star in stars]
        self.__timeStep = 0

    def __str__(self):
        return f'System at time step {self.__timeStep} is:\n' \
               + '\n'.join([str(star) for star in self.__stars]) \
               + '\nInit condition is:\n' \
               + '\n'.join([str(star) for star in self.__initStars]) \
               + f'\nTotal energy is {self.calculateTotalEnergy()}\n'

    def calculateTotalEnergy(self):
        return sum([star.calculateEnergy() for star in self.__stars])

    def nextStep(self):
        self.__timeStep += 1
        for star in self.__stars:
            for other in self.__stars:
                star.updateVelocity(other)
        for star in self.__stars:
            star.updatePosition()

    def getStep(self):
        return self.__timeStep

    def equalToInit(self):
        for index in range(len(self.__stars)):
            if self.__stars[index] != self.__initStars[index]:
                return False
        return True


def partOne():
    system = System(stars=[ \
        Star(position=Coordinate(6, 10, 10), velocity=Coordinate(0, 0, 0)), \
        Star(position=Coordinate(-9, 3, 17), velocity=Coordinate(0, 0, 0)), \
        Star(position=Coordinate(9, -4, 14), velocity=Coordinate(0, 0, 0)), \
        Star(position=Coordinate(4, 14, 4), velocity=Coordinate(0, 0, 0))])

    system.nextStep()
    while not system.equalToInit():
        print(system)
        system.nextStep()


def partTwo():
    xs, xvs = [6, -9, 9, 4], [0, 0, 0, 0]
    ys, yvs = [10, 3, -4, 14], [0, 0, 0, 0]
    zs, zvs = [10, 17, 14, 4], [0, 0, 0, 0]

    def calculateChange(list):
        result = []
        for item in list:
            total = 0
            for other in list:
                if other > item:
                    total += 1
                elif other < item:
                    total -= 1
            result.append(total)
        return result

    def sumList(list1, list2):
        return [list1[i] + list2[i] for i in range(len(list1))]

    def calculateReturnToInitSteps(positionList, velocityList):
        step = 0
        initP, initV = positionList.copy(), velocityList.copy()
        while step == 0 or not (initP == positionList and initV == velocityList):
            change = calculateChange(positionList)
            velocityList = sumList(velocityList, change)
            positionList = sumList(positionList, velocityList)
            step += 1
            print(f'At step {step}, position {positionList}, velocity {velocityList}, init {initP}, {initV}')
        print(f'Step {step} to init.')
        return step

    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    def lcmOfList(list):
        result = list[0]
        for i in range(1, len(list)):
            result = lcm(result, list[i])
        return result

    stepx = calculateReturnToInitSteps(xs, xvs)
    stepy = calculateReturnToInitSteps(ys, yvs)
    stepz = calculateReturnToInitSteps(zs, zvs)

    print(f'Step for x,y,z axis are {stepx}, {stepy}, {stepz}')
    print(f'The LCM of above is {lcmOfList([stepx, stepy, stepz])}')


if __name__ == "__main__":
    partTwo()
