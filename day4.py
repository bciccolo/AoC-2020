import re

def main():
    file = open('day4.dat', 'r')
    lines = file.readlines()

    valid_count = 0
    entry = ""

    row = 0

    for line in lines:
        text = line.strip()

        if text == "":
            # print(str(row + 1) + entry)
            if process_entry(entry, True):
                # print(str(row + 1) + ": " + entry + " is valid")
                valid_count = valid_count + 1
            entry = ""
        else:
            entry = entry + " " + text

        row = row + 1

        # if row > 20:
        #     break;

    # Process the final entry in the file
    if process_entry(entry, True):
        valid_count = valid_count + 1

    print(valid_count)


# Part 1: set extended = False, Part 2: set extended = True
def process_entry(entry, extended):
    valid = "byr" in entry and \
            "iyr" in entry and \
            "eyr" in entry and \
            "hgt" in entry and \
            "hcl" in entry and \
            "ecl" in entry and \
            "pid" in entry

    if valid and extended:
        # print(entry)
        map = {}
        pairs = entry.split()
        for pair in pairs:
            kv = pair.split(":")
            map[kv[0]] = kv[1]

        # Validate birth year
        byr = int(map["byr"])
        valid = valid and byr >= 1920 and byr <= 2002

        # Validate issue year
        iyr = int(map["iyr"])
        valid = valid and iyr >= 2010 and iyr <= 2020

        # Validate expiration year
        eyr = int(map["eyr"])
        valid = valid and eyr >= 2020 and eyr <= 2030

        # Validate height
        unit = map["hgt"][-2:]
        if unit == "cm":
            magnitude = int(map["hgt"][:-2])
            valid = valid and magnitude >= 150 and magnitude <= 193
        elif unit == "in":
            magnitude = int(map["hgt"][:-2])
            valid = valid and magnitude >= 59 and magnitude <= 76
        else:
            valid = False

        # Validate hair color
        hcl = map["hcl"]
        valid = valid and re.search(r"^#[0-9a-f]{6}$", hcl) != None

        # Validate eye color
        ecl = map["ecl"]
        valid = valid and ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        # Validate passport ID
        pid = map["pid"]
        valid = valid and re.search(r"^[0-9]{9}$", pid) != None

    return valid


main()