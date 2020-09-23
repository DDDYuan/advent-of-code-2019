input = '597967370476643225434885050821479669972464655808057915784174627887807404844096256746766609475415714489100070'\
        '0282145406894565391148614082316823391528522907537400088802997780034166358604662200362077036173827001424673093'\
        '6046471831804308263177331723460787712423587453725840042234550299991238029307205348958992794024402253747340630'\
        '3789446723008746914786318466178612550157702986994072543118894845085458612644498789846243303242282780573773130'\
        '2980250537626019690421374628183021435233762201347301924508183485478127756570654572049228261648895073129197432'\
        '8672252657631353765496979142830459889682475397686651923318015627694176893643969864689257620026916615305397'


def getPattern(basePattern, index):
    position = index + 1
    multiple = [[x] * position for x in basePattern]
    result = list()
    for item in multiple:
        result += item
    return result


def calculateNumber(numbers, pattern):
    sum = 0
    indexNumber = 0
    indexPattern = 1
    while indexNumber < len(numbers):
        sum += numbers[indexNumber] * pattern[indexPattern]
        indexNumber += 1
        indexPattern = 0 if indexPattern + 1 == len(pattern) else indexPattern + 1
    return abs(sum) % 10


def partOne():
    basePattern = [0, 1, 0, -1]
    numberArray = [int(x) for x in input]
    phases = 0
    limit = 100
    while phases < limit:
        newArray = []
        for i in range(len(numberArray)):
            pattern = getPattern(basePattern, i)
            number = calculateNumber(numberArray, pattern)
            newArray.append(number)
        phases += 1
        numberArray = newArray
        print(f'After {phases} phases, result is {"".join([str(x) for x in numberArray])}')
    return numberArray


def calculateTail(array):
    result = []
    for i in range(len(array)):
        number = array[i] if i == 0 else array[i] + result[i-1]
        result.append(number)
    return [x % 10 for x in result]


def partTwo():
    raw = input * 10000
    offset = int(raw[:7])
    numberArray = [int(x) for x in raw[offset:]]
    phases = 0
    limit = 100
    numberArray.reverse()
    while phases < limit:
        phases += 1
        numberArray = calculateTail(numberArray)
        print(f'After {phases} phases')
    numberArray.reverse()
    string = ''.join([str(x) for x in numberArray])
    print(f'Offset is {offset}, message is {string[:8]}')


if __name__ == "__main__":
    # partOne()
    partTwo()
