def count_trees(x, y):
    file = open('day3.dat', 'r')
    lines = file.readlines()

    tree_count = 0

    row = 0
    position = 0

    for line in lines:
        if row % y == 0:
            text = line.strip()

            if text[position] == "#":
                tree_count = tree_count + 1
            #     print("row " + str(row) + ": hit a tree at position " + str(position))
            # else:
            #     print("row " + str(row) + ": safe")

            position = position + x
            if position > (len(text) - 1):
                position = position - len(text)

        row = row + 1

    return tree_count


count11 = count_trees(1, 1)
count31 = count_trees(3, 1)
count51 = count_trees(5, 1)
count71 = count_trees(7, 1)
count12 = count_trees(1, 2)

print(count11)
print(count31)
print(count51)
print(count71)
print(count12)

result = count11 * count31 * count51 * count71 * count12
print(result)
