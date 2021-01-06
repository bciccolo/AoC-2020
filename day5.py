def main():
    file = open('day5.dat', 'r')
    lines = file.readlines()

    all_seat_ids = []
    max_seat_id = 0

    for line in lines:
        boarding_pass = line.strip()

        seat_id = get_seat_id(boarding_pass)
        all_seat_ids.append(seat_id)

        if seat_id > max_seat_id:
            max_seat_id = seat_id

    print("Max: " + str(max_seat_id))

    last_id = -1
    all_seat_ids.sort()
    for next_id in all_seat_ids:
        if last_id != -1 and (last_id + 1) != next_id:
            print("Gap between " + str(last_id) + " and " + str(next_id))

        last_id = next_id


def get_seat_id(boarding_pass):
    row_segment = boarding_pass[0:7]
    column_segment = boarding_pass[7:]

    power = 64
    row = 0
    for x in row_segment:
        if x == "B":
            row = row + power
        power = power / 2

    power = 4
    column = 0
    for y in column_segment:
        if y == "R":
            column = column + power
        power = power / 2

    # print(boarding_pass + ": " + str(row) + ", " + str(column) + " --> " + str(row * 8 + column))
    return row * 8 + column


main()

# get_seat_id("BFFFBBFRRR")
# get_seat_id("FFFBBBFRRR")
# get_seat_id("BBFFBBFRLL")