def part1():
    #
    # Step 1: parse each line into a map of parent bag colors to lists of children bag colors
    #
    parent_to_children = {}

    row = 0
    file = open('day7.dat', 'r')
    lines = file.readlines()
    for line in lines:
        text = line.strip()

        parts = text.split(" bags contain ")
        parent = parts[0]
        children = []

        if parts[1][0:2] != "no":
            for child in parts[1].split(","):
                # strip down to just the color ("4 muted orange bags" becomes "muted orange")
                child = child.strip("0123456789 .") # removes leading space, numbers, and trailing period (for last color only)
                child = child[0:-4].strip() # removes trailing ' bag' or 'bags', then strips the last space for 'bags'
                children.append(child)

        parent_to_children[parent] = children

        row = row + 1

        # if row > 2:
        #     break

    # print(parent_to_children)

    #
    # Step 2: recursively search each entry's values to see if it contains the specified color,
    #         starting with "shiny gold"; add each color to a unique set
    unique_colors = set()
    add_colors(unique_colors, parent_to_children, "shiny gold")

    print(len(unique_colors));


def add_colors(unique_colors, parent_to_children, search_color):
    for parent in parent_to_children:
        if search_color in parent_to_children[parent]:
            unique_colors.add(parent)
            # Recursively check the parent
            add_colors(unique_colors, parent_to_children, parent)


def part2():
    #
    # Step 1: parse each line into a map of parent bag colors to tuples of children bag colors and counts
    #
    parent_to_children = {}

    row = 0
    file = open('day7.dat', 'r')
    lines = file.readlines()
    for line in lines:
        text = line.strip()

        parts = text.split(" bags contain ")
        parent = parts[0]
        children = []

        if parts[1][0:2] != "no":
            for child in parts[1].split(","):
                child = child.strip(" .") # removes leading space and trailing period (for last color only)
                child = child[0:-4].strip() # removes trailing ' bag' or 'bags', then strips the last space for 'bags'
                children.append((child[child.find(" ") + 1:], int(child[0:child.find(" ")])))

        parent_to_children[parent] = children

        row = row + 1

        # if row > 2:
        #     break

    # print(parent_to_children)

    #
    # Step 2: starting with "shiny gold", recursively count how many bags are contained
    #
    print(count_bags("shiny gold", parent_to_children, 0))


def count_bags(search_color, parent_to_children, depth):
    # print("search_color: " + search_color + ", depth: " + str(depth))
    count = 0

    for parent in parent_to_children:
        if parent == search_color:
            for tuple in parent_to_children[parent]:
                # print(tuple)
                count = count + tuple[1] + tuple[1] * count_bags(tuple[0], parent_to_children, depth + 1)
            # print("depth " + str(depth) + " count is " + str(count))

    return count


part1()
part2()