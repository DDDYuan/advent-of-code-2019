import math

inputs = [
    '1 ZQVND => 2 MBZM',
    '2 KZCVX, 1 SZBQ => 7 HQFB',
    '1 PFSQF => 9 RSVN',
    '2 PJXQB => 4 FSNZ',
    '20 JVDKQ, 2 LSQFK, 8 SDNCK, 1 MQJNV, 13 LBTV, 3 KPBRX => 5 QBPC',
    '131 ORE => 8 WDQSL',
    '19 BRGJH, 2 KNVN, 3 CRKW => 9 MQJNV',
    '16 DNPM, 1 VTVBF, 11 JSGM => 1 BWVJ',
    '3 KNVN, 1 JQRML => 7 HGQJ',
    '1 MRQJ, 2 HQFB, 1 MQJNV => 5 VQLP',
    '1 PLGH => 5 DMGF',
    '12 DMGF, 3 DNPM, 1 CRKW => 1 CLML',
    '1 JSGM, 1 RSVN => 5 TMNKH',
    '1 RFJLG, 3 CFWC => 2 ZJMC',
    '1 BRGJH => 5 KPBRX',
    '1 SZBQ, 17 GBVJF => 4 ZHGL',
    '2 PLGH => 5 CFWC',
    '4 FCBZS, 2 XQWHB => 8 JSGM',
    '2 PFSQF => 2 KNVN',
    '12 CRKW, 9 GBVJF => 1 KRCB',
    '1 ZHGL => 8 PJMFP',
    '198 ORE => 2 XQWHB',
    '2 BWVJ, 7 CFWC, 17 DPMWN => 3 KZCVX',
    '4 WXBF => 6 JVDKQ',
    '2 SWMTK, 1 JQRML => 7 QXGZ',
    '1 JSGM, 1 LFSFJ => 4 LSQFK',
    '73 KNVN, 65 VQLP, 12 QBPC, 4 XGTL, 10 SWMTK, 51 ZJMC, 4 JMCPR, 1 VNHT => 1 FUEL',
    '1 BWVJ, 7 MBZM => 5 JXZT',
    '10 CFWC => 2 DPMWN',
    '13 LQDLN => 3 LBTV',
    '1 PFZW, 3 LQDLN => 5 PJXQB',
    '2 RSVN, 2 PFSQF => 5 CRKW',
    '1 HGQJ, 3 SMNGJ, 36 JXZT, 10 FHKG, 3 KPBRX, 2 CLML => 3 JMCPR',
    '126 ORE => 4 FCBZS',
    '1 DNPM, 13 MBZM => 5 PLGH',
    '2 XQWHB, 10 FCBZS => 9 LFSFJ',
    '1 DPMWN => 9 PFZW',
    '1 ZJMC, 3 TMNKH => 2 SWMTK',
    '7 TZCK, 1 XQWHB => 5 ZQVND',
    '4 CFWC, 1 ZLWN, 5 RSVN => 2 WXBF',
    '1 BRGJH, 2 CLML => 6 LQDLN',
    '26 BWVJ => 2 GBVJF',
    '16 PJXQB, 20 SDNCK, 3 HQFB, 7 QXGZ, 2 KNVN, 9 KZCVX => 8 XGTL',
    '8 PJMFP, 3 BRGJH, 19 MRQJ => 5 SMNGJ',
    '7 DNPM => 2 SZBQ',
    '2 JQRML, 14 SDNCK => 8 FHKG',
    '1 FSNZ, 6 RFJLG, 2 CRKW => 8 SDNCK',
    '2 CLML, 4 SWMTK, 16 KNVN => 4 JQRML',
    '8 TZCK, 18 WDQSL => 2 PFSQF',
    '1 LSQFK => 8 VTVBF',
    '18 BRGJH, 8 ZHGL, 2 KRCB => 7 VNHT',
    '3 TZCK => 4 DNPM',
    '14 PFZW, 1 PFSQF => 7 BRGJH',
    '21 PLGH, 6 VTVBF, 2 RSVN => 1 ZLWN',
    '149 ORE => 2 TZCK',
    '3 JSGM => 1 RFJLG',
    '4 PFSQF, 4 DMGF => 3 MRQJ'
]


class Reaction:
    def __init__(self, input):
        self.__inputs = []
        [inputsStr, outputStr] = input.split(' => ')
        outputObject = outputStr.split(' ')
        self.__output = {
            'name': outputObject[1], 'amount': int(outputObject[0])}

        inputStrs = inputsStr.split(', ')
        for str in inputStrs:
            inputObject = str.split(' ')
            self.__inputs.append(
                {'name': inputObject[1], 'amount': int(inputObject[0])})

    def isProduce(self, name):
        return name == self.__output['name']

    def calculateNeeds(self, amount):
        times = math.ceil(amount / self.__output['amount'])
        return ([{'name': input['name'], 'amount': times * input['amount']} for input in self.__inputs],
                None if amount - times * self.__output['amount'] == 0 else {'name': self.__output['name'],
                                                                            'amount': times * self.__output[
                                                                                'amount'] - amount})


reactions = [Reaction(string) for string in inputs]


def findReaction(reactions, outputName):
    for reaction in reactions:
        if reaction.isProduce(outputName):
            return reaction
    return None


def onlyORERemain(list):
    return len(list) == 1 and list[0]['name'] == 'ORE'


def findFromList(list, name):
    for item in list:
        if item['name'] == name:
            return item
    return None


def mergeList(list, otherList):
    for item in otherList:
        found = findFromList(list, item['name'])
        if found is not None:
            found['amount'] += item['amount']
        else:
            list.append(item)


def cutOffWaste(list, wasteList):
    for waste in wasteList:
        found = findFromList(list, waste['name'])
        if found is not None:
            if found['amount'] > waste['amount']:
                found['amount'] -= waste['amount']
                wasteList.remove(waste)
            elif found['amount'] < waste['amount']:
                waste['amount'] -= found['amount']
                list.remove(found)
            else:
                wasteList.remove(waste)
                list.remove(found)


def getORENeeded(fuelAmount):
    needs = [{'name': 'FUEL', 'amount': fuelAmount}]
    wastes = []

    while not onlyORERemain(needs):
        cutOffWaste(needs, wastes)
        output = needs.pop(0)
        if output['name'] == 'ORE':
            needs.append(output)
        else:
            (inputs, waste) = findReaction(reactions,
                                           output['name']).calculateNeeds(output['amount'])
            mergeList(needs, inputs)
            if waste is not None:
                mergeList(wastes, [waste])
    ore = needs[0]['amount']
    print(f'Produce {fuelAmount} FUEL needs {ore} ORE.')
    return ore


cargo = 0
cargoLimit = 1000000000000
fuel = 1
while cargo < cargoLimit:
    fuel *= 2
    cargo = getORENeeded(fuel)

print('Start to check')
limitLow, limitHigh, stepLength = fuel // 2, fuel, fuel // 4

while stepLength >= 1:
    checkPoint = limitLow + stepLength
    ore = getORENeeded(checkPoint)
    if ore > cargoLimit:
        limitHigh = checkPoint
    else:
        limitLow = checkPoint
    stepLength //= 2
