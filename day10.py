FILE_NAME = 'day10.dat'


def part1():
    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    jolts = [int(x) for x in lines]
    jolts.sort()

    # print(jolts)

    singleCount = 0
    tripleCount = 1 # Count the built-in adapter

    lastJolt = 0
    for jolt in jolts:
        if jolt - lastJolt == 1:
            singleCount = singleCount + 1
        elif jolt - lastJolt == 3:
            tripleCount = tripleCount + 1

        lastJolt = jolt

    product = singleCount * tripleCount

    print('Part 1: ' + str(product))


def part2():

    print('Part 2: ' + str(0))


part1()
part2()