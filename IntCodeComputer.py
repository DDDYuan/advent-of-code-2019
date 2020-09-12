class IntCodeComputer:
    codes = None
    pointer = 0
    relativeBase = 0
    inputs = None
    end = False

    def __init__(self, codes=[], inputs=[]):
        self.codes = codes + 10000000*[0]
        self.inputs = inputs

    def reset(self):
        self.pointer = 0

    def isEnd(self):
        return self.end

    def appendInputs(self, inputs):
        self.inputs = self.inputs + inputs

    def parseCommandMode(self, code):
        fullCommand = str(code).rjust(5, '0')
        opCode = fullCommand[-2:]
        firstType = fullCommand[-3]
        secondType = fullCommand[-4]
        outType = fullCommand[-5]
        return (int(opCode), int(firstType), int(secondType), int(outType))

    def parseValue(self, type, parameterPosition):
        if type == 0:
            return self.codes[self.codes[parameterPosition]]
        elif type == 1:
            return self.codes[parameterPosition]
        elif type == 2:
            return self.codes[self.relativeBase + self.codes[parameterPosition]]
        else:
            print('INVALID PARAMETER TYPE: ' + str(type))
            return None

    def getPosition(self, type, index):
        if type == 0:
            return self.codes[index]
        elif type == 1:
            return index
        elif type == 2:
            return self.codes[index] + self.relativeBase
        else:
            print('INVALID PARAMETER TYPE: ' + str(type))
            return None

    def runToOutput(self):
        while not self.end:
            current = self.codes[self.pointer]
            (opCode, firstType, secondType, outType) = self.parseCommandMode(current)
            if opCode == 1:
                firstNumber = self.parseValue(firstType, self.pointer+1)
                secondNumber = self.parseValue(secondType, self.pointer+2)
                self.codes[self.getPosition(outType, self.pointer+3)] = firstNumber + secondNumber
                self.pointer += 4
                continue
            elif opCode == 2:
                firstNumber = self.parseValue(firstType, self.pointer+1)
                secondNumber = self.parseValue(secondType, self.pointer+2)
                self.codes[self.getPosition(outType, self.pointer+3)] = firstNumber * secondNumber
                self.pointer += 4
                continue
            elif opCode == 5:
                condition = self.parseValue(firstType, self.pointer+1)
                if condition != 0:
                    self.pointer = self.parseValue(secondType, self.pointer+2)
                else:
                    self.pointer += 3
                continue
            elif opCode == 6:
                condition = self.parseValue(firstType, self.pointer+1)
                if condition == 0:
                    self.pointer = self.parseValue(secondType, self.pointer+2)
                else:
                    self.pointer += 3
                continue
            elif opCode == 7:
                firstNumber = self.parseValue(firstType, self.pointer+1)
                secondNumber = self.parseValue(secondType, self.pointer+2)
                self.codes[self.getPosition(outType, self.pointer+3)] = 1 if firstNumber < secondNumber else 0
                self.pointer += 4
                continue
            elif opCode == 8:
                firstNumber = self.parseValue(firstType, self.pointer+1)
                secondNumber = self.parseValue(secondType, self.pointer+2)
                self.codes[self.getPosition(outType, self.pointer+3)] = 1 if firstNumber == secondNumber else 0
                self.pointer += 4
                continue
            elif opCode == 3:
                inputValue = self.inputs.pop(0) if len(
                    self.inputs) > 0 else int(input('Provide your input: '))
                print('Set input value ' + str(inputValue))
                position = self.codes[self.pointer+1] if firstType == 0 else self.codes[self.pointer+1] + self.relativeBase
                self.codes[position] = inputValue
                self.pointer += 2
                continue
            elif opCode == 4:
                result = self.parseValue(firstType, self.pointer+1)
                print('Output. value is ' + str(result))
                self.pointer += 2
                return result
            elif opCode == 9:
                self.relativeBase += self.parseValue(firstType, self.pointer+1)
                self.pointer += 2
                continue
            elif opCode == 99:
                print('Run to end.')
                self.end = True
                continue
            else:
                print('NOT A VALID CODE: ' + str(opCode))
                return None
        return None
