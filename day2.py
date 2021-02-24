file = open('day2.dat', 'r')
lines = file.readlines()

valid_policy_1 = 0
valid_policy_2 = 0

for line in lines:
    parts = line.strip().split(": ")
    #2-8 t: pncmjxlvckfbtrjh
    #10-11 x: xxxxxxxxxcv

    criteria = parts[0]
    password = parts[1]

    parts = criteria.split(" ")
    counts = parts[0]
    letter = parts[1]

    parts = counts.split("-")
    min = int(parts[0])
    max = int(parts[1])

    # Check policy 1
    count = 0
    for c in password:
        if c == letter:
            count = count + 1

    if count >= min and count <= max:
        valid_policy_1 = valid_policy_1 + 1
        #print("Min {}, Max {}, Letter {}, Password {}".format(min, max, letter, password))

    # Check policy 2
    if (password[min - 1] == letter and password[max - 1] != letter) or \
       (password[min - 1] != letter and password[max - 1] == letter):
        valid_policy_2 = valid_policy_2 + 1
        #print("Pos1 {}, Pos2 {}, Letter {}, Password {}".format(min, max, letter, password))

print("Policy 1: " + str(valid_policy_1))
print("Policy 2: " + str(valid_policy_2))