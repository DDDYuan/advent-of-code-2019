class IntCodeComputer:
    def __init__(self, codes=[], inputs=[]):
        self.__codes = list(codes)
        self.__inputs = inputs
        self.__innerInputs = []
        self.reset()

    def reset(self):
        self.__pointer = 0
        self.__relativeBase = 0
        self.__end = False

    def isEnd(self):
        return self.__end

    def appendInputs(self, inputs, asciiMode=False):
        if not asciiMode:
            self.__inputs = self.__inputs + inputs
        else:
            for input in inputs:
                self.__inputs += self.__convertToAsciiList(input)

    def __parseCommandMode(self, code):
        fullCommand = str(code).rjust(5, '0')
        opCode = fullCommand[-2:]
        firstType = fullCommand[-3]
        secondType = fullCommand[-4]
        outType = fullCommand[-5]
        return (int(opCode), int(firstType), int(secondType), int(outType))

    def __getValue(self, type, index):
        position = self.__getPosition(type, index)
        return self.__codes[position]

    def __getPosition(self, type, index):
        if type == 0:
            position = self.__codes[index]
        elif type == 1:
            position = index
        elif type == 2:
            position = self.__codes[index] + self.__relativeBase
        else:
            raise Exception(f'INVALID PARAMETER TYPE: {type}.')
        if position >= len(self.__codes):
            memoryTimes = position // len(self.__codes)
            print(f'Extend memory to {memoryTimes+1} times large.')
            self.__codes = self.__codes + [0] * memoryTimes * len(self.__codes)
        return position

    def __convertToAsciiList(self, inputValue):
        return [ord(char) for char in inputValue] + [10]

    def runToOutput(self, asciiMode=False, noPrint=False, stopAtInput=False):
        outputs = []
        while not self.__end:
            current = self.__codes[self.__pointer]
            (opCode, firstType, secondType, outType) = self.__parseCommandMode(current)
            if opCode == 1:
                firstNumber = self.__getValue(firstType, self.__pointer+1)
                secondNumber = self.__getValue(secondType, self.__pointer+2)
                position = self.__getPosition(outType, self.__pointer+3)
                self.__codes[position] = firstNumber + secondNumber
                self.__pointer += 4
                continue
            elif opCode == 2:
                firstNumber = self.__getValue(firstType, self.__pointer+1)
                secondNumber = self.__getValue(secondType, self.__pointer+2)
                position = self.__getPosition(outType, self.__pointer+3)
                self.__codes[position] = firstNumber * secondNumber
                self.__pointer += 4
                continue
            elif opCode == 5:
                condition = self.__getValue(firstType, self.__pointer+1)
                if condition != 0:
                    self.__pointer = self.__getValue(secondType, self.__pointer+2)
                else:
                    self.__pointer += 3
                continue
            elif opCode == 6:
                condition = self.__getValue(firstType, self.__pointer+1)
                if condition == 0:
                    self.__pointer = self.__getValue(secondType, self.__pointer+2)
                else:
                    self.__pointer += 3
                continue
            elif opCode == 7:
                firstNumber = self.__getValue(firstType, self.__pointer+1)
                secondNumber = self.__getValue(secondType, self.__pointer+2)
                position = self.__getPosition(outType, self.__pointer+3)
                self.__codes[position] = 1 if firstNumber < secondNumber else 0
                self.__pointer += 4
                continue
            elif opCode == 8:
                firstNumber = self.__getValue(firstType, self.__pointer+1)
                secondNumber = self.__getValue(secondType, self.__pointer+2)
                position = self.__getPosition(outType, self.__pointer+3)
                self.__codes[position] = 1 if firstNumber == secondNumber else 0
                self.__pointer += 4
                continue
            elif opCode == 3:
                if len(self.__inputs) > 0:
                    inputValue = self.__inputs.pop(0)
                    if not asciiMode:
                        if not noPrint:
                            print(f'Input: {inputValue} [PRESET]')
                    else:
                        if not noPrint:
                            print(chr(inputValue), end='')
                elif len(self.__innerInputs) > 0:
                    inputValue = self.__innerInputs.pop(0)
                elif stopAtInput:
                    return outputs
                else:
                    userInput = input('Input: ')
                    if asciiMode:
                        codeList = self.__convertToAsciiList(userInput)
                        inputValue = codeList.pop(0)
                        self.__innerInputs += codeList
                    else:
                        inputValue = userInput
                position = self.__getPosition(firstType, self.__pointer+1)
                self.__codes[position] = int(inputValue)
                self.__pointer += 2
                continue
            elif opCode == 4:
                result = self.__getValue(firstType, self.__pointer+1)
                if asciiMode:
                    try:
                        if not noPrint:
                            print(chr(result), end='')
                    except ValueError:
                        if not noPrint:
                            print(f'Output: {result}. [TO LARGE IN ASCII MODE]')
                else:
                    if not noPrint:
                        print(f'Output: {result}.')
                self.__pointer += 2
                if stopAtInput:
                    outputs.append(result)
                else:
                    return result
            elif opCode == 9:
                self.__relativeBase += self.__getValue(firstType, self.__pointer+1)
                self.__pointer += 2
                continue
            elif opCode == 99:
                print('\nRun to end.')
                self.__end = True
                continue
            else:
                raise Exception(f'NOT A VALID CODE: {opCode}.')
        return outputs if stopAtInput else None
