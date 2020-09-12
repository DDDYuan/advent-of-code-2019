import itertools


class Amp:
    setting = None
    pointer = 0
    settingSet = False
    codes = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 42, 51, 76, 93, 110, 191, 272, 353, 434, 99999, 3, 9, 1002, 9, 2, 9, 1001, 9, 3, 9, 1002, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 1002, 9, 3, 9, 4, 9, 99, 3, 9, 1002, 9, 4, 9, 101, 5, 9, 9, 1002, 9, 3, 9, 1001, 9, 4, 9, 1002, 9, 5, 9, 4, 9, 99, 3, 9, 1002, 9, 5, 9, 101, 3, 9, 9, 102, 5, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 5, 9, 101, 5, 9, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102,
             2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99]

    def __init__(self, setting):
        self.setting = setting

    def parseCommand(self, code):
        fullCommand = str(code).rjust(5, '0')
        opCode = fullCommand[-2:]
        firstType = fullCommand[-3]
        secondType = fullCommand[-4]
        return (int(opCode), int(firstType), int(secondType))

    def run(self, input):
        result = None
        inputSet = False
        while(self.codes[self.pointer] != 99):
            currentCode = self.codes[self.pointer]
            if currentCode == 3:
                if not self.settingSet:
                    print('Set setting rate to ' +
                          str(self.setting))
                    self.codes[self.codes[self.pointer+1]
                               ] = self.setting
                    self.settingSet = True
                elif not inputSet:
                    print('Set input to ' + str(input) + ' on setting ' + str(self.setting))
                    self.codes[self.codes[self.pointer+1]] = input
                    inputSet = True
                else:
                    print('Wait for input. Current output is ' + str(result))
                    return (result, False)
                self.pointer += 2
                continue
            elif currentCode == 4:
                result = self.codes[self.codes[self.pointer+1]]
                print('Output. value is ' + str(result))
                self.pointer += 2
                continue
            else:
                (opCode, firstType, secondType) = self.parseCommand(
                    self.codes[self.pointer])
                if opCode == 1:
                    firstNumber = self.codes[self.pointer +
                                             1] if firstType == 1 else self.codes[self.codes[self.pointer+1]]
                    secondNumber = self.codes[self.pointer +
                                              2] if secondType == 1 else self.codes[self.codes[self.pointer+2]]
                    result = firstNumber + secondNumber
                    self.codes[self.codes[self.pointer+3]] = result
                elif opCode == 2:
                    firstNumber = self.codes[self.pointer +
                                             1] if firstType == 1 else self.codes[self.codes[self.pointer+1]]
                    secondNumber = self.codes[self.pointer +
                                              2] if secondType == 1 else self.codes[self.codes[self.pointer+2]]
                    result = firstNumber * secondNumber
                    self.codes[self.codes[self.pointer+3]] = result
                elif opCode == 5:
                    condition = self.codes[self.pointer +
                                           1] if firstType == 1 else self.codes[self.codes[self.pointer+1]]
                    if condition != 0:
                        self.pointer = self.codes[self.pointer +
                                                  2] if secondType == 1 else self.codes[self.codes[self.pointer+2]]
                    else:
                        self.pointer += 3
                    continue
                elif opCode == 6:
                    condition = self.codes[self.pointer +
                                           1] if firstType == 1 else self.codes[self.codes[self.pointer+1]]
                    if condition == 0:
                        self.pointer = self.codes[self.pointer +
                                                  2] if secondType == 1 else self.codes[self.codes[self.pointer+2]]
                    else:
                        self.pointer += 3
                    continue
                elif opCode == 7:
                    firstNumber = self.codes[self.pointer +
                                             1] if firstType == 1 else self.codes[self.codes[self.pointer+1]]
                    secondNumber = self.codes[self.pointer +
                                              2] if secondType == 1 else self.codes[self.codes[self.pointer+2]]
                    self.codes[self.codes[self.pointer+3]
                               ] = 1 if firstNumber < secondNumber else 0
                elif opCode == 8:
                    firstNumber = self.codes[self.pointer +
                                             1] if firstType == 1 else self.codes[self.codes[self.pointer+1]]
                    secondNumber = self.codes[self.pointer +
                                              2] if secondType == 1 else self.codes[self.codes[self.pointer+2]]
                    self.codes[self.codes[self.pointer+3]
                               ] = 1 if firstNumber == secondNumber else 0
                self.pointer += 4
                continue
        print('Run to end')
        return (result, True)

maxThruster = 0
for permutation in itertools.permutations([5,6,7,8,9]):
    amps = []
    for setting in permutation:
        amps.append(Amp(setting))
    currentIndex = 0
    thruster = 0
    end = False
    while not end:
        (output, runEnd) = amps[currentIndex].run(thruster)
        thruster = output
        if runEnd and currentIndex == 4:
            end = True
        else:
            currentIndex = 0 if currentIndex + 1 == 5 else currentIndex + 1
    print('Thruster of ' + str(permutation) + ' is ' + str(thruster))
    maxThruster = thruster if thruster > maxThruster else maxThruster
    input('-----')

print('Max thruster is ' + str(maxThruster))
