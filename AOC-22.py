commands = [
    'deal with increment 65',
    'deal into new stack',
    'deal with increment 25',
    'cut -6735',
    'deal with increment 3',
    'cut 8032',
    'deal with increment 71',
    'cut -4990',
    'deal with increment 66',
    'deal into new stack',
    'cut -8040',
    'deal into new stack',
    'deal with increment 18',
    'cut -8746',
    'deal with increment 42',
    'deal into new stack',
    'deal with increment 17',
    'cut -8840',
    'deal with increment 55',
    'cut -4613',
    'deal with increment 10',
    'cut -5301',
    'deal into new stack',
    'deal with increment 21',
    'cut -5653',
    'deal with increment 2',
    'cut 5364',
    'deal with increment 72',
    'cut -3468',
    'deal into new stack',
    'cut -9661',
    'deal with increment 63',
    'cut 6794',
    'deal with increment 43',
    'cut 2935',
    'deal with increment 66',
    'cut -1700',
    'deal with increment 6',
    'cut 5642',
    'deal with increment 64',
    'deal into new stack',
    'cut -5699',
    'deal with increment 43',
    'cut -9366',
    'deal with increment 42',
    'deal into new stack',
    'cut 2364',
    'deal with increment 13',
    'cut 8080',
    'deal with increment 2',
    'deal into new stack',
    'cut -9602',
    'deal with increment 51',
    'cut 3214',
    'deal into new stack',
    'cut -2995',
    'deal with increment 57',
    'cut -8169',
    'deal into new stack',
    'cut 362',
    'deal with increment 41',
    'cut -4547',
    'deal with increment 56',
    'cut -1815',
    'deal into new stack',
    'cut 1554',
    'deal with increment 71',
    'cut 2884',
    'deal with increment 44',
    'cut -2423',
    'deal with increment 4',
    'deal into new stack',
    'deal with increment 20',
    'cut -2242',
    'deal with increment 48',
    'cut -716',
    'deal with increment 29',
    'cut -6751',
    'deal with increment 45',
    'cut -9511',
    'deal with increment 75',
    'cut -440',
    'deal with increment 35',
    'cut 6861',
    'deal with increment 52',
    'cut -4702',
    'deal into new stack',
    'deal with increment 28',
    'cut 305',
    'deal with increment 16',
    'cut 7094',
    'deal into new stack',
    'cut 5175',
    'deal with increment 30',
    'deal into new stack',
    'deal with increment 61',
    'cut 1831',
    'deal into new stack',
    'deal with increment 25',
    'cut 4043'
]

testCommands = [
    'deal into new stack',
    'cut -2',
    'deal with increment 7',
    'cut 8',
    'cut -4',
    'deal with increment 7',
    'cut 3',
    'deal with increment 9',
    'deal with increment 3',
    'cut -1'
]


def partOne(stackNumber, inputs):
    stack = range(stackNumber)
    while len(inputs) > 0:
        current = inputs.pop(0)
        if current == 'deal into new stack':
            stack = list(reversed(stack))
            print('Reversed')
        elif current.startswith('cut'):
            number = int(current.split(' ')[-1])
            stack = stack[number:] + stack[:number]
            print(f'Cut {number}')
        elif current.startswith('deal with increment'):
            number = int(current.split(' ')[-1])
            newStack = [-1] * len(stack)
            position = 0
            for card in stack:
                newStack[position] = card
                position += number
                if position >= len(stack):
                    position -= len(stack)
            stack = newStack
            print(f'Jump sort {number}')
    return stack


if __name__ == '__main__':
    result = partOne(10007, commands)
    print(result.index(2019))
