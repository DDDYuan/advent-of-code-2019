import os


def getch():
    import termios
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return _getch()


def generateGraph(x, y):
    return [[0 for x in range(x)] for y in range(y)]


def printGraph(graph, legend, clearScreen=False):
    if clearScreen:
        os.system('clear')
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            print(legend[graph[y][x]], end='')
        print('')
