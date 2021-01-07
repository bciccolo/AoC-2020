def main():
    file = open('day6.dat', 'r')
    lines = file.readlines()

    group = []
    sum_unique = 0
    sum_common = 0
    row = 0

    for line in lines:
        text = line.strip()

        if text == "":
            # Part 1:
            sum_unique = sum_unique + count_unique_letters(group)
            # Part 2:
            sum_common = sum_common + count_common_letters(group)
            # print(sum)
            group = []
        else:
            group.append(text)

        row = row + 1

        # if row > 17:
        #     break;

    # Process the last group in the file
    sum_unique = sum_unique + count_unique_letters(group)
    sum_common = sum_common + count_common_letters(group)

    print("Unique: " + str(sum_unique))
    print("Common: " + str(sum_common))


def count_common_letters(responses):
    # print(responses)
    letter_counts = {}

    # Assuming letters are unique within a single response,
    # count up the number of occurences for each letter...
    for response in responses:
        for letter in response:
            count = letter_counts.get(letter)
            if count != None:
                letter_counts[letter] = count + 1
            else:
                letter_counts[letter] = 1

    # ...if that count is the same as the length of the responses
    # list then the letter must have appeared in each response
    total = 0
    for count in letter_counts.values():
        if count == len(responses):
            total = total + 1

    return total


def count_unique_letters(responses):
    # print(responses)
    unique_letters = set()

    for response in responses:
        for letter in response:
            unique_letters.add(letter)

    return len(unique_letters)


main()

# list = ["d", "r", "r", "p", "d" ]
# print(count_unique_letters(list))
# print(count_common_letters(list))
# list = ["erxwkjlv", "jpoefrlx", "kjrwxeld" ]
# print(count_unique_letters(list))
# print(count_common_letters(list))