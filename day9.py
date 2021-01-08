def part1(preamble_size, data):
    index = preamble_size
    while validate_index(data[index], data[index - preamble_size:index]):
        index = index + 1

        # if index > 30:
        #     break;

    return data[index]


def part2(number, data):
    answer = 0

    for x in range(len(data)):
        i = x
        min = data[i]
        max = data[i]
        sum = 0
        while sum < number:
            # print("i: " + str(i) + ", sum: " + str(sum))
            if data[i] < min:
                min = data[i]

            if data[i] > max:
                max = data[i]

            sum = sum + data[i]
            i = i + 1

        if sum == number:
            # print("found it!")
            answer = min + max
            break

    return answer


def load_data():
    file = open('day9.dat', 'r')
    lines = file.readlines()

    data = []
    for line in lines:
        data.append(int(line.strip()))

    return data


def validate_index(check, values):
    # print("Checking " + str(check) + " in " + str(values))
    for i in values:
        for j in values:
            if (i + j == check):
                return True

    return False


# test_values = [ 35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576 ]
# number = part1(5, test_values)
# print("Part 1: " + str(number))
# print("Part 2: " + str(part2(number, test_values)))

data = load_data()
number = part1(25, data)
print("Part 1: " + str(number))
print("Part 2: " + str(part2(number, data)))
