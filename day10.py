FILE_NAME = 'day10.dat'

counts_by_jolt = {}
jolts = []
calls = 0

def count_arrangements(starting_index):
    global counts_by_jolt, jolts, calls

    calls = calls + 1

    # Don't go through all the recursion if we already calculated the value
    # This technique reduces 226775649501184 calls to just 1961 for the full data set
    precalculated_count = counts_by_jolt.get(jolts[starting_index])
    if precalculated_count != None:
        # print('Using count for ' + str(jolts[starting_index]))
        return precalculated_count

    count = 1

    for i in range(starting_index, len(jolts)):
        jolt = jolts[i]

        # print('counting index ' + str(i) + ' (' + str(jolt) + ')')

        if i + 3 < len(jolts) and jolts[i + 3] - jolt <= 3:
            # print('+3 at index ' + str(i))
            count = count + count_arrangements(i + 3)

        if i + 2 < len(jolts) and jolts[i + 2] - jolt <= 3:
            # print('+2 at index ' + str(i))
            count = count + count_arrangements(i + 2)

    # Remember the count for this jolt in case we need to calculate it again
    # print('Setting count for ' + str(jolts[starting_index]) + ': ' + str(count))
    counts_by_jolt[jolts[starting_index]] = count

    return count


def load_jolts():
    global jolts

    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    jolts = [int(x) for x in lines]
    jolts.sort()

    # print(jolts)


def part1():
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
    arrangements = count_arrangements(0)

    if jolts[1] <= 3:
        arrangements = arrangements + count_arrangements(1)

    if jolts[2] <= 3:
        arrangements = arrangements + count_arrangements(2)

    # print('Total calls: ' + str(calls))

    print('Part 2: ' + str(arrangements))


load_jolts()
part1()
part2()