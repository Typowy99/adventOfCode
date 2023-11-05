with open('3.txt', 'r') as file:
    comp = [line.strip() for line in file.readlines()]

# Initialize an empty dictionary to store the priorities
priority_dict = {}

# Generate priorities for lowercase item types 'a' to 'z'
for i in range(26):
    priority_dict[chr(ord('a') + i)] = i + 1

# Generate priorities for uppercase item types 'A' to 'Z'
for i in range(26):
    priority_dict[chr(ord('A') + i)] = i + 27   


def find_item(a, b, c=None):
    for letter in a:
        if letter in b:
            if c:
                if letter in c:
                    return letter
                else:
                    continue
            return letter


def solution1():
    pkt = 0
    for backpack in comp:
        compartments = round(len(backpack) / 2)
        letter = find_item(backpack[:compartments], backpack[compartments:])
        pkt += priority_dict[letter]
    return pkt


def solution2():
    pkt = 0
    back_3 = []
    for x, backpack in enumerate(comp):
        back_3.append(backpack)
        if len(back_3) == 3:
            letter = find_item(back_3[0], back_3[1], back_3[2])
            pkt += priority_dict[letter]
            back_3 = []
    return pkt


print(f"Answer 1: {solution1()}")
print(f"Answer 2: {solution2()}")